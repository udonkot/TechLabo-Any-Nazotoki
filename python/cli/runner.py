from app.services.stage_service import StageService
from app.services.answer_service import AnswerService
from app.models.stage import StageConfig, StageResult
from cli import display

SUPPORTED_LANGUAGES = {
    "1": "python",
    "2": "java",
}


class GameRunner:
    """CLI ゲームループ管理クラス
    
    Web 化時は cli/runner.py を web/runner.py（FastAPI等）に差し替え、
    app 層（StageService / AnswerService）はそのまま再利用できる。
    """

    def __init__(self):
        self.stage_service = StageService()
        self.answer_service = AnswerService()
        self.language: str = ""
        self.fragments: dict = {}

    # ──────────────────────────────────────────
    # エントリーポイント
    # ──────────────────────────────────────────
    def start(self):
        display.clear_screen()
        display.print_header()
        display.print_prologue()
        input("Enterキーで開始... ")

        self.language = self._select_language()

        for stage in self.stage_service.get_all():
            display.clear_screen()
            display.print_header()

            result = self._run_stage(stage)

            if not result.cleared:
                display.print_game_over()
                return

            if result.fragment is not None:
                self.fragments[f"stage{stage.id}"] = result.fragment

        # 全ステージクリア
        display.clear_screen()
        display.print_header()
        display.print_epilogue(
            final_password=self.fragments.get("stage5", "???"),
            fragments=self.fragments,
        )

    # ──────────────────────────────────────────
    # 言語選択
    # ──────────────────────────────────────────
    def _select_language(self) -> str:
        print("\n使用言語を選択してください:")
        for key, lang in SUPPORTED_LANGUAGES.items():
            print(f"  [{key}] {lang.capitalize()}")
        while True:
            choice = input("\n番号を入力 > ").strip()
            if choice in SUPPORTED_LANGUAGES:
                lang = SUPPORTED_LANGUAGES[choice]
                print(f"\n  言語: {lang.upper()} が選択されました\n")
                return lang
            print("  正しい番号を入力してください")

    # ──────────────────────────────────────────
    # 1ステージ実行
    # ──────────────────────────────────────────
    def _run_stage(self, stage: StageConfig) -> StageResult:
        display.print_stage_header(stage.id, stage.title)
        print(stage.description)

        problem_file = self.stage_service.get_problem_file(stage.id, self.language)
        if problem_file:
            display.print_problem_file(problem_file)

        # stage5 のみ: 収集断片を表示してヒントにする
        if stage.id == 5:
            display.print_fragments(self.fragments)

        for attempt in range(stage.max_attempts):
            user_input = input("\n答えを入力 > ").strip()

            if self.answer_service.check(stage, user_input):
                display.print_unlocked(stage.fragment_label, stage.answer)
                input("\nEnterキーで次のステージへ... ")
                return StageResult(
                    stage_id=stage.id,
                    cleared=True,
                    fragment=stage.answer,
                    attempts_used=attempt + 1,
                )

            remaining = stage.max_attempts - attempt - 1
            hint = stage.hints[attempt] if attempt < len(stage.hints) else ""
            if remaining > 0:
                display.print_wrong(remaining, hint)

        return StageResult(stage_id=stage.id, cleared=False, attempts_used=stage.max_attempts)

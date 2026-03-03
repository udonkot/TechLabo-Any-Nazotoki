import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    print("=" * 60)
    print("      封鎖されたラボからの脱出 - TechLabo Escape")
    print("=" * 60)


def print_stage_header(stage_id: int, title: str):
    print(f"\n{'━' * 60}")
    print(f"  STAGE {stage_id} / 5  ―  {title}")
    print(f"{'━' * 60}")


def print_problem_file(path: str):
    print(f"\n  [問題ファイル] {path}")
    print("  ファイルを開いてコードを解析・修正し、答えを入力してください。\n")


def print_unlocked(fragment_label: str, value: str):
    print(f"\n  [UNLOCKED] 正解！ 断片「{fragment_label}」: '{value}' を入手した。")


def print_wrong(remaining: int, hint: str):
    msg = f"  >> 不正解。残り {remaining} 回。"
    if hint:
        msg += f"\n  {hint}"
    print(msg)


def print_game_over():
    print("\n  >> 試行回数を超えました。もう一度挑戦してください。\n")


def print_fragments(fragments: dict):
    labels = {
        "stage1": "ファイル名",
        "stage2": "拡張子",
        "stage3": "コメント行数",
        "stage4": "開始〜終了位置",
    }
    print("\n  ── 収集した断片 ──────────────────────")
    for key, val in fragments.items():
        label = labels.get(key, key)
        print(f"    [{label}] {val}")
    print()


def print_prologue():
    print(
        """
【プロローグ】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
深夜、あなたは某IT企業の研究所に閉じ込められた。
セキュリティシステムが誤作動し、全ての扉がロックされた。

脱出するには、ラボに残されたコンピュータを駆使して
5つの謎を解き、メインシステムの封印を解く必要がある。

各ステージで問題ファイルが提示される。
コードを修正・実装して答えを導き出せ。

  STAGE 1 → ファイル名         を入手
  STAGE 2 → 拡張子             を入手
  STAGE 3 → コメント行数       を入手
  STAGE 4 → 開始〜終了位置     を入手
  STAGE 5 → 4つを組み合わせて最終パスワードを解読
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    )


def print_epilogue(final_password: str, fragments: dict):
    print(
        f"""
【エンディング】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
全てのロックが解除された。
メインゲートがゆっくりと開いていく...

あなたは無事、ラボからの脱出に成功した。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

★ おめでとうございます！全ステージクリア！ ★
"""
    )
    print_fragments(fragments)
    print(f"  最終パスワード: {final_password}\n")

package cli;

import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Java 版 CLI ゲームループ管理クラス。
 *
 * <p>
 * Python 版の cli/runner.py に相当する。 ステージごとに問題ファイルを提示し、プレイヤーの入力を検証して
 * 断片を収集、全ステージクリアで最終パスワードを表示する。
 *
 * <p>
 * 実行方法（java/ ディレクトリ内）:
 * <pre>
 *   # コマンドプロンプト (cmd)
 *   mvn exec:java -Dexec.mainClass=cli.GameRunner
 *
 *   # PowerShell
 *   mvn exec:java "-Dexec.mainClass=cli.GameRunner"
 * </pre>
 */
public class GameRunner {

    // ──────────────────────────────────────────
    // ステージ定義
    // ──────────────────────────────────────────
    /**
     * ステージ設定の内部データクラス
     */
    private record StageConfig(
            int id,
            String title,
            String description,
            String fragmentLabel,
            String answer,
            List<String> hints,
            String problemFile // java/ からの相対パス
            ) {

    }

    private static final List<StageConfig> STAGES = List.of(
            new StageConfig(
                    1,
                    "エントランス：壊れた認証プログラム",
                    """
            エントランスのドアパネルに古いPCが接続されている。
            認証プログラムにバグがある。

            バグを修正して正しく実行すると、
            「ターゲットのファイル名（拡張子なし）」が出力される。

            >> 答え: プログラムが出力するファイル名を入力せよ""",
                    "ファイル名",
                    "master",
                    List.of(
                            "ヒント: 代入(=)と比較(==)の演算子の違いに注目せよ",
                            "ヒント: return 文で拡張子を除いた値だけを返すよう修正せよ"
                    ),
                    "problems/stage1/BugFix.java"
            ),
            new StageConfig(
                    2,
                    "廊下：怪しいアクセスログ",
                    """
            廊下のPCにアクセスログが残っている。
            異常に多くアクセスされているファイルに共通する「拡張子」を特定せよ。

            問題ファイルのコードを完成させ、access_log.json を解析せよ。

            >> 答え: アクセス数が 500 を超えるファイルに共通する拡張子（ドットなし）""",
                    "拡張子",
                    "log",
                    List.of(
                            "ヒント: access_count が 500 超のエントリだけを抽出せよ",
                            "ヒント: ファイル名を '.' で split して末尾の要素（拡張子）を確認せよ"
                    ),
                    "problems/stage2/DataAnalysis.java"
            ),
            new StageConfig(
                    3,
                    "サーバールーム：FizzBuzzロック",
                    """
            サーバールームのドアパネルに指示が表示されている:

              「1 から 20 までの FizzBuzz を実行し、
               'Fizz' だけになる数の個数を入力せよ」

            問題ファイルの fizzbuzz メソッドを完成させよ。
            ( 'FizzBuzz' は除外すること )

            >> 答え: Fizz のみになる数の個数を入力せよ""",
                    "コメント行数",
                    "5",
                    List.of(
                            "ヒント: 15 は 'FizzBuzz' なので Fizz にはカウントしない",
                            "ヒント: 3の倍数かつ5の倍数でない → 3,6,9,12,18 の個数を数えよ"
                    ),
                    "problems/stage3/FizzBuzz.java"
            ),
            new StageConfig(
                    4,
                    "所長室：センサーエラー範囲の特定",
                    """
            所長室のPCにセンサーログが残っている。
            システムアラートが「エラーが記録されている」と警告している。

            問題ファイルの detect メソッドを完成させ、
            エラー(1) が最初に現れた位置と最後に現れた位置を特定せよ。
            位置は 1-indexed で答えよ。

            >> 答え: 「開始位置~終了位置」の形式で入力せよ（例: 2~8）""",
                    "開始〜終了位置",
                    "3~9",
                    List.of(
                            "ヒント: 配列のインデックスは 0-based だが、答えは 1-indexed で入力せよ",
                            "ヒント: sensor_log.json 内の 1 の位置（1-indexed）を探せ"
                    ),
                    "problems/stage4/Analyze.java"
            ),
            new StageConfig(
                    5,
                    "メインゲート：最終解読",
                    """
            ここまでに集めた4つの断片を組み合わせよ。

              断片1（ファイル名）    + 断片2（拡張子） → 開くべきファイルが分かる
              断片3（コメント行数）  → そのファイルの何番目のコメント行か
              断片4（開始〜終了位置）→ 何文字目〜何文字目を切り出すか

            ../python/data/ フォルダを確認し、該当ファイルを開いて解読せよ。
            ( コメント行 = '//' で始まる行 / 文字位置は 1-indexed )

            >> 答え: 切り出した文字列を入力せよ""",
                    "最終パスワード",
                    "FREEDOM",
                    List.of(
                            "ヒント: 断片1と断片2を組み合わせてファイル名を作れ（例: name.ext）",
                            "ヒント: '//' で始まる行だけを抽出し、断片3番目の行の断片4の範囲を読め"
                    ),
                    null // data ファイルを直接参照
            )
    );

    private static final int MAX_ATTEMPTS = 3;

    // ──────────────────────────────────────────
    // フィールド
    // ──────────────────────────────────────────
    private final Map<String, String> fragments = new LinkedHashMap<>();
    private final Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8);

    // ──────────────────────────────────────────
    // エントリーポイント
    // ──────────────────────────────────────────
    public static void main(String[] args) throws Exception {
        // Windows 環境での文字化けを防ぐために標準出力を UTF-8 に設定
        System.setOut(new PrintStream(System.out, true, StandardCharsets.UTF_8));
        new GameRunner().start();
    }

    public void start() {
        clearScreen();
        printHeader();
        printPrologue();
        waitEnter();

        for (StageConfig stage : STAGES) {
            clearScreen();
            printHeader();

            boolean cleared = runStage(stage);

            if (!cleared) {
                printGameOver();
                return;
            }
        }

        // 全ステージクリア
        clearScreen();
        printHeader();
        printEpilogue();
    }

    // ──────────────────────────────────────────
    // 1ステージ実行
    // ──────────────────────────────────────────
    private boolean runStage(StageConfig stage) {
        printStageHeader(stage.id(), stage.title());
        System.out.println(stage.description());

        if (stage.problemFile() != null) {
            printProblemFile(stage.problemFile());
        }

        // stage5 のみ: 収集断片をヒントとして表示
        if (stage.id() == 5) {
            printFragments();
        }

        for (int attempt = 0; attempt < MAX_ATTEMPTS; attempt++) {
            System.out.print("\n答えを入力 > ");
            String input = scanner.nextLine().strip();

            if (checkAnswer(stage.answer(), input)) {
                printUnlocked(stage.fragmentLabel(), stage.answer());
                fragments.put("stage" + stage.id(), stage.answer());
                waitEnter();
                return true;
            }

            int remaining = MAX_ATTEMPTS - attempt - 1;
            String hint = attempt < stage.hints().size() ? stage.hints().get(attempt) : "";
            if (remaining > 0) {
                printWrong(remaining, hint);
            }
        }

        return false;
    }

    // ──────────────────────────────────────────
    // 答え合わせ（大文字小文字・前後空白無視）
    // ──────────────────────────────────────────
    private boolean checkAnswer(String correct, String input) {
        return correct.trim().equalsIgnoreCase(input.trim());
    }

    // ──────────────────────────────────────────
    // 表示メソッド群
    // ──────────────────────────────────────────
    private void clearScreen() {
        try {
            if (System.getProperty("os.name").toLowerCase().contains("win")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception ignored) {
            System.out.println("\n".repeat(40));
        }
    }

    private void printHeader() {
        System.out.println("=".repeat(60));
        System.out.println("      封鎖されたラボからの脱出 - TechLabo Escape");
        System.out.println("=".repeat(60));
    }

    private void printStageHeader(int id, String title) {
        System.out.println("\n" + "━".repeat(60));
        System.out.printf("  STAGE %d / 5  ―  %s%n", id, title);
        System.out.println("━".repeat(60));
    }

    private void printProblemFile(String path) {
        System.out.println("\n  [問題ファイル] " + path);
        System.out.println("  ファイルを開いてコードを解析・修正し、答えを入力してください。\n");
    }

    private void printUnlocked(String label, String value) {
        System.out.printf("%n  [UNLOCKED] 正解！ 断片「%s」: '%s' を入手した。%n", label, value);
    }

    private void printWrong(int remaining, String hint) {
        System.out.printf("  >> 不正解。残り %d 回。%n", remaining);
        if (!hint.isEmpty()) {
            System.out.println("  " + hint);
        }
    }

    private void printGameOver() {
        System.out.println("\n  >> 試行回数を超えました。もう一度挑戦してください。\n");
    }

    private void printFragments() {
        Map<String, String> labels = Map.of(
                "stage1", "ファイル名",
                "stage2", "拡張子",
                "stage3", "コメント行数",
                "stage4", "開始〜終了位置"
        );
        System.out.println("\n  ── 収集した断片 ──────────────────────");
        fragments.forEach((key, val) -> {
            String label = labels.getOrDefault(key, key);
            System.out.printf("    [%s] %s%n", label, val);
        });
        System.out.println();
    }

    private void printPrologue() {
        System.out.println("""

【プロローグ】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
深夜、あなたは某IT企業の研究所に閉じ込められた。
セキュリティシステムが誤作動し、全ての扉がロックされた。

脱出するには、ラボに残されたコンピュータを駆使して
5つの謎を解き、メインシステムの封印を解く必要がある。

各ステージで問題ファイルが提示される。
コードを解析・実装して答えを導き出せ。

  STAGE 1 → ファイル名         を入手
  STAGE 2 → 拡張子             を入手
  STAGE 3 → コメント行数       を入手
  STAGE 4 → 開始〜終了位置     を入手
  STAGE 5 → 4つを組み合わせて最終パスワードを解読
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""");
    }

    private void printEpilogue() {
        System.out.println("""

【エンディング】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
全てのロックが解除された。
メインゲートがゆっくりと開いていく...

あなたは無事、ラボからの脱出に成功した。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

★ おめでとうございます！全ステージクリア！ ★
""");
        printFragments();
        System.out.println("  最終パスワード: " + fragments.getOrDefault("stage5", "???"));
        System.out.println();
    }

    private void waitEnter() {
        System.out.print("Enterキーで続ける... ");
        scanner.nextLine();
    }
}

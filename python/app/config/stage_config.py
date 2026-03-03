from app.models.stage import StageConfig

# ステージ設定一覧（答え・ヒントを含むサーバーサイド設定）
# Web 化時はこのファイルはバックエンド専用として公開しない
STAGE_CONFIGS = [
    StageConfig(
        id=1,
        title="エントランス：壊れた認証プログラム",
        description=(
            "エントランスのドアパネルに古いPCが接続されている。\n"
            "認証プログラムにバグがある。\n\n"
            "バグを修正して正しく実行すると、\n"
            "「ターゲットのファイル名（拡張子なし）」が出力される。\n\n"
            ">> 答え: プログラムが出力するファイル名を入力せよ"
        ),
        fragment_label="ファイル名",
        answer="master",
        hints=[
            "ヒント: 代入(=)と比較(==)の演算子の違いに注目せよ",
            "ヒント: return 文で拡張子を除いた値だけを返すよう修正せよ",
        ],
        problem_files={
            "python": "problems/stage1/bug_fix.py",
            "java":   "../java/problems/stage1/BugFix.java",
        },
    ),
    StageConfig(
        id=2,
        title="廊下：怪しいアクセスログ",
        description=(
            "廊下のPCにアクセスログが残っている。\n"
            "異常に多くアクセスされているファイルに共通する「拡張子」を特定せよ。\n\n"
            "問題ファイルのコードを完成させ、access_log.json を解析せよ。\n\n"
            ">> 答え: アクセス数が 500 を超えるファイルに共通する拡張子（ドットなし）"
        ),
        fragment_label="拡張子",
        answer="log",
        hints=[
            "ヒント: access_count が 500 超のエントリだけを抽出せよ",
            "ヒント: ファイル名を '.' で split して末尾の要素（拡張子）を確認せよ",
        ],
        problem_files={
            "python": "problems/stage2/data_analysis.py",
            "java":   "../java/problems/stage2/DataAnalysis.java",
        },
    ),
    StageConfig(
        id=3,
        title="サーバールーム：FizzBuzzロック",
        description=(
            "サーバールームのドアパネルに指示が表示されている:\n\n"
            "  「1 から 20 までの FizzBuzz を実行し、\n"
            "   'Fizz' だけになる数の個数を入力せよ」\n\n"
            "問題ファイルの fizzbuzz 関数を完成させよ。\n"
            "( 'FizzBuzz' は除外すること )\n\n"
            ">> 答え: Fizz のみになる数の個数を入力せよ"
        ),
        fragment_label="コメント行数",
        answer="5",
        hints=[
            "ヒント: 15 は 'FizzBuzz' なので Fizz にはカウントしない",
            "ヒント: 3の倍数かつ5の倍数でない → 3,6,9,12,18 の個数を数えよ",
        ],
        problem_files={
            "python": "problems/stage3/fizzbuzz.py",
            "java":   "../java/problems/stage3/FizzBuzz.java",
        },
    ),
    StageConfig(
        id=4,
        title="所長室：センサーエラー範囲の特定",
        description=(
            "所長室のPCにセンサーログが残っている。\n"
            "システムアラートが「エラーが記録されている」と警告している。\n\n"
            "問題ファイルの detect 関数を完成させ、\n"
            "エラー(1) が最初に現れた位置と最後に現れた位置を特定せよ。\n"
            "位置は 1-indexed で答えよ。\n\n"
            ">> 答え: 「開始位置~終了位置」の形式で入力せよ（例: 2~8）"
        ),
        fragment_label="開始〜終了位置",
        answer="3~9",
        hints=[
            "ヒント: リストのインデックスは 0-based だが、答えは 1-indexed で入力せよ",
            "ヒント: sensor_log.json 内の 1 の位置（1-indexed）を探せ",
        ],
        problem_files={
            "python": "problems/stage4/analyze.py",
            "java":   "../java/problems/stage4/Analyze.java",
        },
    ),
    StageConfig(
        id=5,
        title="メインゲート：最終解読",
        description=(
            "ここまでに集めた4つの断片を組み合わせよ。\n\n"
            "  断片1（ファイル名）    + 断片2（拡張子） → 開くべきファイルが分かる\n"
            "  断片3（コメント行数）  → そのファイルの何番目のコメント行か\n"
            "  断片4（開始〜終了位置）→ 何文字目〜何文字目を切り出すか\n\n"
            "data/ フォルダを確認し、該当ファイルを開いて解読せよ。\n"
            "( コメント行 = '#' で始まる行 / 文字位置は 1-indexed )\n\n"
            ">> 答え: 切り出した文字列を入力せよ"
        ),
        fragment_label="最終パスワード",
        answer="FREEDOM",
        hints=[
            "ヒント: 断片1と断片2を組み合わせてファイル名を作れ（例: name.ext）",
            "ヒント: '#' で始まる行だけを抽出し、断片3番目の行の断片4の範囲を読め",
        ],
        problem_files={},  # stage5 は data/master.log を直接参照
    ),
]

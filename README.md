# TechLabo Any Nazotoki

プログラミングのスキルアップを兼ねた謎解き脱出ゲームです。  
各ステージでコードのデバッグ・実装・データ推理を行い、最終パスワードを解読して脱出を目指します。

## ストーリー

深夜、某IT企業の研究所に閉じ込められた。  
セキュリティシステムが誤作動し、全ての扉がロックされた。  
ラボに残されたコンピュータを使い、5つの謎を解いて脱出せよ。

## ステージ構成

| ステージ | 内容                            | 答えの種類         |
| -------- | ------------------------------- | ------------------ |
| STAGE 1  | バグ修正                        | ファイル名         |
| STAGE 2  | データ推理（アクセスログ解析）  | 拡張子             |
| STAGE 3  | FizzBuzz コーディング           | コメント行数       |
| STAGE 4  | センサーログ異常検知            | 開始位置〜終了位置 |
| STAGE 5  | 4つの断片を組み合わせて最終解読 | パスワード         |

## ディレクトリ構成

```
TechLabo-Any-Nazotoki/
├── python/                  # Python 版
│   ├── main.py              # CLI エントリーポイント
│   ├── requirements.txt     # 依存パッケージ
│   ├── app/                 # コアロジック（CLI/Web 共通）
│   │   ├── config/          # ステージ設定・正解管理
│   │   ├── models/          # データクラス
│   │   └── services/        # ビジネスロジック
│   ├── cli/                 # CLI 固有コード
│   ├── data/
│   │   └── master.log       # STAGE 5 解読用ファイル
│   ├── problems/            # 問題ファイル（プレイヤーが編集）
│   │   ├── stage1/
│   │   ├── stage2/
│   │   ├── stage3/
│   │   └── stage4/
│   └── answers/             # 解答ファイル（ネタバレ注意）
│       ├── stage1/
│       ├── stage2/
│       ├── stage3/
│       └── stage4/
│
└── java/                    # Java 版
    ├── pom.xml              # Maven 設定（依存ライブラリ定義）
    ├── problems/            # 問題ファイル（プレイヤーが編集）
    │   ├── stage1/
    │   ├── stage2/
    │   ├── stage3/
    │   └── stage4/
    └── answers/             # 解答ファイル（ネタバレ注意）
        ├── stage1/
        ├── stage2/
        ├── stage3/
        └── stage4/
```

---

## 環境構築・実行手順

### Python 版

#### 必要環境
- Python 3.11 以上

#### セットアップ

```bash
cd python

# 仮想環境の作成
python -m venv .venv

# 仮想環境の有効化
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# 依存パッケージのインストール
pip install -r requirements.txt
```

#### ゲームの起動

```bash
# python/ ディレクトリ内で実行
python main.py
```

#### 問題ファイルの実行（単体）

```bash
# 例: Stage 1 の問題を実行
python problems/stage1/bug_fix.py

# 例: Stage 3 の問題を実行
python problems/stage3/fizzbuzz.py
```

#### 仮想環境の終了

```bash
deactivate
```

---

### Java 版

#### 必要環境
- Java 17 以上
- Maven 3.8 以上

#### セットアップ・ビルド

```bash
cd java

# 依存ライブラリのダウンロード & コンパイル
mvn compile

# VS Code 用に依存 JAR を lib/ にコピー（VS Code でのエラー解消）
mvn dependency:copy-dependencies -DoutputDirectory=lib
```

#### 問題ファイルの実行

```bash
# java/ ディレクトリ内で実行

# STAGE 1: バグ修正
mvn exec:java -Dexec.mainClass=problems.stage1.BugFix

# STAGE 2: データ推理
mvn exec:java -Dexec.mainClass=problems.stage2.DataAnalysis

# STAGE 3: FizzBuzz
mvn exec:java -Dexec.mainClass=problems.stage3.FizzBuzz

# STAGE 4: センサーログ解析
mvn exec:java -Dexec.mainClass=problems.stage4.Analyze
```

#### 解答ファイルの実行（ネタバレ注意）

```bash
mvn exec:java -Dexec.mainClass=answers.stage1.Answer
mvn exec:java -Dexec.mainClass=answers.stage2.Answer
mvn exec:java -Dexec.mainClass=answers.stage3.Answer
mvn exec:java -Dexec.mainClass=answers.stage4.Answer
```

---

## 拡張について

| 目的             | 対応方法                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| 新言語の追加     | ルート直下に `{言語}/` フォルダを追加し、同じ `problems/` 構成を用意する        |
| 新ステージの追加 | `python/app/config/stage_config.py` にエントリを追加するだけ                    |
| Web アプリ化     | `python/cli/runner.py` を Web フレームワーク用に差し替え（`app/` 層は再利用可） |

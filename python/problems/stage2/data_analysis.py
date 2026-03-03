# ============================================================
# STAGE 2: データ推理問題
# ============================================================
# access_log.json を解析し、
# アクセス数が 500 を超えるファイルに共通する「拡張子」を求めよ。
#
# 期待する動作:
#   find_common_extension() が拡張子（ドットなし）を出力する
# ============================================================

import json
import os


def find_common_extension(log_data: list, threshold: int) -> str:
    """
    log_data: [{"file": str, "access_count": int}, ...]
    threshold を超える access_count を持つファイルの共通拡張子を返せ。
    """
    # ここを実装せよ
    pass


base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "access_log.json"), encoding="utf-8") as f:
    data = json.load(f)

result = find_common_extension(data, threshold=500)
print(result)

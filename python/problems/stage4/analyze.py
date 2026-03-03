# ============================================================
# STAGE 4: コーディング + データ推理問題
# ============================================================
# sensor_log.json にはセンサーの記録が配列で格納されている。
#   0 = 正常 / 1 = エラー
#
# find_error_range() を完成させ、
# エラー(1) が「最初に現れた位置」と「最後に現れた位置」を
# 1-indexed で求めよ。
#
# 出力形式: 開始位置~終了位置  例) 2~8
# ============================================================

import json
import os
from typing import Tuple


def find_error_range(log: list) -> Tuple[int, int]:
    """
    log: 0 か 1 の整数リスト
    エラー(1) の最初と最後の位置を 1-indexed のタプルで返せ。
    """
    # ここを実装せよ
    pass


base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "sensor_log.json"), encoding="utf-8") as f:
    log = json.load(f)

start, end = find_error_range(log)
print(f"{start}~{end}")

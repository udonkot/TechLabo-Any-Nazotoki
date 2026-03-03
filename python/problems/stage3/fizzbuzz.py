# ============================================================
# STAGE 3: コーディング問題
# ============================================================
# fizzbuzz 関数を完成させ、
# 1 から 20 までで "Fizz" のみになる数の個数を出力せよ。
#
# ルール:
#   3 の倍数かつ 5 の倍数でない → "Fizz"
#   5 の倍数かつ 3 の倍数でない → "Buzz"
#   3 かつ 5 の倍数             → "FizzBuzz"
#   それ以外                    → 数字をそのまま追加
#
# 注意: "FizzBuzz" は "Fizz" に含めないこと
# ============================================================


def fizzbuzz(n: int) -> list:
    results = []
    for i in range(1, n + 1):
        # ここを実装せよ
        pass
    return results


result = fizzbuzz(20)
fizz_only = [x for x in result if x == "Fizz"]
print(len(fizz_only))

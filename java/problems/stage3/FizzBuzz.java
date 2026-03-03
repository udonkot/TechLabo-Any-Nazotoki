// ============================================================
// STAGE 3: コーディング問題
// ============================================================
// fizzbuzz メソッドを完成させ、
// 1 から 20 までで "Fizz" のみになる数の個数を出力せよ。
//
// ルール:
//   3 の倍数かつ 5 の倍数でない → "Fizz"
//   5 の倍数かつ 3 の倍数でない → "Buzz"
//   3 かつ 5 の倍数             → "FizzBuzz"
//   それ以外                    → 数字をそのまま追加
//
// 注意: "FizzBuzz" は "Fizz" に含めないこと
// ============================================================
package problems.stage3;

import java.util.ArrayList;
import java.util.List;

public class FizzBuzz {

    static List<String> fizzbuzz(int n) {
        List<String> results = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            // ここを実装せよ
        }
        return results;
    }

    public static void main(String[] args) {
        List<String> result = fizzbuzz(20);
        long fizzCount = result.stream().filter(s -> s.equals("Fizz")).count();
        System.out.println(fizzCount);
    }
}

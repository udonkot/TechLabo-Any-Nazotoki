// ============================================================
// STAGE 4: コーディング + データ推理問題
// ============================================================
// sensor_log.json にはセンサーの記録が配列で格納されている。
//   0 = 正常 / 1 = エラー
//
// findErrorRange() を完成させ、
// エラー(1) が「最初に現れた位置」と「最後に現れた位置」を
// 1-indexed で求めよ。
//
// 出力形式: 開始位置~終了位置  例) 2~8
// ============================================================
package problems.stage4;

import org.json.JSONArray;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Analyze {

    /**
     * log: 0 か 1 の整数配列 エラー(1) の最初と最後の位置を 1-indexed で "start~end" 形式の文字列で返せ。
     */
    static String findErrorRange(int[] log) {
        // ここを実装せよ
        return null;
    }

    public static void main(String[] args) throws Exception {
        String content = new String(Files.readAllBytes(Paths.get("problems/stage4/sensor_log.json")));
        JSONArray jsonArray = new JSONArray(content);

        int[] log = new int[jsonArray.length()];
        for (int i = 0; i < jsonArray.length(); i++) {
            log[i] = jsonArray.getInt(i);
        }

        System.out.println(findErrorRange(log));
    }
}

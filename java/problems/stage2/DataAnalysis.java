// ============================================================
// STAGE 2: データ推理問題
// ============================================================
// access_log.json を解析し、
// アクセス数が 500 を超えるファイルに共通する「拡張子」を求めよ。
//
// 期待する動作:
//   findCommonExtension() が拡張子（ドットなし）を出力する
// ============================================================
package problems.stage2;

import org.json.JSONArray;
import org.json.JSONObject;
import java.nio.file.Files;
import java.nio.file.Paths;

public class DataAnalysis {

    /**
     * logData: JSONArray [{"file": String, "access_count": int}, ...] threshold
     * を超える access_count を持つファイルの共通拡張子を返せ。
     */
    static String findCommonExtension(JSONArray logData, int threshold) {
        // ここを実装せよ
        return null;
    }

    public static void main(String[] args) throws Exception {
        String content = new String(Files.readAllBytes(Paths.get("problems/stage2/access_log.json")));
        JSONArray data = new JSONArray(content);

        String result = findCommonExtension(data, 500);
        System.out.println(result);
    }
}

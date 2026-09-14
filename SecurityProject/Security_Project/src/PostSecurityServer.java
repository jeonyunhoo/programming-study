import com.sun.net.httpserver.HttpExchange; // 한 번의 HTTP 요청과 응답 정보를 다루는 클래스를 불러옵니다.
import com.sun.net.httpserver.HttpServer; // 자바 기본 웹 서버를 만드는 클래스를 불러옵니다.

import java.io.IOException; // 입출력 중 발생할 수 있는 예외 클래스를 불러옵니다.
import java.io.OutputStream; // 서버가 브라우저로 데이터를 보내는 출력 통로를 불러옵니다.
import java.net.InetSocketAddress; // 서버 주소와 포트번호를 지정하는 클래스를 불러옵니다.
import java.nio.charset.StandardCharsets; // 한글을 UTF-8로 처리하기 위한 상수를 불러옵니다.

import java.util.HashMap;
import java.util.Map;
import java.net.URLDecoder;

public class PostSecurityServer {

    // POST 데이터를 항목별로 분리하는 메서드
    private static Map<String, String> parseFormData(
            String requestData
    ) {

        Map<String, String> formData = new HashMap<>();

        String[] items = requestData.split("&");

        for (String item : items) {

            String[] nameAndValue = item.split("=", 2);

            String name = URLDecoder.decode(
                    nameAndValue[0],
                    StandardCharsets.UTF_8
            );

            String value = "";

            if (nameAndValue.length == 2) {
                value = URLDecoder.decode(
                        nameAndValue[1],
                        StandardCharsets.UTF_8
                );
            }

            formData.put(name, value);
        }

        return formData;
    }

    // 오류 화면을 만드는 메서드
    private static String errorPage(String message) {

        return """
                <!DOCTYPE html>
                <html lang="ko">
                <head>
                    <meta charset="UTF-8">
                    <title>입력 오류</title>
                </head>
                <body>
                    <h2>입력값이 올바르지 않습니다.</h2>

                    <p>%s</p>

                    <a href="/">다시 입력하기</a>
                </body>
                </html>
                """.formatted(message);
    }

    // 브라우저에 응답을 전송하는 메서드
    private static void sendResponse(
            HttpExchange exchange,
            int statusCode,
            String responseText
    ) throws IOException {

        byte[] responseBytes =
                responseText.getBytes(StandardCharsets.UTF_8);

        exchange.getResponseHeaders().set(
                "Content-Type",
                "text/html; charset=UTF-8"
        );

        exchange.sendResponseHeaders(
                statusCode,
                responseBytes.length
        );

        try (OutputStream output =
                     exchange.getResponseBody()) {

            output.write(responseBytes);
        }
    }
}


import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpsConfigurator;
import com.sun.net.httpserver.HttpsServer;

import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.KeyStore;

import javax.net.ssl.KeyManagerFactory;
import javax.net.ssl.SSLContext;

public class HttpHttpsCompareServer {

    public static void main(String[] args) throws Exception {

        // 1. 실습용 인증서 파일을 열 때 사용할 비밀번호입니다.
        //    실제는 비밀번호를 소스 코드에 직접 적지 않습니다.
        char[] password = "classroom123".toCharArray();

        // 2. keytool로 만든 인증서 파일을 읽습니다.
        // classroom-local.p12 파일을 열어 Java가 인증서와 개인키를 사용할 수 있게 읽어 오는 부분
        KeyStore store = KeyStore.getInstance("PKCS12");
        //KeyStore는 인증서와 개인키를 보관하는 보관함을 다루는 Java 객체
        //PKCS12는 인증서와 개인키를 한 파일에 보관하기 위한 표준 파일 형식

        try (var input = Files.newInputStream(
                Path.of("classroom-local.p12"))) {
            //읽을 파일의 경로를 지정합니다. 현재 폴더에서 찾음
            //.p12: PKCS12 형식 파일에 흔히 붙이는 파일 확장자
            store.load(input, password);
        }

        // 3. 인증서와 개인키를 HTTPS 서버에서 사용할 수 있도록 준비합니다.
        KeyManagerFactory keys = KeyManagerFactory.getInstance(
                KeyManagerFactory.getDefaultAlgorithm()
        );

        keys.init(store, password);

        // TLS: 그 인증서와 키를 활용해 통신을 보호하는 기술
        // 4. HTTPS 통신을 위한 TLS 설정을 만듭니다.
        SSLContext tls = SSLContext.getInstance("TLS");
        tls.init(keys.getKeyManagers(), null, null);

        // 5. HTTP 서버를 자기 컴퓨터의 8081번 포트에서 실행하도록 만듭니다.
        HttpServer http = HttpServer.create(
                new InetSocketAddress("127.0.0.1", 8081),
                0
        );

        // 6. HTTPS 서버를 자기 컴퓨터의 8443번 포트에서 실행하도록 만듭니다.
        HttpsServer https = HttpsServer.create(
                new InetSocketAddress("127.0.0.1", 8443),
                0
        );

        // 7. HTTPS 서버에 앞에서 만든 TLS 설정을 연결합니다.
        https.setHttpsConfigurator(new HttpsConfigurator(tls));

        // 8. HTTP와 HTTPS가 같은 요청을 처리하도록 합니다.
        //    두 서버의 응답이 같아야 전송 방식의 차이를 비교하기 쉽습니다.
        HttpHandler handler = exchange -> {

            // 클라이언트가 보낸 내용을 읽습니다.
            String sent = new String(
                    exchange.getRequestBody().readAllBytes(),
                    StandardCharsets.UTF_8
            );

            // 받은 내용을 응답 문장에 넣습니다.
            // 예: note=classroom을 보내면
            //     received: note=classroom을 응답합니다.
            String response = "received: " + sent;
            byte[] answer = response.getBytes(StandardCharsets.UTF_8);

            // 응답 내용이 일반 텍스트이며 UTF-8을 사용한다고 알립니다.
            exchange.getResponseHeaders().set(
                    "Content-Type",
                    "text/plain; charset=UTF-8"
            );

            // HTTP 상태 코드 200과 응답 데이터 길이를 보냅니다.
            exchange.sendResponseHeaders(200, answer.length);

            // 실제 응답 내용을 클라이언트에 보냅니다.
            try (var output = exchange.getResponseBody()) {
                output.write(answer);
            }
        };

        // 9. 두 서버 모두 주소 "/"로 온 요청을 처리하게 합니다.
        http.createContext("/", handler);
        https.createContext("/", handler);

        // 10. 서버 두 개를 시작합니다.
        http.start();
        https.start();

        System.out.println("HTTP  http://127.0.0.1:8081/");
        System.out.println("HTTPS https://127.0.0.1:8443/");
    }
}
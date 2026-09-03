import java.sql.*;
import java.util.Scanner;

public class MemberInsert {

    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/movie_db";
        String user = "root";
        String password = "sql12345";

        Scanner scanner = new Scanner(System.in);

        try {

            Connection conn = DriverManager.getConnection(url, user, password);

            System.out.println("[영화관 회원 가입]");

            System.out.print("아이디: ");
            String inputId = scanner.nextLine();

            System.out.print("비밀번호: ");
            String inputPass = scanner.nextLine();

            System.out.print("이름: ");
            String inputName = scanner.nextLine();

            System.out.print("회원권한: ");
            String inputRole = scanner.nextLine();

            String sql = "insert into member (user_id, user_password, m_name, m_role) " +
                         "values (?, ?, ?, ?) ";

            PreparedStatement pstmt = conn.prepareStatement(sql);

            // 첫 번째 ?에 아이디 입력
            pstmt.setString(1, inputId);

            // 두 번째 ?에 비밀번호 입력
            pstmt.setString(2,inputPass);

            pstmt.setString(3,inputName);

            pstmt.setString(4,inputRole);

            System.out.println("실행할 SQL문");
            System.out.println(sql);

            int count = pstmt.executeUpdate();
            if(count > 0) {

                System.out.println("\n가입 성공");
            } else {

                System.out.println("형식에 맞지 않는 기입이 있습니다.");
            }

            pstmt.close();
            conn.close();
        } catch(SQLException e) {

            System.out.println("MySQL 연셜 실패");

            System.out.println("오류 내용: " + e.getMessage());
        } finally {

            scanner.close();
        }
    }
}

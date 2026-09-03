import java.sql.*;
import java.util.Scanner;

public class SecureLogin {

    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/movie_db";
        String user = "root";
        String password = "sql12345";

        Scanner scanner = new Scanner(System.in);

        try {

            Connection conn = DriverManager.getConnection(url, user, password);

            System.out.println("[영화관 회원 로그인]");

            System.out.print("아이디: ");
            String inputId = scanner.nextLine();

            System.out.print("비밀번호: ");
            String inputPass = scanner.nextLine();

            String sql = "select user_id, m_name, m_id, m_role " +
                         "from member " +
                         "where user_id = ? "+
                         "and user_password = ?";

            PreparedStatement pstmt = conn.prepareStatement(sql);

            // 첫 번째 ?에 아이디 입력
            pstmt.setString(1, inputId);

            // 두 번째 ?에 비밀번호 입력
            pstmt.setString(2,inputPass);

            System.out.println("실행할 SQL문");
            System.out.println(sql);

            ResultSet rs = pstmt.executeQuery();

            if(rs.next()) {

                // sql의 결과 중 필요한 것만 java의 변수로 옮겨와야 함
                String memberName = rs.getString("m_name");
                String memberRole = rs.getString("m_role");

                System.out.println("\n로그인 성공");
                System.out.println(memberName + "님, 환영합니다.");
                System.out.println("회원 권한: " + memberRole);
            } else {

                System.out.println("아이디 혹은 비밀번호가 옳지 않습니다.");
            }

            rs.close();
            pstmt.close();
            conn.close();
        } catch (SQLException e) {

            System.out.println("MySQL 연셜 실패");

            System.out.println("오류 내용: " + e.getMessage());
        } finally {

            scanner.close();
        }
    }
}
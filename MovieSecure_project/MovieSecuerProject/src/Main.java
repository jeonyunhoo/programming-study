import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Main {

    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/movie_db";
        String user = "root";
        String password = "sql12345";

        try {

            Connection conn =
                    DriverManager.getConnection(url, user, password);

            System.out.println("MySQL 연결 성공");

            conn.close();
        } catch (SQLException e) {

            System.out.println("MySQL 연셜 실패");

            System.out.println("오류 내용: " + e.getMessage());
        }
    }
}
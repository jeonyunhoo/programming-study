import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.interfaces.PBEKey;
import javax.crypto.spec.PBEKeySpec;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Scanner;

public class PasswordUtil {

    private static final int ITERATIONS = 600000;
    private static final int KEY_LENGTH = 256;
    public static String  generateSalt() {

        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[16];
        random.nextBytes(salt);
        return Base64.getEncoder().encodeToString(salt);
    }

    public static String hashPassword(
            String password,
            String salt
    ) throws Exception {

        byte[] saltByte = Base64.getDecoder().decode(salt);
        PBEKeySpec spec = new PBEKeySpec(

                password.toCharArray(),
                saltByte,
                ITERATIONS,
                KEY_LENGTH
        );

        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");

        byte[] hashBytes = factory.generateSecret(spec).getEncoded();

        return Base64.getEncoder().encodeToString(hashBytes);
    }

    public static boolean verifyPassword(

            String inputPassword,
            String savedSalt,
            String savedHash
    ) throws Exception {

        if(savedSalt == null || savedHash == null) {

            return false;
        }

        String inputHash = hashPassword(
                inputPassword,
                savedSalt
        );

        return inputHash.equals(savedHash);
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        try {

            System.out.print("비밀번호 입력: ");
            String password = scanner.nextLine();

            String salt = generateSalt();

            String passwordHash = hashPassword(password, salt);

            System.out.println("\n[반환 결과]");
            System.out.println("입력 비밀번호: " + password);
            System.out.println("생성된 솔트: " + salt);
            System.out.println("비밀번호 해시: " + passwordHash);
            System.out.print("\n로그인 확인용 비밀번호 입력: ");
            String checkPassword = scanner.nextLine();

            boolean passwordMatch =
                    verifyPassword(

                            checkPassword,
                            salt,
                            passwordHash
                    );
            if(passwordMatch) {

                System.out.println("비밀번호가 일치합니다.");
            } else {

                System.out.println("비밀번호가 일치하지 않습니다.");
            }
        } catch (Exception e) {

            System.out.println("비밀번호 처리 중 오류가 발생했습니다.");
            System.out.println("오류 내용: " + e.getMessage());
        } finally {

            scanner.close();
        }
    }
}

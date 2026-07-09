package ex01;

interface Login {

    void login();
    void logout();
}

interface Print {

    void printinfo();
}

class student implements Login, Print {

    @Override
    public void login() {

        System.out.println("학생 계정으로 로그인했습니다.");
    }

    @Override
    public void logout() {

        System.out.println("학생 계정이 로그아웃되었습니다.");
    }

    @Override
    public void printinfo() {

        System.out.println("학생 정보를 출력합니다.");
    }
}

class teacher implements Login, Print {

    @Override
    public void login() {

        System.out.println("교사 계정으로 로그인했습니다.");
    }

    @Override
    public void logout() {

        System.out.println("교사 계정이 로그아웃되었습니다.");
    }

    @Override
    public void printinfo() {

        System.out.println("교사 정보를 출력합니다.");
    }
}

public class InterfaceMain {

    public static void main() {

        Login s = new student();
        Print s1 = new student();

        Login t = new teacher();
        Print t1 = new teacher();

        s.login();
        s1.printinfo();
        s.logout();
        System.out.println();
        t.login();
        t1.printinfo();
        t.logout();
    }
}

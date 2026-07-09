package ex01;

abstract class Company { // 부모 클래스

    String name;

    Company(String name) {

        this.name = name;
    }

    void start() {

        System.out.println(name + "(이)가 출근했습니다.");
    }

    void end() {

        System.out.println(name + "(이)가 퇴근했습니다");
    }
    // 직무 마다 다른 기능
    abstract void work(); // 추상 메서드: 내용 구현 X
    // 미완성, 자식이 반드시 완성
    // 기능을 작성하고 싶지만 너무 많은 내용으로 인해 부모 클래스에서 작성 힘듦
}

class Devel extends Company {

    Devel(String name) {

        super(name);
    }

    @Override
    void work() {

        System.out.println(name + "님이 프로그램을 개발합니다.");
    }
}

class Designer extends Company {

    Designer(String name) {

        super(name);
    }

    @Override
    void work() {

        System.out.println(name + "님이 디자인합니다.");
    }
}

class Planner extends Company {

    Planner(String name) {

        super(name);
    }

    @Override
    void work() {

        System.out.println(name + "님이 기획합니다.");
    }
}

public class AbstractMain {

    static void main() {

        Company c1 = new Devel("이말년");
        Company c2 = new Designer("조석");
        Company c3 = new Planner("제임스");

        c1.start();
        c1.work();
        c1.end();
        System.out.println();
        c2.start();
        c2.work();
        c2.end();
        System.out.println();
        c3.start();
        c3.work();
        c3.end();
    }
}
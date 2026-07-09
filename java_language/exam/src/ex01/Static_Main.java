package ex01;

class Bank {

    String owner;
    int balance;

    static int count = 0;
    // 생성자
    Bank(String owner, int balance) {

        this.owner = owner;
        this.balance = balance;
        count++; // 객체 관계 없이 공동으로 사용
    }
    // 일반 메서드
    void show() {

        System.out.println(owner + " 잔액: " + balance);
        System.out.println();
    }

    static void show_count() {

        System.out.println("계좌 수: " + Bank.count);
    }
}

public class Static_Main {

    public static void main(String[] args) {

        Bank b1 = new Bank("홍길동", 100000);
        Bank b2 = new Bank("권율", 3000000);

        b1.balance += 5000;
        b2.balance += 10000;

        b1.show();
        b2.show();

        Bank.show_count();
    }
}

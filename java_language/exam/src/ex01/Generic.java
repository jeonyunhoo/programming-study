package ex01;

// 제너릭(Generic): 자료형을 미리 정하지 않고 사용할 대 정하게 하는 방식,
//                하나의 클래스를 여러 자료형에 재사용 할 수 있게 해 주는 문법
//                보통 <> 기호를 사용

class Box<T> {

    private T data;

    public void setData(T data) {

        this.data = data;
    }

    public T getData() {

        return data;
    }
}

public class Generic {

    public static void main(String[] args) { // 메인 메서드(시작)

        Box<String> nameBox = new Box<>();
        nameBox.setData("Marcin");

        Box<Integer> scoreBox = new Box<>();
        scoreBox.setData(100);

        Box<Double> doubleBox = new Box<>();
        doubleBox.setData(187.6);

        Box<Boolean> passBox = new Box<>();
        passBox.setData(true);

        printBox(nameBox);
        printBox(scoreBox);
        printBox(doubleBox);
        printBox(passBox);
    }
    //보조 메서드는 메인 메서드 안에 넣으면 안됨
    public static <T> void printBox(Box<T> box) { //보조 메서드

        System.out.println(box.getData());
    }
} //메인 메서드(끝)

//<래퍼클래스>
//래퍼 클래스는 int, double, boolean 같은 기본형 값을 객체처럼 사용할 수 있게 감싸 주는 클래스
//ArrayList 같은 컬렉션에는 기본형 자료형을 직접 넣을 수 없기 때문이다
//ArrayList는 객체를 담는 상자
// 래퍼 클래스는 메서드를 사용할 수 있다
//기본형과 래퍼 클래스
//기본형   래퍼 클래스
//byte           Byte
//short     Short
//int           Integer
//long           Long
//float           Float
//double   Double
//char           Character
//boolean   Boolean
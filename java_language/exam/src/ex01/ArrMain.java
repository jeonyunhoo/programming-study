package ex01;

import java.util.ArrayList;

public class ArrMain {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("홍길동"); // 추가
        names.add("김철수");
        names.add("이영희");

        System.out.println("전체 목록: " + names);
        System.out.println("첫 번째 이름: " + names.get(0)); // 가져오기

        names.set(1, "권율"); //값 변경(위치, 바꿀 값)

        System.out.println("변경 후: " + names);
        names.remove(2); // 값 삭제

        System.out.println("삭제 후: " + names);
        System.out.println("저장된 개수: " + names.size()); // 개수
    }
}

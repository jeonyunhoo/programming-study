package ex01;

class Employee { // 부모 = 슈퍼클래스
	
	public int pay() {
		
		return 0; // 급여를 0으로 줌, 반환형이 정수(int)
	}
}

class FullTime extends Employee {
	
	@Override
	public int pay() {
		
		return 5000000;
	}
	
	public void work() {
		
		System.out.println("정규직 직원이 일합니다.");
	}
}



public class Main02 {

	public static void main(String[] args) { // 자식 = 서브클래스
		
		FullTime e1 = new FullTime();
		Employee p1 = new Employee();
		Employee f1 = new FullTime();
		
		System.out.println("부모 메서드: " + p1.pay());
		System.out.println("자식 메서드: " + e1.pay());
		System.out.println("부모 타입, 자식 메서드: " + f1.pay());
		
		e1.work();
		p1.work();
		f1.work();
	}
}

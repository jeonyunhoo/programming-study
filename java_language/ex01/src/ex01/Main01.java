package ex01;

class Product {
	
	private String name;
	private int price;
	
	public String getname() {
		
		return name;
	}
	
	public int getprice() {
		
		return price;
	}
	
	public void setname(String name) {
		
		this.name = name;
	}
	
	public void setprice(int price) {
		
		this.price = price;
	}
}

public class Main01 {

	public static void main(String[] args) {
		
		Product p = new Product();
		p.setname("키보드");
		p.setprice(30000);
		
		p.setprice(35000);
		
		System.out.println("상품명: " + p.getname());
		System.out.println("가격: " + p.getprice());
	}
}





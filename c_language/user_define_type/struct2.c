// 포인터를 통한 구조체 참조
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

struct student {

	int number;
	char name[20];
	double grade;
};

int main(void) {

	struct student s = { 1,  "홍길동",  4.3 };   //구조체 변수
	struct student* p;  //구조체를 가리키는 포인터

	p = &s;  // 구조체 주소를 p 포인터가 기억

	printf("학번=%d 이름=%s 학점=%f \n", s.number, s.name, s.grade);
	printf("학번=%d 이름=%s 학점=%f \n", (*p).number, (*p).name, (*p).grade); //p가 가리키는 구조체 변수의 멤버
	printf("학번=%d 이름=%s 학점=%f \n", p->number, p->name, p->grade); // -> 연산자는 구조체  포인터로 구조체 멤버 참조

	return 0;
}
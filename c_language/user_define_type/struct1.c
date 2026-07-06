#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 구조체: 다른 자료형들을 모아둔 것
struct student {

	int number;
	char name[10];
	double grade;
};

int main() {

	struct student s;

	printf("학번을 입력하세요: ");
	scanf("%d", &s.number);

	printf("이름을 입력하세요: ");
	scanf("%s", s.name);

	printf("학점을 입력하세요: ");
	scanf("%lf", &s.grade);

	printf("학번: %d\n", s.number);
	printf("학번: %s\n", s.name);
	printf("학번: %.2f\n", s.grade);

	return 0; // 정상 종료
	// return 1; 비정상 종료
}
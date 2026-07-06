#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

#define STU_NUMBER 1
#define REG_NUMBER 2

struct  student { //구조체 : 3개의 멤버
    int type;

    union {  //공용체 :  여러 멤버가 같은 메모리 공간을 함께 사용, 둘 중 하나만 사용하는 구조
        int stu_number;      // 학번
        char reg_number[15];     // 주민등록번호
    } id; //공용체 변수이름은 id

    char name[20];
};

void print(struct student s)
{
    switch (s.type)
    {
    case STU_NUMBER:
        printf("학번: %d\n", s.id.stu_number);
        printf("이름: %s\n", s.name);
        break;
    case REG_NUMBER:
        printf("주민등록번호: %s\n", s.id.reg_number);
        printf("이름: %s\n", s.name);
        break;
    default:
        printf("타입오류\n");
        break;
    }
}

int main(void)
{
    struct student s1, s2;   //구조체 변수

    s1.type = STU_NUMBER;
    s1.id.stu_number = 1;
    strcpy(s1.name, "홍길동"); //문자열 배열에는 =로 직접 대입할 수 없기 때문에 strcpy()를 사용

    s2.type = REG_NUMBER;
    strcpy(s2.id.reg_number, "990101-1056076");
    strcpy(s2.name, "김철수");

    print(s1);
    print(s2);

    return 0;
}
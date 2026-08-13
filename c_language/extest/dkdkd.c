#include <stdio.h>

int main() {


    int sales[5] = { 8,15,12,5,20 };

    int sum = 0; // 전체 판매 수량 변수
    int count = 0; // 10개 이상 판매 상품 수 변수
    int susu = 0; // 최고 판매 상품 번호
    int max = sales[0]; // 최고 판매수량 구하기 위한 변수
    int miman = 0; // 평균 미만 상품 수 구하기 위한 변수


    for (int i = 0; i < 5;i++)
    {

        // 전체 판매 수량
        sum += sales[i];

        // 10개 이상 판매 상품 수
        if (sales[i] >= 10) {
            count += 1;
        }

        // 최고 판매 수량
        if (sales[i] > max) {
            max = sales[i];
            susu = i;
        }


    }

    printf("전체 판매수량 : %d\n", sum);

    // 배열 길이 구하기
    float length = sizeof(sales) / sizeof(sales[0]);

    // 평균 판매 수량
    float divi = (float)sum / length;

    printf("평균 판매 수량 : %.1f\n", divi);

    printf("10개 이상 판매 상품 수 : %d\n", count);

    printf("최고 판매 수량 : %d\n", max);

    printf("최고 판매 상품 번호 : %d\n", susu + 1);

    for (int i = 0; i < 5; i++) {
        // 평균 미만 상품 수
        if (sales[i] < divi) {
            miman += 1;
        }
    }

    printf("평균 미만 상품 수 : %d\n", miman);


}
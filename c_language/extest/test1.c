#include <stdio.h>

int main() {

	int sales[5] = {8, 15, 12, 5, 20};
	int length = sizeof(sales[5]);

	int sum = 0;
	int max_sale = 0;
	int less_aver = 0;
	int above_aver = 0;
	int max_s = 0;
	int max_index = 0;

	double average = 0.0;

	for (int i = 0; i <= length; i++) { // sales의 처음부터 끝까지의 값을 하나씩 확인

		sum += sales[i]; // 모든 판매 개수 합산

		if (sales[i] >= 10) { // sales[i]가 10 이상일 때

			above_aver++;
		}

		if (sales[i] > max_s) { // 최고 판매 수량

			max_s = sales[i];
			max_index = i + 1;
		}
	}

	average = sum / 5; // 평균값

	for (int i = 0; i <= length; i++) {

		if (sales[i] < average) { // sales[i]가 average 이하일 때

			less_aver++;
		}
	}

	printf("전체 판매 수량: %d\n", sum);
	printf("평균 판매 수량: %.1f\n", average);
	printf("10 이상 판매 수: %d\n", above_aver);
	printf("최고 판매 수량: %d\n", max_s);
	printf("최다 판매 물품 번호: %d\n", max_index);
	printf("평균 이하 판매 수량: %d\n", less_aver);

	return 0;
}
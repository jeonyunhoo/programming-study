#include <stdio.h>

int main() {

	int sum = 0;
	int amount_ten = 0;
	int max = 0;
	int max_index = 0;
	int less_count = 0;

	double average = 0;

	int sales[5] = { 8, 15, 12, 5, 20 };
	int length = sizeof(sales) / sizeof(sales[0]);

	int less = sales[0];
	int less_index = 1;

	for (int i = 0; i < length; i++) {

		sum += sales[i];

		if (sales[i] >= 10) {

			amount_ten += 1;
		}

		if (sales[i] > max) {

			max = sales[i];
			max_index = i + 1;
		}

		if (sales[i] < less) {

			less = sales[i];
			less_index = i + 1;
		}
	}

	average = sum / 5.0;

	for (int i = 0; i <= length; i++) {

		if (sales[i] < average) {

			less_count += 1;
		}
	}

	printf("전체 판매 수량: %d\n", sum);
	printf("평균 판매 수량: %.1f\n", average);
	printf("10 이상 판매 상품 수: %d\n", amount_ten);
	printf("최다 판매 수량: %d\n", max);
	printf("최다 판매 상품 번호: %d\n", max_index);
	printf("평균 미만 판매 상품 수: %d\n", less_count);
	printf("최저 판매 수량: %d\n", less);
	printf("최저 판매 상품 번호: %d\n", less_index);

	return 0;
}
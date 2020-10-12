#include <stdio.h>

void InsertionSort(int A[], int n) {
	int i, j, value;

	printf("0 단계 \t");
	for (int k = 0; k <= n; k++)
		printf("%d \t", A[k]);
	printf("\n");

	for (i = 2; i <= n; i++) {
		value = A[i];
		j = i;
		while (A[j - 1] > value) {
			A[j] = A[j - 1];
			j--;
		}
		A[j] = value;

		printf("%d 단계 \t", i - 1);
		for (int k = 0; k <= n; k++)
			printf("%d \t", A[k]);
		printf("\n");

	}
}

int main() {
	int A[] = {-1, 30, 20, 40, 10, 5, 10, 30, 15 };
	int n = sizeof(A) / sizeof(int) - 1;

	InsertionSort(A, n);

}
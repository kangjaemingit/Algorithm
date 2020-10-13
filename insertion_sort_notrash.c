#include <stdio.h>

void InsertionSort(int A[], int n) {
	int i, j, value;

	printf("0 단계 \t");
	for (int k = 0; k < n; k++)
		printf("%d \t", A[k]);
	printf("\n");

	for (i = 1; i < n; i++) {
		value = A[i];
		j = i;
		while (j > 0 && A[j - 1] > value) {
			A[j] = A[j - 1];
			j--;
		}
		A[j] = value;
		
		printf("%d 단계 \t", i);
		for (int k = 0; k < n; k++)
			printf("%d \t", A[k]);
		printf("\n");

	}
}

int main() {
	int A[] = {30, 20, 40, 10, 5, 10, 30, 15 };
	int n = sizeof(A) / sizeof(int);

	InsertionSort(A, n);

}
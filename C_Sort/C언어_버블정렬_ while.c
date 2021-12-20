#include <stdio.h>

void swap(int A[], int a, int b) {
	int temp;
	temp = A[a];
	A[a] = A[b];
	A[b] = temp;
}

void BubbleSort(int A[], int n) {
	int sorted = 0;
	int level = 0;

	while (!sorted) {
		printf("%d 단계 \t", level);
		for (int i = 0; i < n; i++)
			printf("%d \t", A[i]);
		printf("\n");

		sorted = 1;

		for (int i = 1; i < n - level; i++) {
			if (A[i - 1] > A[i]) {
				swap(A, i - 1, i);
				sorted = 0;
			}
		}

		level++;
	}

	printf("%d 단계 \t", level);
	for (int i = 0; i < n; i++)
		printf("%d \t", A[i]);


}

int main() {
	int arr[] = { 8,7,6,5,4,3,2,1 };
	int n = sizeof(arr) / sizeof(int);

	BubbleSort(arr, n);
	printf("%d", n);
}
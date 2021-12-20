#include <stdio.h>

void swap(int A[], int a, int b) {
	int temp;
	temp = A[a];
	A[a] = A[b];
	A[b] = temp;
}

void BubbleSort(int A[], int n) {
	int sorted = 0;
	int k;

	for(k = 0; k < n; k++) {
		printf("%d ´Ü°è \t", k);
		for (int i = 0; i < n; i++)
			printf("%d \t", A[i]);
		printf("\n");

		if (sorted)
			break;

		sorted = 1;

		for (int i = 1; i < n - k; i++) {
			if (A[i - 1] > A[i]) {
				swap(A, i - 1, i);
				sorted = 0;
			}
		}

	}

}

int main() {
	int arr[] = { 8,7,6,5,4,3,2,1 };
	int n = 8;

	BubbleSort(arr, n);

}
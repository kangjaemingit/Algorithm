#include<stdio.h>

void SelectionSort(int A[], int n) {
	int i, j, MinIndex;

	for (i = 0; i < n-1; i++) {
		MinIndex = i;
		
		// �迭 ���
		printf("%d �ܰ�", i);
		for (int k = 0; k < n; k++) 
		{
			printf("\t %d", A[k]);
		}
			
		// �ּҰ� index ã��
		for (j = MinIndex + 1; j < n; j++) 
		{
			if (A[MinIndex] > A[j])
				MinIndex = j;
		}

		// �ڸ�����
		if (MinIndex != i) 
		{

		}

		printf("\n");
	}

	// ���� �迭 ���(���� ��)
	printf("%d �ܰ�", i);
	for (int k = 0; k < n; k++)
		printf("\t %d", A[k]);
}

int main() {
	int A[] = { 30, 20, 40, 10, 5, 10, 30, 15 };
	int B[2][8] = { {0,1,2,3,4,5,6,7}, {30, 20, 40, 10, 5, 10, 30, 15} };
	//SelectionSort(A, 8);


	// Stable�� �������� �����ϱ�
	int i, j, MinIndex;
	int n = 8;

	for (i = 0; i < n - 1; i++)
	{
		MinIndex = i;

		printf("%d �ܰ� \n", i);
		for (int k = 0; k < 2; k++)
		{
			for (int l = 0; l < n; l++)
			{
				printf("\t %d", B[k][l]);
			}
			printf("\n");
		}

		for (j = MinIndex + 1; j < n; j++)
		{
			if (B[1][MinIndex] == B[1][j])
			{
				if (B[0][MinIndex] > B[0][j])
				{
					MinIndex = j;
				}
			}
			else if (B[1][MinIndex] > B[1][j])
				MinIndex = j;
		}

		if (MinIndex != i) {
			for (int x = 0; x < 2; x++) {
				int temp = B[x][i];
				B[x][i] = B[x][MinIndex];
				B[x][MinIndex] = temp;
			}
		}

		printf("\n\n");

	}

	printf("%d �ܰ� \n", i);
	for (int k = 0; k < 2; k++)
	{
		for (int l = 0; l < n; l++)
		{
			printf("\t %d", B[k][l]);
		}
		printf("\n");
	}

}
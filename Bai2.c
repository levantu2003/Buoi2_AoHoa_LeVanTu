#include <stdio.h>
#include <math.h>

//Hàm kiểm tra số chính phương
int kiemTraSoChinhPhuong(int num) {
    int sqrtNum = (int)sqrt(num);
    return (sqrtNum * sqrtNum == num);
}

//Hàm đếm và in các số chính phương nhỏ hơn n
int demVaInSoChinhPhuong(int n) {
    int count = 0;
    printf("Các số chính phương nhỏ hơn %d: \n", n);
    for(int i = 1; i < n; i++) {
        if(kiemTraSoChinhPhuong(i)){
            printf("%d ", i);
            count++:
        }
    }
    printf("\n");
    return count;
}

int main(){
    int n;
    printf("Nhập một số nguyên n: ");
    scanf("%d", &n);

    int count = demVaInSoChinhPhuong(n);
    printf("Có %d số chính phương nhỏ hơn %d. \n", count, n);
    return 0;
}
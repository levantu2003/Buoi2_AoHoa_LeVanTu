#include <stdio.h>

void xuatHaiChuSoBoiBay(){
    int i;
    printf("Các số nguyên có 2 chữ số và là bội của 7:\n");
    for(i = 10; i < 100; i++) {
        if(i % 7 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    xuatHaiChuSoBoiBay();
    return 0;
}
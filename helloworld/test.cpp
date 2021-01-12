#include <iostream>
#include<cmath>
using namespace std;

//输入参数的方式为地址，可读性较差
int solution(double a, double b, double c, double &x1, double &x2, int &i, float &fl){
    double d;
    d = b*b-4*a*c;
    if (d>0){
        x1 = (-b+sqrt(d))/(2*a);
        x2 = (-b-sqrt(d))/(2*a);
        return 2;    
    }
    else if (d==0){
        x1 = (-b)/(2*a);
        return 1;
    } 
    else
    {
        return 0;
    }
    
}

int main(){
    double x1, x2;
    int i;
    float fl;
    int sum = solution(1, 4, 5, x1, x2, i, fl);
    printf("sum is %d\n", sum);
    printf("x1 ,x2 is %f, %f\n", x1, x2);
    printf("i ,f is %d, %f\n", i, fl);
    return 0;
}
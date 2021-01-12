#include<stdio.h>
#include<time.h>

int main(){
	time_t t;        //声明time_t类型变量
    struct tm *start_time, *end_time;  //tm结构指针
    
	time (&t);//获取时间戳。  
    start_time = localtime (&t);//转为时间结构。  
    printf ( "%d\n", start_time);
//    printf ( "%d/%d/%d %d:%d:%d\n",lt->tm_year+1900, lt->tm_mon, lt->tm_mday, lt->tm_hour, lt->tm_min, lt->tm_sec);//输出结果  	

	int length = 99999;
	int evens[length/2];
	int j = 0, i;

	for(i=0;i<=length;i++){
		if (i % 2 == 0){
			evens[j] = i;
			j += 1;
		}
	}
	
	time (&t);
	end_time = localtime (&t);
	printf ( "%d\n", end_time);
	
	// for(i=0;i<=length/2;i++){
	// 	printf("%d ", evens[i]);
	// 	if(i % 10 == 0){
	// 		printf("\n");
	// 	}	
	// }
	
	printf("%d", end_time - start_time);
		
	return 0;
} 
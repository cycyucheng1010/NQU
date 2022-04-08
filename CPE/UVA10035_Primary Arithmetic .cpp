#include<iostream>
int divide(int n ,int arr[],int &count){
	for(count=0;n!=0;count++){
		arr[count]=n%10;
		n=n/10;
	}
	
}
using namespace std;
int main(void){
	int a,b;
	while(cin>>a>>b && (a!=0 || b!=0)){
		int alen,blen;
		int arra[11] = {},arrb[11]={};
		int sum[12]={};
		divide(a,arra,alen);
		divide(b,arrb,blen);
		int len = max(alen,blen);
		int ans=0;
		for(int i =0;i<len;++i){
			sum[i]+=(arra[i]+arrb[i]);
			if(sum[i]>=10){
				sum[i]=sum[i]-10;
				sum[i+1]++;
				++ans;
			}
			
		}
		if(ans==0){
		cout<<"No carry operation."<<endl;
		}
		else if(ans==1){
		cout<<"1 carry operation."<<endl;
		}
		else{
		cout<<ans<<" carry operations."<<endl;
		}
	}
	
	return 0;
}

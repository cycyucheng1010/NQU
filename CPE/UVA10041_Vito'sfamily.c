#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> num;
int main(void){
	int n,r,s;
	
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>r;
		num.clear();
		for(int j=0;j<r;j++){
			cin>>s;
			num.push_back(s);
		}
		sort(num.begin(),num.end());
		int mid=num[r/2];
		int sum =0;
		for(int k=0;k<r;k++){
			sum =sum + abs(num[k]-mid);
		}
		cout<<sum<<endl;
	}

	return 0;
}


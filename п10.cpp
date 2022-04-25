#include <iostream>
using namespace std;
int Denis(int rev);
int main()
{
int user,a,rev;
int size = 4;
int kek[4];
int b = 0;
cin>>user;

while(user>0){
a=user%10;
rev=rev*10+a;
user=user/10;
}
cout<<rev<<endl;
cout<< "rev^2 = " << Denis(rev) << endl;
cout << "rev^4 = "<< Denis(rev)*Denis(rev)<<endl;
		 // changed maks 

int sum = 0;
//shoh
for (int i=0; i<size;i++){
	cout<<"Add number"<<endl;
	cin>>kek[i];
}
for (int i=0; i<size;i++){ 
  
   sum+=kek[i];
   b=sum/size;
    cout<<sum<<endl;
  }
 return 0;
}
  
int Denis(int rev) {
	
	return rev*rev;
}

// Online C++ compiler to run C++ program online
#include <iostream>
#include<string>
using namespace std;

int main() {
    // Write C++ code here
    string s;

    cin>>s;
     int n=s.size();
    int shifts[n];
    for(int i=0;i<n;i++){
        cin>>shifts[i];
    }
    for(int i =0;i<3;i++){
        for(int j=0;j<=i;j++){
            int a = int(s[j]);
            a=a+shifts[i];
            if(a>122){
                a=(a%122)+96;
            }
            s[j] = char(a);
        }

    }
    cout<<s;
    return 0;
}

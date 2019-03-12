#include<bits/stdc++.h>

using namespace std; 

long long fun(long long n, long long int* arr)
{
    if(n == 1 || n == 0)
        return n ;
    if(arr[n] != 0)
        return arr[n] ;
    else
    {
        arr[n] = max(n, fun(n/2, arr)+fun(n/3, arr)+fun(n/4, arr));
        return arr[n];
    }
}

int main(int argc, char const *argv[])
{
    long long x;
    while(cin >> x)
    {
        long long *arr = new long long[x+1];
        cout << fun(x, arr) << endl ;
    }
    return 0;
}

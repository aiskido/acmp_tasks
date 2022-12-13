#include <iostream>

using namespace std;

int main()
{
    int n, m, x, y;
    cin >> n >> m >> x >> y;
    int arr[n][m];
    int temp = -1;
    for(int i=0; i<n; i++){
        if(i%2==0){
            for(int j=0; j<m; j++){
                temp++;
                arr[i][j] = temp;
            }
            temp+=m;
        }
        else{
            for(int j=0; j<m; j++){
                arr[i][j] = temp;
                temp--;
            }
            temp+=m;
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    cout << "The needed number is: " << arr[x-1][y-1];
    return 0;
}

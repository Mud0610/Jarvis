#include <iostream>
using namespace std;
  

void printTwoElements(int arr[], int n)
{
    int temp[n] = {}; // Creating temp array of size n with
                      // initial values as 0.
    int repeatingNumber=-1;
    int missingNumber=-1;
    
    for (int i = 0; i < n; i++) {
        cout<< arr[i-1];
        temp[arr[i]-1]++;
        if (temp[arr[i] - 1] > 1) {
            repeatingNumber = arr[i];
        }
    }
    for (int i = 0; i < n; i++) {
        cout<< temp[i];
        if (temp[i] == 0) {
            missingNumber = i + 1;
            break;
        }
    }
    
    cout << "The repeating number is " << repeatingNumber<<"."
         << endl;
    cout << "The missing number is " << missingNumber<<"."
         << endl;
    
}
  
int main()
{
  
    int arr[] = { 7, 3, 4, 5, 5, 6, 2 };
    int n = sizeof(arr) / sizeof(arr[0]);
    printTwoElements(arr, n);
    return 0;
}
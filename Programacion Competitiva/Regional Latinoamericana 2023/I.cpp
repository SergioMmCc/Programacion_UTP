#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define m 1000000007

using namespace std;

int main () {
    long long int rightFrequencies[30], leftFrequencies[30], left = 0, right = 0, saveLetter, length, result, n;
    string word;
    
    memset (rightFrequencies, 0, sizeof rightFrequencies);
    memset (leftFrequencies, 0, sizeof leftFrequencies);
    cin >> word;
    cin >> n;
    length = word.size () - 1;
    
    for (int letterIndex = 0; letterIndex <= length; letterIndex++) {
        saveLetter = (int)word[letterIndex] - 96;
        for (int frequencyIndex = saveLetter; frequencyIndex < 26; frequencyIndex++)
            leftFrequencies[frequencyIndex]++;
        
        left += leftFrequencies[saveLetter - 1];
    }
    
    for (int letterIndex = length; letterIndex >= 0; letterIndex--) {
        saveLetter = (int)word[letterIndex] - 96;
        for (int frequencyIndex = saveLetter; frequencyIndex < 26; frequencyIndex++)
            rightFrequencies[frequencyIndex]++;
        
        right += rightFrequencies[saveLetter - 1];
    }
    
    cout << right << "\n";
    cout << left << "\n";
    
    if (n % 2 == 0) 
        result = (((n/2)%m) * (((right*(n+1)) + (left*(n-1)))%m)) % m;
    
    else
        result = ((n%m) * ((((right*(n+1)) + (left*(n-1)))/2)%m)) % m;

    cout << result << "\n799008402\n";

    return 0;
}


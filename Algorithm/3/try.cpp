#include<iostream>
using namespace std;

int main(){
    int n,N;
    string command;
    string com_list[N];

    cin >> N;

    for (int num = 0; num < N; num++)
    {
        cin >> command >> n;
        

        if (command == "delete")
        {
            for (int k; k < N; k++)
            {
                if (com_list[k] == "insert" + to_string(n))
                {
                    com_list[num] = "pass";
                }
            }
        }
        else
        {
            com_list[num] = command + to_string(n);
        }
    }

    for (int i = 0; i < N-1; i++)
    {
        cout << com_list[i] << " ";
    }
    
    cout << com_list[N-1] << endl;

    return 0;
}
#include <iostream>
using namespace std;

int main(){
    int  N, n, list[100], i;
    cin >> N;//命令数
    string command;

    /*for (int num = 0; num < N; num++)
    {
        cin >> command >> n;
        string com_list[N];
        string pass;
        
        if (command == "delete" + n){
            for (int k; k<N; k++){
                if (com_list[k] == "insert" + n){
                    com_list[k] = pass;
                }
            }
        }else{
            com_list[num] = command;
        }
    }*/

    for (i = 0; i < N; i++)
    {
        cin >> command >> n;
        if (command == "insert")
        {
            //insert n の処理
            list[i] = n;
        }
        else if (command == "delete")
        {
            //delete n　の処理
        }
        else if (command == "deleteFirst")
        {

        }
        else
        {
            //daleteLastの処理
        }
    }

    for (i = 0; i < N - 1; i++)
    {
        cout << list[i] << " ";
    }

    cout << list[N - 1] << endl;

    return 0;
    }
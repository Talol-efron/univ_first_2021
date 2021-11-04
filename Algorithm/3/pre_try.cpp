#include<iostream>
using namespace std;

struct Node
{
    int key;
    Node *prev, *next;
};

int main(){
    Node *x = (Node *)malloc(sizeof(Node));
    cout << x;
    return 0;
}
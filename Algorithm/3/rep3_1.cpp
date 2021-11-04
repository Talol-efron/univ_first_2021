#include <cstdio>
#include <cstdlib>
#include <cstring>
struct Node{
    int key;
    Node *prev, *next;
};

Node *nill;

void init(){
    nill = (Node *)malloc(sizeof(Node));
    nill ->next = nill;
    nill ->prev = nill;
}

void insert(int key) {
    Node *x = (Node *)malloc(sizeof(Node));
    x -> key = key;
    //番兵の直後に要素を追加
    x ->next = nill ->next;
    nill->next->prev = x; //初回はnill->prevをNodeにつなぐ
    nill ->next = x;
    x->prev = nill;
}

Node* listSearch(int key){
    Node *cur = nill->next; //番兵の次の要素から探る
    while (cur != nill && cur ->key != key)
    {
        cur = cur->next;
    }
    return cur;
}

void deleteNode(Node *t) {
    if (t == nill)
    {
        return;
    }
    t->prev->next = t->next;
    t->next->prev = t->prev;
    free(t);
}

void deleteFirst(){
    deleteNode(nill->next);
}

void deleteLast(){
    deleteNode(nill->prev);
}

void deleteKey(int key){
    //検索したNodeを削除
    deleteNode(listSearch(key));
}

void printList(){
    Node *cur = nill->next;
    int isf = 0;
    while (1)
    {
        if (cur == nill)
            break;
        if (isf++ > 0)
            printf(" ");
        printf("%d", cur->key);
        cur = cur->next;
    }
    printf("\n");
}

int main(){
    int key, n, i;
    int size = 0;
    char com[20];
    int np = 0, nd = 0;
    scanf("%d", &n);
    init();
    for (i=0; i<n; i++){
        scanf("%s%d", com, &key);
        if(com[0] == 'i'){
            insert(key);
            np++;
            size++;
        }else if(com[0] == 'd'){
            if (strlen(com) > 6)
            {
                if (com[6] == 'F')
                {
                    deleteFirst();
                }else if(com[6] == 'L'){
                    deleteLast();
                }   
            }else{
                deleteKey(key);
                nd++;
            }
            size--;
        }
    }
    printList();
    return 0;
}
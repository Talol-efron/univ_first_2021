#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const int MAX_WORDS = 100000;

typedef struct
{
    int count;
    char word[256];
} WordCount;

static WordCount* words[MAX_WORDS];
static int num_words = 0;

void count_word(char* word)
{
    if(word == NULL)
        return;
    
    int found = 0;
    for(int i=0; i<num_words; ++i) {
        if(strcmp(words[i]->word, word) == 0) {
            words[i]->count++;
            found = 1;
            break;
        }
    }
    
    if(found == 0) {
        WordCount* wc;
        
        wc = (WordCount*)malloc(sizeof(WordCount));
        strcpy(wc->word, word);
        wc->count ++;
        
        words[num_words] = wc;
        
        num_words ++;
    }
}

int main(int argc, char** argv)
{
    FILE* f = fopen("dracula.txt", "r");
    
    //counting 
    char line[1024*16];
    while(fgets(line, sizeof(line), f))
    {
        line[strlen(line)-1] = 0;
        char *p = strtok(line, " \n");

        count_word(p);
        while((p = strtok(NULL, " \n"))) {
            count_word(p);
        }
    }
    
    printf("The number of words = %d\n", num_words);
    
    //bubble sort
    for(int i=0; i<num_words-1; ++i) {
        for(int j=num_words-1; j>i; --j) {
            if(words[j-1]->count < words[j]->count) {
                WordCount* temp = words[j];
                words[j] = words[j-1];
                words[j-1] = temp;
            }
        }
    }
    
    
    for(int i=0; i<20; ++i) {
        WordCount* wc = words[i];
        
        printf("%s %d\n", wc->word, wc->count);
    }
}

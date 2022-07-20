// Implements a dictionary's functionality
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"

// Linked list that contain a nodes, where every node has a value and a pointer to the next node(which is a caracter array and a pointer to the address of the next word in this linked list)
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;
// difining constant integer to be equal to any- and a node table that is going to represent our hash table which is an array of node pointers where evey element of that array is a pointer to a node.
const unsigned int N = 100000;
// Hash table
node *table[N];
int dict_size = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // f open function to open up the dictionary file
    FILE *dict_pointer = fopen(dictionary, "r");
    // Check if null
    if (dictionary == NULL)
    {
        printf("Unable to open %s\n", dictionary);
        return false;
    }
    // Initialise word array
    char next_word[LENGTH + 1];
    // fscanf which is represent scaning from a file(file pointer, %s meaning you want to read from a string,some caracter array which is a place that you want to read your word into) and when fscanf return EOF, it means you reached the end of the file
    while (fscanf(dict_pointer, "%s", next_word) != EOF)
    {
        // ask for some memory from the computer equal to the size of node , the number of byte of memory i need in order to store a node and the address of that node is going to be inside of n
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        // string copy which is going to copy a string from a source into a distination, in this case it is going to copy the word "Hello" into the caracter array and arrow worrd
        strcpy(n->word, next_word);
        // hash function will take a string and return as index which is a number that you can index your linked list.
        int hash_value = hash(next_word);
        // Insert node into hash table at that location
        n->next = table[hash_value];
        table[hash_value] = n;
        dict_size++;
    }
    // Close file
    fclose(dict_pointer);
return true;
}

// a hash function going to take a char star represnting the word you going to hash and it will return unsigned integer, an integer that will be negative represntiong which idex into the hash table you should
//use corresponding to that particular word
unsigned int hash(const char *word)
{
    // This hash function adds the ASCII values of all characters
    long sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return sum % N;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return dict_size;
}

// Take a word and check if that word is in the dictionary or not, char* representin a word as an input and the output will be a boolian variable true of false
bool check(const char *word)
{
    // Hash word to obtain hash value
    int hash_value = hash(word);
    // Access linked list at that index in hash table
    node *n = table[hash_value];
    // Traverse linked list, looking for word (strcasecomp) by checking one by one node till meeting the right word
    while (n != NULL)
    {
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }
        n = n->next;
    }
return false;
}

// unload function will call free to release memory that youve allocated using malloc and return true
bool unload(void)
{
    // Iterate over hash table and free nodes in each linked list
    for (int i = 0; i < N; i++)
    {
        // Assign cursor
        node *n = table[i];
        // Loop through linked list
        while (n != NULL)
        {
            // Make temp equal cursor;
            node *tmp = n;
            // Point cursor to next element
            n = n->next;
            // free temp
            free(tmp);
        }
        if (n == NULL && i == N - 1)
        {
            return true;
        }
    }
return false;
}

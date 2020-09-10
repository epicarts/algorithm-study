#include <stdio.h>
#include <stdlib.h>

typedef struct s_node
{
    char data;
    struct s_node *prev;
}   t_node;

typedef struct s_word
{
    t_node *top;
}   t_word;

t_node *create_node(char data)
{
    t_node *new_node;

    new_node = (t_node*) malloc(sizeof(t_node));
    new_node->data = data;
    new_node->prev = NULL;

    return (new_node);
}
t_word *create_word(void)
{
    t_word *new_word;

    new_word = (t_word*) malloc(sizeof(t_word));
    new_word->top = NULL;

    return (new_word);
}
void add_character(t_word **my_word, char c)
{
    t_node *new_node;

    new_node = create_node(c);
    if ((*my_word)->top == NULL)
    {
        (*my_word)->top = new_node;
    }
    else
    {
        new_node->prev = (*my_word)->top;
        (*my_word)->top = new_node;
    }
}

void free_node(t_node *target_node)
{
    target_node->data = 0;
    target_node->prev = NULL;
    free(target_node);
}

void print_word(t_word **my_word)
{
    t_node *current_node;

    while((*my_word)->top != NULL)
    {
        current_node = (*my_word)->top;
        printf("%c",current_node->data);
        (*my_word)->top = current_node->prev;
        free_node(current_node);
    }
}
void print_reverse_word(char *string)
{
    int index;
    t_word *current_word;

    index = 0;
    current_word = create_word();
    while(string[index] != '\0')
    {
        if(string[index] == ' ')
        {
            print_word(&current_word);
            printf(" ");
        }
        else
        {
            add_character(&current_word, string[index]);
        }
        index++;
    }
    if(string[index]=='\0' && current_word != NULL)
        print_word(&current_word);
    printf("\n");
}

void buffer_clear(void)
{
    while(getchar()!='\n');
}

int main (void)
{
    int total_line;
    int index;
    char string[1000];

    index = 0;
    scanf("%d",&total_line);
    buffer_clear();
    while(index < total_line)
    {
        scanf("%[^\n]",string);
        buffer_clear();
        print_reverse_word(string);
        index++;
    }
    return (0);
}



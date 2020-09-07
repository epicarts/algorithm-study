#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct s_node
{
    int data;
    struct s_node *prev;
    struct s_node *next;
}   t_node;        

typedef struct s_list
{
    t_node *head;
    t_node *tail;
    int size;
}   t_list;

int input_number(void)
{
    int number;

    scanf("%d",&number);
    return (number);
}

t_node *create_node(int data)
{
    t_node *new_node;

    new_node = (t_node*) malloc(sizeof(t_node));
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = NULL;
    return (new_node);
}

void list_push(t_list **list, int data)
{
    t_node *new_node;
    t_node *last_node;

    new_node = create_node(data);
    last_node = (*list)->head;
    if (last_node == NULL)
    {
        (*list)->head = new_node;
        (*list)->tail = new_node;
        (*list)->size = 1;
        return;
    }
    // find last node
    while(last_node->next != NULL)
    {
        last_node = last_node->next;
    }
    // append node;
    last_node->next = new_node;
    new_node->prev = last_node;
    (*list)->tail = new_node;
    (*list)->size += 1;
}

void list_empty(t_list *list)
{
    if (list != NULL)
        list->size == 0 ? printf("1\n") : printf("0\n");
}

void free_node(t_node *target_node)
{
    target_node->data = 0;
    target_node->prev = NULL;
    target_node->next = NULL;
    free(target_node);
}

void list_pop(t_list **list)
{
    t_node *last_node;

    last_node = (*list)->tail;
    if ((*list)->head == NULL)
    {
        printf("-1\n");
        return;
    }
    printf("%d\n",last_node->data);
    (*list)->size -= 1;
    if ((*list)->head == (*list)->tail)
    {
        (*list)->head = NULL;
        (*list)->tail = NULL;
    }
    else
    {
        last_node->prev->next = NULL;
        (*list)->tail = last_node->prev;
    }
    free_node(last_node);
}

void input_command(t_list **list)
{
    char command[6];
    int data;
    scanf("%s",command);

    if (strcmp("push", command) == 0)
    {
        scanf("%d",&data);
        list_push(list, data);
    }
    else if(strcmp("pop", command) == 0)
    {
        list_pop(list);
    }
    else if(strcmp("size", command) == 0)
    {
        printf("%d\n",(*list)->size);
    }
    else if(strcmp("empty", command) == 0)
    {
        list_empty(*list);
    }
    else if(strcmp("top", command) == 0)
    {
        ((*list)->tail == NULL) ? printf("-1\n") : printf("%d\n",(*list)->tail->data);
    }
}

int main(void)
{
    int total_number;
    int index;
    t_list *list;

    // initialize list
    list = (t_list*) malloc(sizeof(t_list));
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;

    total_number = input_number();
    index = 0;
    while(index < total_number)
    {
        input_command(&list);
        index++;
    }
    return (0);
}

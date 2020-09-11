#include <stdio.h>
#include <stdlib.h>

typedef struct s_operation
{
    char sign;
    struct s_operation *next;
}   t_operation;

typedef struct s_operation_record
{
    t_operation *head;
    t_operation *tail;
}   t_operation_record;

typedef struct s_stack_node
{
    int data;
    struct s_stack_node *prev;
}   t_stack_node;

typedef struct s_stack
{
    t_stack_node *top;
}   t_stack;

int *create_array(int size, int type)
{
    int *new_array;
    int index;

    index = 0;
    new_array = (int*) malloc(sizeof(int)*size);
    while(index < size)
    {
        (type == 0) ? (new_array[index] = 0) : (new_array[index] = index + 1);
        index++;
    }

    return (new_array);
}

t_operation *create_operation(void)
{
    t_operation *new;
    
    new = (t_operation*) malloc(sizeof(t_operation));
    new -> next = NULL;
    
    return (new);
}

t_operation_record *create_record(void)
{
    t_operation_record *new;

    new = (t_operation_record*) malloc(sizeof(t_operation_record));
    new -> tail = NULL;

    return (new);
}

t_stack_node *create_stack_node(int data)
{
    t_stack_node *new;

    new = (t_stack_node*) malloc(sizeof(t_stack_node));
    new -> data = data;
    new -> prev = NULL;

    return (new);
}

t_stack *create_stack_list(void)
{
    t_stack *new;
    
    new = (t_stack*) malloc(sizeof(t_stack));
    new -> top = NULL;

    return (new);
}

void buffer_clear(void)
{
    while(getchar() != '\n');
}

void push_stack(t_operation_record **my_record, t_stack **my_stack, int data)
{
    t_stack_node *new_stack;
    t_operation *new_operation;

    new_stack = create_stack_node(data);
    new_operation = create_operation();
    new_operation->sign = '+';
    if ((*my_stack)->top == NULL)
    {
        (*my_stack)->top = new_stack;
    }
    else
    {
        new_stack->prev = (*my_stack)->top;
        (*my_stack)->top = new_stack;
    }

    if ((*my_record)->head == NULL)
    {
        (*my_record)->head = new_operation;
        (*my_record)->tail = new_operation;

    }
    else
    {
        (*my_record)->tail->next = new_operation;
        (*my_record)->tail = new_operation;

    }
}

void pop_stack(t_operation_record **my_record, t_stack **my_stack)
{
    t_operation *new_operation;
    t_stack_node *target_node;

    new_operation = create_operation();
    new_operation -> sign = '-';
    
    (*my_record) -> tail -> next = new_operation;
    (*my_record) -> tail = new_operation;
    if ((*my_stack) -> top ->  prev == NULL)
    {
        target_node = (*my_stack) -> top;
        (*my_stack) -> top = NULL;
    }
    else
    {
        target_node = (*my_stack) -> top;
        (*my_stack) -> top = (*my_stack) -> top -> prev;
    }
    target_node -> data = 0;
    target_node -> prev = NULL;
    free(target_node);
}

int check_stack_sequence(t_operation_record **my_record, int *sequence, int size)
{
    int index_seq;
    int index_asc;
    int *ascending;
    t_stack *my_stack;

    index_seq = 0;
    index_asc = 0;
    ascending = create_array(size, 1);
    my_stack = create_stack_list();
    while(index_seq < size )
    {
        if (my_stack -> top == NULL || my_stack -> top -> data < sequence[index_seq])
        {
            push_stack(my_record, &my_stack, ascending[index_asc]);
            printf("+");
                index_asc++;
        }
        if (my_stack -> top != NULL)
        {
            if (my_stack -> top -> data > sequence[index_seq])
            {
                printf("NO\n");
                return (0);
            }
            else if (my_stack -> top -> data == sequence[index_seq])
            {
                pop_stack(my_record, &my_stack);
                printf("-");
                index_seq++;
            }
        }
    }
    printf("\n");
    return (1);
}

void print_record(t_operation_record *my_record)
{
    t_operation *current;

    current = my_record -> head;
    while(current != NULL)
    {
        printf("%c\n",current -> sign);
        current = current->next;
    }
}

int main(void)
{
    t_operation_record *my_record;
    int total_number;
    int index;
    int *sequence;

    index = 0;
    my_record = create_record();
    scanf("%d",&total_number);
    buffer_clear(); 
    sequence = create_array(total_number, 0);
    while(index < total_number)
    {
        scanf("%d",&sequence[index]);
        buffer_clear();
        index++;
    }

    check_stack_sequence(&my_record, sequence, total_number);

    return(0);
}

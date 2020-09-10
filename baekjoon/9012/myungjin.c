#include <stdio.h>
#include <stdlib.h>

typedef struct s_parenthesis
{
    struct s_parenthesis *prev;
}   t_parenthesis;

typedef struct s_stack
{
    t_parenthesis *top;
}   t_stack;

void buffer_clear(void)
{
    while(getchar()!='\n');
}

t_stack *create_stack(void)
{
    t_stack *new_stack;

    new_stack = (t_stack *) malloc(sizeof(t_stack));
    new_stack->top = NULL;

    return(new_stack);
}

t_parenthesis *create_parenthesis(void)
{
    t_parenthesis *new;

    new = (t_parenthesis*) malloc(sizeof(t_parenthesis));
    new -> prev = NULL;

    return new;
}

void add_stack (t_stack **list)
{
    t_parenthesis *new;
    new = create_parenthesis();
    if ((*list) -> top == NULL)
    {
        (*list) -> top = new;
    }
    else
    {
        new -> prev = (*list) -> top;
        (*list) -> top = new;
    }
}

void free_parenthesis(t_parenthesis *target)
{
    target -> prev = NULL;
    free(target);
}

void pop_stack (t_stack **list)
{
    t_parenthesis *current;
    
    current = (*list)->top;
    if ((*list)->top->prev == NULL)
    {
        (*list) -> top = NULL;
    }
    else
    {
        (*list) -> top = current->prev;
    }
    free_parenthesis(current);
}

int is_vaild_vsp(char *string)
{
    t_stack *list;
    int index;

    list = create_stack();
    index = 0;
    
    while(string[index] != '\0')
    {
        if (string[index] == '(')
        {
            add_stack(&list);
        }
        else if (string[index] == ')')
        {
            if (list -> top == NULL)
                return(0);
            pop_stack(&list);
        }
        index++;
    }

    if (list -> top == NULL)
        return(1);
    else
        return(0);
}

int main(void)
{
    int total_line;
    int index;
    char string[50];

    index = 0;
    scanf("%d",&total_line);
    buffer_clear();
    while (index < total_line)
    {
        scanf("%s",string);
        buffer_clear();
        if (is_vaild_vsp(string))
            printf("YES\n");
        else
            printf("NO\n");
        index++;
    }
    
    return (0);
}

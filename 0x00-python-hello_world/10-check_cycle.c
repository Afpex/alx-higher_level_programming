#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: the linked list to be checked
 *
 * Return: 1 if there is a cycle in the linked liste, 0 if none
 */
int check_cycle(listint_t *list)
{
    if (!list)
    {
        return (0);
    }

    listint_t *slow = list;
    listint_t *fast = list;

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
        {
            return (1);
        }
    }

    return (0);
}

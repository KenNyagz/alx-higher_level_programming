#include "lists.h"

/**
*check_cycle - check for a cycle in a linked list
*@list: pointer to head of linked list
*Return: 1 if there is a loop, 0 of no
*/

int check_cycle(listint_t *list)
{
listint_t *fast = list ,*slow = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}
return (0);
}

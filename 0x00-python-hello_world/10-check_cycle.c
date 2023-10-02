#inlcude "lists.h"

/**
*check_cycle - check for a cycle in a linked list
*@list: pointer to head of linked list
*Return: Number of odes before loop
*/

int check_cycle(listint_t *list)
{
listint_t *fast = list, *slow = list;
int count = 0;

	while (fast->head != NULL && fast != NULL)
	{
		fast = list->head->head;
		slow = list->head;
		if (slow == fast)
			return (1);
	}
return (0);
}

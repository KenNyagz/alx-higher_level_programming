#include "lists.h"

/**
*is_palindrome -checks if a singly linked list is a palindrome
*@head: pointer to head of original list
*Return: 0 if not palindrome, 1 if palindrome
*/

int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int *arr, count = 0, i = 0, j = 0;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	if (count <= 1)
		return (1);
	arr = malloc(sizeof(int) * count);
	current = *head;

	while (current != NULL)
	{
		arr[i] = current->n;
		i++;
		current = current->next;
	}

	for (i = 0; i <= count; i++)
		for (j = count; j >= 0; j--)
		{
			if (arr[i] == arr[j])
				continue;
			else
				return (1);
		}

	free(arr);

return (0); /*not palindrome*/
}

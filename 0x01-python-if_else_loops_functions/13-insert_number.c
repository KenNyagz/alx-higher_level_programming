#include "lists.h"

/**
*insert_node - inserts node at specific point on linked list
*@head: pointer to (origina) node to be created
*@number: position where node is to be added
*Return: node at new position
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *ahead = NULL, *behind = NULL, *newnode = NULL;
int count = 0;

ahead = (*head)->next;
behind = *head;
	newnode = malloc(sizeof(listint_t));
	if (head == NULL)
	{
		*head = newnode;
		
	}
	if (newnode == NULL)
		return (NULL);
	while (ahead != NULL && behind != NULL)
	{
		++count;
		ahead = ahead->next;
		behind = behind->next;

		if (count == number)
		{

			*head = ahead;
			behind = *head;
			(*head)->n = number;
		}
	}
free(newnode);
return (behind);
}

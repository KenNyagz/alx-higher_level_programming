#include "lists.h"

/**
*insert_node - inserts node to a listint_t linked list
*@head: pointer to (origina) node to be created
*@number: data to be inserted to new node
*Return:  new node
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = NULL, *newnode = NULL;

current = *head;

newnode = malloc(sizeof(listint_t));
if (newnode == NULL)
	return (NULL);
newnode->n = number;
if (*head == NULL || (*head)->n >= number) /*Insert node at beginning)*/
{
	*head = newnode;
}

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
newnode->next = current->next;
current->next = newnode;


return (newnode);
}

#include "lists.h"
/**
  * insert_node - The function to be built
  * @head: The head of the linked list
  * @number: The data
  * Return: listint_t
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}

	else
	{
		while (ptr->next != NULL && number > ptr->next->n)
		{
			ptr = ptr->next;
		}

		new->next = ptr->next;
		ptr->next = new;
	}

	return (new);
}

#include "lists.h"
/**
  * check_cycle - The function to be built
  * @list: The list to be checked
  * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast->next && fast->next->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		return (1);
	}
	return (0);
}

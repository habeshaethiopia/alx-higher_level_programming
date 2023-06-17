#include "lists.h"
/**
 * check_cycle- function
 * @list: head
 * Return: 0 or 1;
 */
int check_cycle(listint_t *list)
{
	listint_t *h;

	h = list;
	while (list)
	{
		list = list->next;
		if (list == h)
			return (1);
	}
	return (0);
}

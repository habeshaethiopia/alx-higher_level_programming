#include "lists.h"
/**
 * check_cycle- function
 * @list: head
 * Return: 0 or 1;
 */
int check_cycle(listint_t *l)
{
	listint_t *h,*list;

	h = list = l;
	while (h && list && list->next)
	{
		list = list->next->next;
		h = h->next;
		if (list == h)
			return (1);
	}
	return (0);
}

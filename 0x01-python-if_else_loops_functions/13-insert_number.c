#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - function to insert node
 * @head: head of a list
 * @number: the value inserted
 * Return: the header of the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *New;
	listint_t *tmp;

	New = malloc(sizeof(listint_t));
	if (New == NULL)
		return (NULL);
	New->n = number;
	tmp = *head;
	if (tmp == NULL)
		tmp = New;
	else if (tmp->n > number)
	{
		New->next = tmp;
		*head = New;
	}
	else
	{
		while (tmp->next->n < number && tmp->next != NULL)
			tmp = tmp->next;
		if (tmp->next == NULL)
            add_nodeint_end(head, number);
        if (tmp->next->n > number)
        {
			New->next = tmp->next;
			tmp->next = New;
		}
	}
	return (*head);
}

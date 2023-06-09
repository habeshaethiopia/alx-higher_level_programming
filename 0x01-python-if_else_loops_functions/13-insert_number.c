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
    
    tmp = *head;
	New = malloc(sizeof(listint_t));
	if (New == NULL)
		exit(EXIT_FAILURE);
	New->n = number;
    New->next = NULL;
	if (*head == NULL)
	{
        *head = New;
		return (*head);
	}
	
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
            tmp->next = New;
        if (tmp->next->n >= number)
        {
			New->next = tmp->next;
			tmp->next = New;
		}
	}
	return (*head);
}

#include "lists.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * is_palindrome - afunction to check if the linked list is palindrom or not
 *
 * @head: the head of the list
 * Return: int 0 or 1
 *
 */
int is_palindrome(listint_t **head)
{

	listint_t *temp = *head;

	listint_t *ch = Reverse(*head);

	if (temp == NULL || temp->next == NULL)
		return (1);
	while (temp && ch)
	{
		if (temp->n != ch->n)
			return (0);
		temp = temp->next;
		ch = ch->next;
	}
	return (1);
}
/**
 * Reverse - function that returns the reverse of linked list
 *
 * @temp: the list
 * Return: listint_t*
 */

listint_t *Reverse(listint_t *temp)
{
	listint_t *curr = temp, *prev = NULL, *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}

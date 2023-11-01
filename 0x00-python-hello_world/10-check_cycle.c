#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: 0 if not cyclic or 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *nexthead;

	if (list == NULL || list->next == NULL)
		return (0);
	head = list->next;
	nexthead = list->next->next;
	while (nexthead->next && head && nexthead)
	{
		if (head == nexthead)
			return (1);
		head = head->next;
		nexthead = nexthead->next->next;
	}
	return (0);
}

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
	listint_t *current, *next_node;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list->next;
	next_node = list->next->next;
	while (current && next_node && next_node->next)
	{
		if (current == next_node)
			return (1);
		current = current->next;
		next_node = next_node->next->next;
	}
	return (0);
}

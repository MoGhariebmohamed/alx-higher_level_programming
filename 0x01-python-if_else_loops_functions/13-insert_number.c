#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - insert a new node at the location n of a listint_t
 *@head: pointer to pointer of first node of listint_t list
 *@number: integer to be included in new node
 *Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_ins;

	current = *head;
	new_ins = malloc(sizeof(listint_t));
	if (new_ins == NULL)
		return (NULL);
	new_ins->n = number;
	if (current->n >= number || current == NULL)
	{
		new_ins->next = current;
		*head = new_ins;
		return (new_ins);
	}
	while (current && current->next->n < number && current->next)
		current = current->next;

	new_ins->next = current->next;
	current->next = new_ins;
	return (new_ins);
}

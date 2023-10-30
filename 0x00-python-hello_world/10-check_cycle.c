#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle.
 * @list: pointer to the start of the node
 * Return: 1 (Success), else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *present, *outcome;

	if (list == NULL || list->next == NULL)
		return (0);
	present = list;
	outcome = present->next;

	while (present != NULL && outcome->next != NULL
		&& outcome->next->next != NULL)
	{
		if (present == outcome)
			return (1);
		present = present->next;
		outcome = outcome->next->next;
	}
	return (0);
}


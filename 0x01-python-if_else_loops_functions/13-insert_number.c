#include "lists.h"

/**
 * insert_node - inserts number into sorted singly linked list.
 * @head: head of list
 * @number: number to be stored in new node
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *runner_pointer;
        listint_t *new_pointer;

        runner_pointer = *head;

        new_pointer = malloc(sizeof(listint_t));
        if (new_pointer == NULL)
                return (NULL);
        new_pointer->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                new_pointer->next = *head;
                *head = new_pointer;
                return (new_pointer);
        }

        while (runner_pointer->next != NULL)
        {
                if ((runner_pointer->next)->n >= number)
                {
                        new_pointer->next = runner_pointer->next;
                        runner_pointer->next = new_pointer;
                        return (new_pointer);
                }
                runner_pointer = runner_pointer->next;
        }

        new_pointer->next = NULL;
        runner_pointer->next = new_pointer;
        return (new_pointer);
}

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/* Define a singly linked list structure */
struct listint_t {
    int data;
    struct listint_t *next;
};

typedef struct listint_t listint_t;

/* Helper function to reverse a linked list */
listint_t *reverseList(listint_t *head) {
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        return 1;  // An empty list or a single-element list is a palindrome.
    }

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL) {
        // List has an odd number of elements; skip the middle element.
        slow = slow->next;
    }

    second_half = reverseList(slow);
    slow = *head;

    while (second_half != NULL) {
        if (second_half->data != slow->data) {
            is_palindrome = 0;
            break;
        }
        second_half = second_half->next;
        slow = slow->next;
    }

    // Restore the original list by reversing the second half again.
    reverseList(second_half);

    return is_palindrome;
}

// Function to insert a node at the beginning of the list for testing
void insertAtBeginning(listint_t **head, int data) {
    listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
    if (new_node == NULL) {
        fprintf(stderr, "Memory allocation error\n");
        exit(1);
    }
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}

int main() {
    listint_t *head = NULL;
    int values[] = {1, 2, 3, 2, 1};

    for (int i = 0; i < 5; i++) {
        insertAtBeginning(&head, values[i]);
    }

    int result = is_palindrome(&head);
    if (result) {
        printf("The list is a palindrome.\n");
    } else {
        printf("The list is not a palindrome.\n");
    }

    return 0;
}

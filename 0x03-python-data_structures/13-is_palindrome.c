#include "lists.h"
#include <stdlib.h>

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - checks if a linked list is palindrome or not
 * @head: pointer to the head pointer
 *
 * Return: 1 if palindrome
 *	   0 if  not palindrome
 */

int is_palindrome(listint_t **head)
{
	int counter, half, odd_half, count = 0, is_palindrome = 1;
	listint_t *temp1 = *head, *temp2 = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (temp1 != NULL)
	{
		count += 1;
		temp1 = temp1->next;
	}
	half = count / 2;
	odd_half = half;
	temp1 = *head;
	if (count % 2 != 0)
		odd_half = half + 1;
	for (counter = 0; counter < odd_half; counter++)
		temp2 = temp2->next;
	temp2 = reverse_listint(&temp2);
	for (counter = 0; counter < half && is_palindrome; counter++)
	{
		if (temp1->n != temp2->n)
			is_palindrome = 0;
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	return (is_palindrome);
}

/**
 * @*reverse_listint - Reverses a linked list in place
 * @head: Pointer to a pointer pointing to the first item in the list
 * Return: The new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

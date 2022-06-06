#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is palindrome or not
 * @head: pointer to the head pointer
 *
 * Return: 1 if palindrome
 *	   0 if  not palindrome
 */

int is_palindrome(listint_t **head)
{
	int counter, half, count = 0, is_palindrome = 1;
	listint_t *temp1 = *head, *temp2;
	int *half1, *half2;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (temp1 != NULL)
	{
		count += 1;
		temp1 = temp1->next;
	}
	if (count % 2 != 0)
		return (!is_palindrome);
	half = count / 2;
	temp1 = *head;
	for (counter = 0; counter < half; counter++)
		temp1 = temp1->next;
	temp2 = temp1;
	temp1 = *head;
	half1 = malloc(sizeof(int) * half);
	half2 = malloc(sizeof(int) * half);
	for (counter = 0; counter < half; counter++)
	{
		half1[counter] = temp1->n;
		half2[counter] = temp2->n;
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	for (counter = 0; counter < half; counter++)
	{
		if (half1[counter] != half2[(half - 1) - counter])
		{
			is_palindrome = 0;
			break;
		}
	}
	return (is_palindrome);
}

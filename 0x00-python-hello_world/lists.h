#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct lsitInt_s - singly linked list.....
 * @n: integer....
 * @next: points to the next node.......
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct lsitInt_s
{
	int n;
	struct lsitInt_s *next;
} listInt_t;

size_t print_listint(const listint_t *h);
listInt_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

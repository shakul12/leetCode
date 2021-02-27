def odd_even_linked_list(head):
	if not head:
		return None

	odd=head
	even=head.next
	even_start=head.next
	while even:
		odd.next=even.next
		if odd.next:
			odd=odd.next
		even.next=odd.next
		even=even.next
	odd.next=even_start
	return head
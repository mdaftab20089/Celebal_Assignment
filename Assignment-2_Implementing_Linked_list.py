##Linked List code with O(n) Time complexity for inserting at end and deleting from the end.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def print_list(self):
        curr = self.head
        if not curr:
            print('[]')
            return
        elems = []
        while curr:
            elems.append(str(curr.data))
            curr = curr.next
        print(' -> '.join(elems))

    def delete_nth(self, n):
        if not self.head or n < 1:
            raise IndexError('Index out of range')
        if n == 1:
            self.head = self.head.next
            return
        prev, curr, count = self.head, self.head.next, 2
        while curr and count < n:
            prev, curr, count = curr, curr.next, count + 1
        if not curr:
            raise IndexError('Index out of range')
        prev.next = curr.next

# Test
if __name__ == '__main__':
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.print_list()        # 10 -> 20 -> 30

    ll.delete_nth(2)
    ll.print_list()        # 10 -> 30

    try:
        ll.delete_nth(5)
    except Exception as e:
        print(e)            # Index out of range

    empty = LinkedList()
    try:
        empty.delete_nth(1)
    except Exception as e:
        print(e)            # Index out of range




##Linked List code with O(1) Time complexity for inserting at end and deleting from the end.


class Node:
    """
    Represents a single node in a singly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Next pointer initialized to None

class LinkedList:
    """
    Manages a singly linked list of Node objects.
    """
    def __init__(self):
        self.head = None
        self._tail = None  # Track tail for O(1) appends instead of O(n)

    def append(self, data):
        """
        Add a node with the given data to the end of the list in O(1) time.
        """
        new_node = Node(data)
        if not self.head:
            self.head = self._tail = new_node
            return
        self._tail.next = new_node
        self._tail = new_node

    def print_list(self):
        """
        Print all the elements in the list. Consider using __str__ or returning
        a string for easier testing rather than direct printing.
        """
        if not self.head:
            print("List is empty.")
            return
        # Build elements in a list and join for cleaner output
        elems = []
        curr = self.head
        while curr:
            elems.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elems))

    def delete_nth(self, n):
        """
        Delete the nth node (1-based index) from the list.
        Raises IndexError for invalid operations.
        """
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")
        if n < 1:
            raise IndexError("Index out of range.")
        if n == 1:
            # Update head and tail if needed
            deleted = self.head
            self.head = self.head.next
            if deleted == self._tail:
                self._tail = None
            return
        prev = self.head
        curr = self.head.next
        count = 2
        while curr and count < n:
            prev = curr
            curr = curr.next
            count += 1
        if not curr:
            raise IndexError("Index out of range.")
        prev.next = curr.next
        if curr == self._tail:
            self._tail = prev  # Update tail when deleting last node

    def __str__(self):
        # Provide a string representation for easier debugging
        elems = []
        curr = self.head
        while curr:
            elems.append(str(curr.data))
            curr = curr.next
        return "LinkedList([" + ", ".join(elems) + "])"

# Sample usage and testing
if __name__ == "__main__":
    ll = LinkedList()
    # Append nodes to the list
    for value in (10, 20, 30):
        ll.append(value)
    print("Original list:", ll)

    # Delete the 2nd node
    try:
        ll.delete_nth(2)
        print("After deleting 2nd node:", ll)
    except IndexError as e:
        print(f"Error: {e}")

    # Attempt to delete a node out of range
    try:
        ll.delete_nth(5)
    except IndexError as e:
        print(f"Error: {e}")

    # Attempt to delete from an empty list
    empty_list = LinkedList()
    try:
        empty_list.delete_nth(1)
    except IndexError as e:
        print(f"Error: {e}")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)


    def print_elements(self): #თუ ცარიელია არაფერს არ დაბეჭდავს თუ არა დაბეჭდავს.
        current_node = self.head #->თუ self.head არ არსებობს none დამეწერება.

        while current_node:
          if current_node.next:
            print(f"{current_node.value}", end=' -> ')
          else:
            print(f"{current_node.value}")


          current_node = current_node.next

    def remove_tail(self):
        if self.head is None:
            print("Nothing in list to remove, because list is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        prev_node = None
        current_node = self.head
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None

# Test append and print:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(15)
linked_list.append(16)
linked_list.append(17)

linked_list.print_elements()

# Test remove and print:
linked_list.remove_tail()

linked_list.print_elements()

# Test remove again and print:
linked_list.remove_tail()

linked_list.print_elements()







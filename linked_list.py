# every time you create an object for node class it creates a new node for the linkedlist
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    # Inserts the data at beginning of the linkedlist
    def insert_at_beginning(self, data):        # Time Complexity O(1)
        node = Node(data, self.head)
        self.head = node

    # Inserts the data at end of the linkedlist
    def insert_at_end(self, data):      # Time Complexity O(n), where n = length of linkedlist
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    # Inserts a list of data into linkedlist
    def insert_values(self, datalist):      # Time Complexity O(n), where n = no.of elements in datalist
        self.head = None
        if datalist:
            for i in datalist:
                self.insert_at_end(i)

    # return the length of the linkedlist
    def length(self):       # Time Complexity O(n), where n = no.of elements in the linkedlist
        if self.head is None:
            return 0
        else:
            len = 0
            itr = self.head
            while itr:
                len += 1
                itr = itr.next
            return len

    # Removes the data from given index
    def remove_at(self, index):        # Time Complexity O(n), where n = (given index)-1
        if self.length() > index >= 0:
            if index == 0:
                self.head = self.head.next
                return
            else:
                count = 0
                itr = self.head
                while itr:
                    if count == index - 1:
                        itr.next = itr.next.next
                        break
                    itr = itr.next
                    count += 1
        else:
            raise Exception('Not a valid index.')

    # Inserts data at given index
    def insert_at(self, index, data):       # Time Complexity O(n)
        if self.length() > index >= 0:
            if index == 0:
                self.head = Node(data=data, next=None)
                return
            else:
                count = 0
                itr = self.head
                while itr:
                    if count == index - 1:
                        add = itr.next
                        itr.next = Node(data=data, next=add)
                        break
                    itr = itr.next
                    count += 1
        else:
            raise Exception("Not a valid index.")

    # Inserts data after the given value
    def insert_after_value(self, data, value):      # Time Complexity O(n)
        if self.length() > 0:
            itr = self.head
            index = 1
            while itr:
                if itr.data == value:
                    self.insert_at(index, data)
                    return
                itr = itr.next
                index += 1
            print("Value not found in the list.")
        else:
            print("LinkedList is empty.")

    # removes the data, when data == value
    def remove_by_value(self, value):       # Time Complexity O(n)
        if self.length() > 0:
            if self.head.data == value:
                self.head = self.head.next
            else:
                itr = self.head
                prev = self.head
                while itr:
                    if itr.data == value:
                        prev.next = itr.next
                        return
                    prev = itr
                    itr = itr.next
                print("Value not found in the list.")
        else:
            print("LinkedList is empty.")

    # clears the data form the linkedlist
    def clear(self):        # Time Complexity O(1)
        self.head = None

    # Prints the contents of the linkedlist
    def print(self):        # Time Complexity O(n), where n = no.of elements in linkedlist
        if self.head is None:
            print("LinkedList is empty.")
            return
        else:
            ll = ""
            itr = self.head
            while itr:
                ll += str(itr.data) + "-->"
                itr = itr.next
            print(ll)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([1, 2, 3, 4, 5, 6])
    ll.print()





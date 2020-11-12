class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """

        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        newnode = ListNode(data)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = newnode

        
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        while self.head!=None:
            if self.head.data == key:
                print( self.head.data)
            else:
                print(None)
            self.head = self.head.next

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        while self.head!=None:
            if self.head.data == key:
                self.head = self.head.next
                return

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
if __name__ == '__main__':
    x1= SinglyLinkedList()
    x1.append(5)
    x1.append(6)

    x1.find(6)
    x1.printList()

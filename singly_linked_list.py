from ctypes import pointer


class SinglyLinkedList:
    class _Node:
        def __init__(self, element, nextNode=None):
            self.element = element
            self.nextNode = nextNode

    def __init__(self):
        self._head = None
        self._size = 0

    def __str__(self):
        result = ""
        pointer = self._head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result

    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1

    def add_last(self, element):
        newNode = self._Node(element)
        if self._head == None:
            self._head = newNode
        else:
            pointer = self._head
            while pointer.nextNode != None:
                pointer = pointer.nextNode
            pointer.nextNode = newNode
        self._size += 1

    def remove_first(self):
        if self._size > 0:
            if self._size == 1:
                value = self._head.element
                self._head = None
                self._size -= 1
                return value
            else:
                pointer = self._head
                value = self._head.element
                self._head = pointer.nextNode
                pointer.nextNode = None
                self._size -= 1
                return value
        return None

    def remove_last(self):
        if self._size > 0:
            if self._size == 1:
                value = self._head.element
                self._head = None
                self._size -= 1
                return value
            else:
                pointer = self._head
                while pointer.nextNode.nextNode != None:
                    pointer = pointer.nextNode
                value = pointer.nextNode.element
                pointer.nextNode = None
                self._size -= 1
                return value
        return None

    def __len__(self):
        return self._size


def main():
    myList = SinglyLinkedList()
    # myList.add_first(10)
    # myList.add_first(20)
    # myList.add_first(30)
    myList.add_last(77)
    myList.add_last(78)
    myList.add_last(79)
    print(str(myList))
    print(len(myList))
    print(f"Delete : {myList.remove_last()}")
    # print(f"Delete : {myList.remove_last()}")
    # print(f"Delete : {myList.remove_last()}")
    # print(f"Delete : {myList.remove_last()}")
    # print(f"Delete : {myList.remove_last()}")
    # print(f"Delete : {myList.remove_last()}")
    print(str(myList))
    print(len(myList))


main()

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next
class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break
# create csll using python
    def createCSLL(self,nodeValue):
        # initializing the node
        node=Node(nodeValue)
        node.next=node
        node.head=node
        node.tail=node
        return "circular singly linked list"
    
# insertion in circular singly linked list.

circularSSL=SLinkedList()
circularSSL.createCSLL(1)
print([node.value for node in circularSSL])



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
    def insertSSL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head= newNode
            self.tail=newNode
        else:
            if location ==0:
                newNode.next=self.head
                self.head=newNode
                # at the end of singly linked list
            elif location==1:
                newNode.next=None
                self.tail.next=newNode
                # at any point 
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
singlyLinkedList=SLinkedList()

# at the end of linked list
singlyLinkedList.insertSSL(1,1)
singlyLinkedList.insertSSL(2,1)
# at the beginning
singlyLinkedList.insertSSL(0,0)
singlyLinkedList.insertSSL(2,0)
# in the middle
singlyLinkedList.insertSSL(0,2)
singlyLinkedList.insertSSL(2,3)
print([node.value for node in singlyLinkedList])     
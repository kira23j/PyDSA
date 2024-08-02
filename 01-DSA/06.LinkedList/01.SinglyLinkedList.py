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
    # insert value at a given location
    def insertSSL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head= newNode
            self.tail=newNode
        else:
            # at the beginning
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
                
    # traverse singly linked list O(n) time complexity and o(1) space complexity
    def traverseSSL(self):
        if self.head is None:
            print("Doesnt Exist")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
    # searching for node in a singly linked list. o(N) time complexity and o(1) space complexity.
    def searchSSL(self,nodeValue):
        if self.head is None:
            return "The list doesnt exist"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue:
                    return node.value
                node=node.next
            return "The value isnt on the list"
    # delete a node from singly linked list
    def deleteNode(self,location):
        if self.head is None:
            print("The SSL doesnt exist")
        else:
            # case one from the beginning
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:self.head=self.head.next
            # case two from the end
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            # case 3 from any point
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
    # deleting entire SSL
    def deleteEntireSSL(self):
        if self.head is None:
            print("doesnt exist")
        else:
            self.head=None
            self.tail=None
    
                  
                  
singlyLinkedList=SLinkedList()
    # insertion of linked list
# at the end of linked list
singlyLinkedList.insertSSL(1,1)
singlyLinkedList.insertSSL(2,1)
# at the beginning
singlyLinkedList.insertSSL(0,0)
singlyLinkedList.insertSSL(2,0)
# in the middle
singlyLinkedList.insertSSL(0,2)
singlyLinkedList.insertSSL(2,3)
# calling out linked list
print([node.value for node in singlyLinkedList])
# traverse through linked list
singlyLinkedList.traverseSSL()   
# searching for a value in SSL
print(singlyLinkedList.searchSSL(2))
print(singlyLinkedList.searchSSL(33))
# traverse the values.
print([node.value for node in singlyLinkedList])
# deleting node from ssl
# from beginnig
singlyLinkedList.deleteNode(0)
print([node.value for node in singlyLinkedList])
# from the end
singlyLinkedList.deleteNode(1)
print([node.value for node in singlyLinkedList])
# from the middle
singlyLinkedList.deleteNode(2)
print([node.value for node in singlyLinkedList])
# delete entire SSL
singlyLinkedList.deleteEntireSSL()
print([node.value for node in singlyLinkedList])
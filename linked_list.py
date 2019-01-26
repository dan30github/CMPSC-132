#Lab #8
#Due Date: 10/12/2018, 11:59PM
########################################
#                                      
# Name:Daniel Melo Cruz
# Collaboration Statement: I saw the exam            
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    '''
        Creates a linked list in ascending order
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(8)
        >>> x.add(7)
        >>> x.add(3)
        >>> x.add(-6)
        >>> print(x)
        Head:Node(-6)
        Tail:Node(8)
        List:-6 3 7 8
        >>> len(x)
        4
        >>> x.pop()
        8
        >>> print(x)
        Head:Node(-6)
        Tail:Node(7)
        List:-6 3 7
    '''
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__
    def add(self, value):
        #write your code here
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            if len(self) == 1:
                if newNode.value > self.head.value:
                    self.head.next = newNode
                    self.tail = newNode
                else:
                    newNode.next = self.head
                    self.head = newNode
            else:
                current = self.head
                prev = None

                while newNode.value> current.value and current.next != None:
                    prev = current
                    current= current.next

                if current == self.head:
                    self.head = newNode
                    newNode.next = current

                elif current.next == None:
                    if newNode.value > current.value:
                        current.next = newNode
                        self.tail = newNode
                    else:
                        newNode.next = current
                        prev.next = newNode
                else:
                    newNode.next = current
                    prev.next = newNode
               
    
    def pop(self):
        #write your code here
        if self.isEmpty():
            return 'List is empty'
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            temp = self.tail
            self.tail = current
            current.next = None
            return temp.value



   
    def isEmpty(self):
        #write your code here
        return self.head==None
        

    def __len__(self):
        #write your code here
        current=self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

#Lab #10
#Due Date: 10/26/2018, 11:59PM
########################################
#                                      
# Name:Daniel Melo Cruz
# Collaboration Statement: I did not ask for help in this assignment. I just reviewed how queues work.
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
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
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        #write your code here
        return self.tail == None

    def __len__(self):
        #write your code here
        count = 0
        temp = self.head
        while temp is not None:
        	count+=1
        	temp = temp.next
        return count

    def enqueue(self, value):
        #write your code here
        newNode = Node(value)
        if self.isEmpty():
        	self.head = newNode
        	self.tail = newNode
        else:
        	self.tail.next = newNode
        	self.tail = newNode

    def dequeue(self):
        #write your code here
        if self.isEmpty():
        	return 'Queue is empty'
        elif len(self) == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            return temp
        else:
        	temp = self.head.value
        	self.head = self.head.next
        	return temp
        		




#Lab #9
#Due Date: 10/19/2018, 11:59PM
########################################
#                                      
# Name:Daniel Melo Cruz
# Collaboration Statement: I did not ask for help to do this.            
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
    '''
        Creates an empty Stack with support for push and pop operations
        >>> x=Stack()
        >>> x.pop()
        'Stack is empty'
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        #write your code here
        return self.top == None

    def __len__(self):
        #write your code here
        count = 1
        temp = self.top
        while temp.next is not None:
            temp = temp.next
            count += 1
        return count
    
    def peek(self):
        #write your code here
        return self.top.value

    def push(self,value):
        #write your code here
        newNode = Node(value)
        if Stack.isEmpty(self):
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        #write your code here
        if self.top == None:
            return 'Stack is empty'
        else:
            temp = self.top
            self.top = self.top.next
            return temp.value





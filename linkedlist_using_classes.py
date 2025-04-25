class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):

        self.head=None


    def display(self):
        current=self.head
        while current!=None:
            print(current.data,end=" ")
            current=current.next

    def insert_at_the_end(self):
        current=self.head
        if current==None:
            dataa=int(input("enter data of the new node"))
            new_node=node(dataa)
            self.head=new_node
            return
            #current.next=None
            
        while current.next:
            current=current.next
        
        data2=int(input("enter data of the new node"))
        current.next=node(data2)

    def insert_at_the_end(self):
        current=self.head
        if current==None:
            dataa=int(input("enter data of the new node"))
            new_node=node(dataa)
            self.head=new_node
            return
        
        while current.next:
            


ll=linkedlist()



while(True):
    n=int(input("1.display 2.insert at end 3.exit"))
    if n==1:
        ll.display()

    elif n==2:
        ll.insert_at_the_end()

    else:
        break




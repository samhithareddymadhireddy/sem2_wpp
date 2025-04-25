class Node:
    def __init__(self,data):
        self.data= data
        self.next =None
class linked_list():
    def __init__(self):
        self.head= None
    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
        print ('None')
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def delete_node(self,key):
        current=self.head
        if current is not None and current.data==key:
            self.head=current.next
            current=None
            return
        prev= None
        while current is not None and current.data!=key:
            prev=current
            current=current.next
        if current is None:
            print(f"Node with data {key} not found")
            return
        prev.next = current.next
        current = None
l1=linked_list()
while True:
    print("Menu \n1. Insert at end \n2. Insert at beginning \n3. Delete node \n4. Display linked list \n5. EXit")
    choice=int (input("enter your choice:"))
    if choice==1:
        data=int(input("enter data to insert at end:-"))
        l1.insert_at_end(data)
    elif choice==2:
        data=int(input("enter data to insert at biginning:-"))
        l1.insert_at_beginning(data)
    elif choice==3:
        key= int(input("enter data to delete:-"))
        l1.delete_node(key)
    elif choice==4:
        print("Linked List...")
        l1.display()
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again")
        
        




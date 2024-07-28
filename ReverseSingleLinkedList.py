class Listnode:
    def __init__(self,data):
        self.data=data
        self.next=None
def rev(head):
    pre=None
    current=head
    while current:
        nextnode=current.next
        current.next=pre
        pre=current
        current=nextnode
    return pre
def display(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print("None")
head=Listnode(9)
head.next=Listnode(90)
head.next.next=Listnode(80)
display(head)
f=rev(head)
display(f)

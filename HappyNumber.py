# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
a=354
def rev(a):
    b=0
    while(a!=0):
       rem=a%10
       b=b*10+rem
       #print(a)
       a//=10
    return b
def val(c):
    b=c
    d=[]
    for i in range(len(str(c))):
        d.append(((b%(10))*10**i))
        b//=10
    d.reverse()
    for i in range(len(str(c))):
        print(d[i],end="+")
c=rev(a)
print(rev(a))
print(val(c))
   

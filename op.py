'''a,b=map(int,input().split())
if a>b:
    print(a)
else:
    print(b)
num=int(input('enter the value of num:'))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

n=int(input("n="))
for i in range(10,n+1,-1):
    if i%2==0:
        print("even")
    else:
        print("odd")
n=int(input())
for i in range(10,n-1,-1):
    print(i,end='')'''
'''n=int(input())
i=100
if n<i:  
    while n>0:

       print(i,end=' ')
       i=i-1
       if i==n:
          break
else:
    print("invalid ")'''
'''n=int(input())
i=1
while i<=n:
    if i%3==0:
       continue
print(i,end=' ')
i+=1'''

'''
n=int(input())
s=0
while True:
    r=n%10
    n=n//10
    s=s+r
    if s<10:
        break
print(s)'''

'''
n,v=map(int,input().split())
for i in range(1,v+1):
    print(n,'x',i,'=',n*i)'''
'''   
n,r1,r2=map(int,input().split())
if(r1>r2):
    r1,r2=r2,r1
i=r1
while i<=r2:
    print(n,'x',i,'=',n*i)
    i+=1'''
#
'''v,n1,n2=map(int,input().split())
if(n1<=n2):
    for i in range(1,n2+1):
        print(v,'x',i,'=',v*i)
else:
    for i in range(n2,0,-1):
        print(v,'x',i,'=',v*i)'''
#
'''n=int(input())
count=0
while True:
    r=n%10
    n=n//10
    
    if r!=0:
        count+=1
    if n==0:
        break
print(count)'''
#
'''

n=int(input())
oc=0
ec=0
while True:
    r=n%10
    n=n//10
    if r%2==0:
        ec+=1
    else:
        oc+=1
if (ec==0 and oc!=0):
    print("odd")
elif(ec!=0 and oc==0):
    print("even")
elif(ec==0 and oc==0):
    print("mixed")'''
#
'''
n=int(input())#12345
even=0
odd=0
while n:
    r=n%10#5 4
    n=n//10#1234 123
    if r%2==0:
        even=even*10+r#40
    else:
        odd=odd*10+r#50
print(even,odd)
'''
  #############  separating even and odd
'''n=int(input())#12345
od=ev=0
o=e=1
while n:
    r=n%10
    n=n//10
    if r%2:
       od=od+o*r
       o=o*10
    else:
        ev=ev+e*r
        e=e*10
print(ev,od)'''

       ############
'''
n,sv,rv=map(int,input().split())
nn=0
c=1
while True:
    r=n%10
    n=n//10
    if r==sv:
       r=rv
    nn=nn+r*c
    c=c*10
        
print(nn)
'''
n=int(input())
mi=n%10
ma=n%10
mic=mac=0
while n:
    r=n%10
    n=n//10
    if r>ma:
        mac+=1
    elif r<mi:
        mic+=1
print(mic,mac)
    
    

    

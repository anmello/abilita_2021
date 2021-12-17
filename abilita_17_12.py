# -*- coding: utf-8 -*-
    
a=range(10)
for i in range(1,10,1):
    print(a[i])

def func_list(x,y):
        a=range(x,y,1)
        for i in range(y):
            print(a[i])
                  
func_list(0,3)

#prova con list e range
a=list(range(10))
for i in range(1,4):
    print(a[i])

stack=[5,6,7]
for i in range(1,3):
    stack.append(i)

print(stack)

imm=('physics','mathematics', 10)

print('gli elementi della tupla sono:', imm[0:3])

dict={x:x**2 for x in range(0,5)}
for i in dict:
    print(dict[i])
    
print(7 in dict)

odd_dict={x:(2*x+1)%10 for x in range(0,5)}

for i in odd_dict:
    print (odd_dict[i])
    
    
exact=5

a=int(input('Enter an integer:'))

if a==exact:
    print('Great')
    
else:
        print('You better try again')



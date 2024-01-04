x = 5
y = 10

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

print ("Hello World")

def sum(n):
    add = 0
    for i in range (1,n+1):
        add +=i*i*i
    return add
n=5
print (sum(n))
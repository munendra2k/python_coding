#function defination
def right_triangle(num):
    for i in range(num):
        for j in range(i):
            print("*",end=" ")
        print()

#calling function
right_triangle(5)

#function defination
def right_number(num):
    for i in range(1,num+1,+1):
        for j in range(1,i+1,+1):
            print(i,end=" ")
        print()

right_number(5)
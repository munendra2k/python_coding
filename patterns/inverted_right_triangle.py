#function defination
def inverted_right_triangle(num):
    for i in range(num,0,-1):
        for j in range(i,0,-1):
            print("*", end=" ")
        print()

#calling function
inverted_right_triangle(5)

#function defination
def inverted_num(num):
    for i in range(num,-1,-1):
        for j in range(i,-1,-1):
            print(f"{j}",end=" ")
        print()

#calling function
inverted_num(5)
try:
    # 0 division error
    a=int(input("Enter first number :"))
    b=int(input("Enter second number :"))
    print(a/b)

    #value error
    c=int(input("Enter your age :"))
    if c<=0:
        raise ValueError("Enter correct age")

    #file not found
    f1=open("C:\\Users\\dyp\\Desktop\\P Python Problem Statements\\exception_handling.txt","r")
    s=f1.read()
    f1.close()

    #type error
    # print("10"+10)

    #index out of box error
    s=[22,23,24,25,21]
    print(s[5])

except ZeroDivisionError:
    print("Enter correct value of second number except 0")

except FileNotFoundError:
    print("File not found")

# except ValueError:
#     print("Enter only number")

except TypeError:
    print("custom type error")

except IndexError:
    print("Index out of box")
# input 10 no. using arbitrary argument & find out occerences of particular element in the argument


def show(*data):
    a=int(input('Enter no. : '))
    print(f"{a} occurs {data.count(a)} times")
show(1,2,2,3,4,5,5,3,9,7)



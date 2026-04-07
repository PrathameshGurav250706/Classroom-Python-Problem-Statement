# Display product info. having product name,quantity,price,color using abitrary keyword argument parameters
def show(**data):                #function which can access key,value pair
    for i,j in data.items():
        print(i,':',j)
show(name='car',qty=10,price=100000,color='Red-yellow')    #function calling with parameters


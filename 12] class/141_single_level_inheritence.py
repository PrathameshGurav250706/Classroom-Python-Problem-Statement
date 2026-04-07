# Override the constructor using single level inheritance having product name, product type as a argument of first conctructor and color as argument of derived class
class product_info1:
    def __init__(self,name,type):
        self.name=name
        self.type=type
        print("Product name :",self.name)
        print("Product type :",self.type)

class product_info2(product_info1):
    def __init__(self, name, type,color):
        self.color=color
        super().__init__(name, type)
        print("Product color :",self.color)

data=product_info2("Book","History","Red")

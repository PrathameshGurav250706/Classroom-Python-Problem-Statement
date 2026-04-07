# use class as vehicle having attribute vehicle type ,color and milege inherite other class which will display vehicle information
class vehicle:
    def __init__(self):
        self.name="Ferrari"
        self.type="4 wheeler"
        self.color="red"
        self.milege=120

class show(vehicle):
    def __init__(self):
        super().__init__()
        print("Vehicle Name : ",self.name)
        print("Vehicle Type : ",self.type)
        print("Vehicle Color : ",self.color)
        print("Vehicle Milege : ",self.milege)
    
s=show()
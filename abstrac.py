from abc import ABC, abstractmethod   
class Car(ABC):
    @abstractmethod
    def mileage(self, mile):
        print("Your driving mileage is: ",mile) 
        pass
    
class Tesla(Car):
# we defined the the mileage function 
    def mileage(self, mile):   
        print("The mileage is {}".format(mile))   



# object 
t= Tesla ()   
t.mileage(40)   
  


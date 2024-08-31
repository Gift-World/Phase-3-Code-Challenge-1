class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
       
        print(f"{self.make} {self.model} {self.year} ")   
        
     
car =Car("Mercedez","E250","2022")   
car.display_info()      
        
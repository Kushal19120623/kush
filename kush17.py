#obejct orineted program
class human:
    def __init__(self,name,age,salary="unknown"):
        print("give me your name and age")
        self.name=name
        self.age=age
        self.salary=salary

    def walk(self):
        print(f"{self.name} is walking and his age is {self.age} and his salary is {self.salary}")
       
kushal= human("kushal",19,12)
gowthu=human("gowtham",45)
kushal.walk()
gowthu.walk()
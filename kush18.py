#abstraction
class car:
    def start_engine(self):
        print("engine started")

    def accelerate(self):
        print("car acceleration")

    def brake(self):
        print("car stoping")

cars=car()
car.start_engine()
car.accelerate()
car.brake()
#encapsulation
class atm:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance+= amount
        print(f"deposited{amount}.new balance:{self.__balance}")

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw{amount}.new balance:{self.__balance}")
        else:
            print("insufficient balance")

atms= atm(1000)
atms.deposit(500)
atms.withdraw(300)

class database:
    def __init__(self):
        self._storage = {}

    def write(self,key,value):
        self.storage[key]=value

    def read(self,key):
        print(self.storage[key])
k=database()
k.write("kushal","kush")
k.read("kushal")
print(k.storage)
#inheritence

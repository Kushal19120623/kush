#obejct orineted program
class human:
    def __init__(self,name):
        self.name=name

    def walk(self):
        print(f"{self.name} is walking")
       
kushal= human("kushal")
kushal.walk()
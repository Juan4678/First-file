from abc import ABC,abstractmethod     #An abstract class needs to import abc and abstract method to be abstract


class Computer(ABC):
    @abstractmethod
    def process(self):      #Abstract method
        pass

class Laptop(Computer):
    def process(self):
        print("It´s running")


class Programmer:
    def work(self,com):
        print("Solving bugs")
        com.process()


#com= Computer()
#com.process()
com1= Laptop()

Prog1=Programmer()
Prog1.work(com1)


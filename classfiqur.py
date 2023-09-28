from abc import ABC,abstractmethod
class Fiqur(ABC):
    @abstractmethod
    def sahe(self):
        pass
    @abstractmethod
    def perimetr(self):
        pass
class Kvadrat(Fiqur):
    def sahe(self,a,b):
        return a * b
    def perimetr(self,a,b):
        return 2*a + 2*b

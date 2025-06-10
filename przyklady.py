# class Example:
#     def __init__(self):
#         self.public_attribute = "Accessible from anywhere"
#         self._protected_attribute = "Accessible within the class and subclasses" #Tylko konwencja - interpreter nie wymusza!
#         self.__private_attribute = "Accessible only within this class"

#     def innerMethod(self):
#         print(self.public_attribute)
#         print(self._protected_attribute)
#         print(self.__private_attribute)

# class SubExample(Example):
#     def __init__(self):
#         super().__init__()

#     def subClassMethod(self):
#         print(self.public_attribute)
#         print(self._protected_attribute)
#         #print(self.__private_attribute)  # To nie zadziała, ponieważ __private_attribute jest prywatne dla Example

# obj = Example()
# obj.innerMethod()
# sub_obj = SubExample()
# sub_obj.subClassMethod()

# print(obj.public_attribute)  # Dostępne
# print(obj._protected_attribute)  # Dostępne, ale niezalecane
# print(obj.__private_attribute)  # To spowoduje błąd, ponieważ __private_attribute jest prywatne dla Example


# #Idea Duck Typing - "Jeżeli coś wygląda jak kaczka, pływa jak kaczka i kwacze jak kaczka, to najprawdopodobniej jest kaczką"
# class type1:
#     def method(self):
#         print("Method from type1")

# class type2:
#     def method(self):
#         print("Method from type2")

# class type3:
#     def method(self):
#         print("Method from type3")

# types = [type1(), type2(), type3()]

# for t in types:
#     t.method()  # Wywołuje metodę z każdego typu, niezależnie od tego, jakiego jest typu


# class BaseClass:
#     def method(self):
#         print("Method from BaseClass")

# class FirstChildClass(BaseClass):
#     def method(self):
#         print("Method from FirstChildClass")

# class SecondChildClass(BaseClass):
#     def method(self):
#         print("Method from SecondChildClass")

# class GrandChildClass(FirstChildClass, SecondChildClass):
#     def method(self):
#         print("Method from GrandChildClass")
    
# obj = GrandChildClass()
# obj.method() # Zadziała Method Resolution Order (MRO) - Python najpierw sprawdza klasy bazowe w kolejności, w jakiej zostały zdefiniowane, a następnie przechodzi do ich rodziców.
# # Można sprawdzić MRO dla klasy
# print(GrandChildClass.__mro__)  # Wyświetla kolejność rozwiązywania metod (MRO) dla GrandChildClass


# from abc import ABC, abstractmethod

# class AbstractClass(ABC):
#     @abstractmethod
#     def abstract_method(self):
#         pass

#     def concrete_method(self):
#         print("This is a concrete method in the abstract class")

# class ConcreteClass(AbstractClass):
#     def abstract_method(self): #Konkretna implementacja metody abstrakcyjnej
#         print("Implemented abstract method")

# obj = ConcreteClass()
# obj.abstract_method()  # Wywołuje zaimplementowaną metodę abstrakcyjną
# obj.concrete_method()  # Wywołuje metodę z klasy bazowej


# class MetaClass(type):
#     def __new__(cls, name, bases, dct):
#         print(f"Creating class {name} with metaclass {cls.__name__}")
#         if 'custom_method' not in dct:
#             raise TypeError(f"{name} must implement a 'custom_method'")
#         return super().__new__(cls, name, bases, dct)

# class CustomClass(metaclass=MetaClass):
#     def custom_method(self):
#         print("This is a custom method in CustomClass")

# class BadCustomClass(metaclass=MetaClass):
#     # Nie implementuje 'custom_method', co spowoduje błąd
#     pass

# from abc import ABC, abstractmethod

# #1 stwórz abstrakcyjny interfejs (Produkt)
# class Product(ABC):
#     @abstractmethod
#     def functionality(self, argument: str):
#         pass
# #2 stwórz konkretne produkty
# class ConcreteProductA(Product):
#     def functionality(self, argument: str):
#         return f"ConcreteProductA functionality with {argument}"
    
# class ConcreteProductB(Product):
#     def functionality(self, argument: str):
#         return f"ConcreteProductB functionality with {argument}"
    
# #3 stwórz fabrykę
# class Factory:
#     @staticmethod
#     def create_product(product_type: str) -> Product:
#         if product_type == "A":
#             return ConcreteProductA()
#         elif product_type == "B":
#             return ConcreteProductB()
#         else:
#             raise ValueError(f"Unknown product type: {product_type}")

# #4 użyj fabryki do tworzenia produktów
# product_a = Factory.create_product("A")
# product_b = Factory.create_product("B")
# print(product_a.functionality("test argument"))
# print(product_b.functionality("test argument"))

# from abc import ABC, abstractmethod

# #Zdefiniuj produkt:
# class Product:
#     def __init__(self):
#         self.option1 = None
#         self.option2 = None
#         self.option3 = None

#     def __str__(self):
#         return f"Product with options: {self.option1}, {self.option2}, {self.option3}"

# #Zdefiniuj interfejs Budowniczego:
# class ProductBuilder(ABC):
#     @abstractmethod
#     def set_option1(self):
#         pass

#     @abstractmethod
#     def set_option2(self):
#         pass

#     @abstractmethod
#     def set_option3(self):
#         pass

#     @abstractmethod
#     def build(self) -> Product:
#         pass

# #Zdefiniuj konkretny budowniczego:
# class ConcreteProductBuilder(ProductBuilder):
#     def __init__(self):
#         self.product = Product()
    
#     def set_option1(self):
#         self.product.option1 = "Option 1 variant"
    
#     def set_option2(self):
#         self.product.option2 = "Option 2 variant"

#     def set_option3(self):
#         self.product.option3 = "Option 3 variant"
    
#     def build(self) -> Product:
#         return self.product

# #Zdefiniuj dyrektora:
# class Director:
#     def __init__(self, builder: ProductBuilder):
#         self.builder = builder

#     def construct_product(self):
#         self.builder.set_option1()
#         self.builder.set_option2()
#         self.builder.set_option3()
#         return self.builder.build()

# #Użyj budowniczego i dyrektora do stworzenia produktu:
# builder = ConcreteProductBuilder()
# director = Director(builder)
# product = director.construct_product()
# print(product)

# Singleton Pattern Example
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass = SingletonMeta):
    def test(self):
        print("Singleton test method")
    pass

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

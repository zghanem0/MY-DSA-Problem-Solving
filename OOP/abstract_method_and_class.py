# usually used with factory method to let who will inherit these classes and methods to custom them.ModuleNotFoundError


from abc import ABC, abstractmethod

# Define the CoffeeFactory interface

# Abstract Class


class CoffeeFactory(ABC):
    @abstractmethod
    def create_coffee(self):
        pass

# Concrete Coffee Factory for Latte


class LatteFactory(CoffeeFactory):
    def create_coffee(self):
        return Latte()

# Concrete Coffee Factory for Americano


class AmericanoFactory(CoffeeFactory):
    def create_coffee(self):
        return Americano()

# Concrete Coffee Factory for Macchiato


class MacchiatoFactory(CoffeeFactory):
    def create_coffee(self):
        return Macchiato()

# Concrete Coffee Factory for Flat White


class FlatWhiteFactory(CoffeeFactory):
    def create_coffee(self):
        return FlatWhite()

# Concrete Coffee Factory for Cortado


class CortadoFactory(CoffeeFactory):
    def create_coffee(self):
        return Cortado()

# Define the Coffee class and its subclasses


class Coffee(ABC):
    @abstractmethod
    def brew(self):
        pass


class Latte(Coffee):
    def brew(self):
        return "Brewing Latte"


class Americano(Coffee):
    def brew(self):
        return "Brewing Americano"


class Macchiato(Coffee):
    def brew(self):
        return "Brewing Macchiato"


class FlatWhite(Coffee):
    def brew(self):
        return "Brewing Flat White"


class Cortado(Coffee):
    def brew(self):
        return "Brewing Cortado"


def order_coffee(factory):
    coffee = factory.create_coffee()
    print(f"{coffee.brew()} for you!")


# Usage
latte_factory = LatteFactory()
order_coffee(latte_factory)

americano_factory = AmericanoFactory()
order_coffee(americano_factory)

macchiato_factory = MacchiatoFactory()
order_coffee(macchiato_factory)

flat_white_factory = FlatWhiteFactory()
order_coffee(flat_white_factory)

cortado_factory = CortadoFactory()
order_coffee(cortado_factory)

#Item Base Class
class Item():
    def __init__ (self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__ (self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
#Items
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
        description="A shiny ass coin with {} printed on the front.\nMoney won't buy happiness, but it will pay rent.".format(str(self.amt)),
        value=self.amt)

class fogPill(Item):
    def __init__(self):
        super().__init__(name="Fog Light Pill",
        description="A small pill that can temporarily grant you the power to see through the fog.",
        value=8.60)

#Weapons
class Weapon(Item):
        def __init__(self, name, description, value, minDamage, maxDamage):
            self.minDamage = minDamage
            self.maxDamage = maxDamage
            super().__init__(name, description, value)

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.maxDamage)

class Book(Weapon):
    def __init__(self):
        super().__init__(name="Book",
        description="A dusty, sturdy hardback. Good for bludgeoning and busting some knowledge.",
        value=5,
        minDamage=2,
        maxDamage=10)

class BoC(Weapon):
    def __init__(self):
        super().__init_(name="Blade of Confidence",
        description="A long, sharp blade with a hella fancy handle.\nAs soon as you hold it, you know you've got this.",
        value=100,
        minDamage=10,
        maxDamage=50)

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

#Minions
class Demon(Enemy):
    def __init__(self):
        super().__init__(name="Demon",
        hp=20,
        damage=5)

class Gremlin(Enemy):
    def __init__(self):
        super().__init__(name="Gremlin",
        hp=35,
        damage=8)

#Bosses
class Sloth(Enemy):
    def __init__(self):
        super().__init__(name="Sloth",
        description="A giant, furry demon of slumber.\nHe may move slow, but when he hits you, he'll hit hard."
        hp=100,
        damage=60)

class Panic(Enemy):
    def __init__(self):
        super().__init__(name="panic",
        description="He'll break you're concentration as you worry if you left the oven on.",
        hp=75,
        damage=30)

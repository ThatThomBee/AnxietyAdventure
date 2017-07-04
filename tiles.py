import items, enemies, time

#Base tile
class emptyTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#Making sure that any accidental boring tile raises an error
def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
    raise NotImplementedError()

#First Room
class wakeUpRoom(MapTile):
    def intro_text(self):
        return "You wake up from a typically restless slumber."
        time.sleep(2)
        return """
        Wiping the sleep from your eye you expect to see the usual 2pm sunshine flooding your room.
        Instead, you can barely see in front of you through a thick layer of fog.
        """
        time.sleep(2)
        return "It's impossible to know where you are, but you feel a wall against your back, and can feel something in your pockets?"
        time.sleep(2)
        checkPocket = raw_input("Do you want to check your pockets?")
        if checkPocket[0] = "y":
            return "You feel a pack of cigarettes and a lighter."
        else:
            return "If you say so man, move on?"

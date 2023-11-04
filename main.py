import random

class Cat:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_hunts(self):
        print("Time to hunts")
        self.progress += 0.12
        self.gladness -= 7

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_play_with_the_owner(self):
        print("Time to play")
        self.gladness += 5
        self.progress -= 0.1

    def to_play_pranks(self):
        print("Time to pranks")
        self.gladness += 5
        self.progress += 0.005

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("It got too boring")
            self.alive = False

    def end_of_play(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,  2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)

        if live_cube == 1:
            self.to_hunts()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play_with_the_owner()
        elif live_cube == 4:
            self.to_play_pranks()

        self.end_of_play()
        self.is_alive()


nick = Cat(name="Marty")

for day in range(1, 366):
    if nick.alive == False:
        break

    nick.live(day)
# Sub Class logic

class Main_functions:
    life = 0
    speed = 0
    def __init__(self, lf, spd):
        self.life = lf
        self.speed = spd

    

class Create_player(Main_functions):
    name = ''

    def define_att(self, nam):
        self.name = nam

p1 = Create_player(10, 3.0)
p1.define_att('Jonh')

print(p1)


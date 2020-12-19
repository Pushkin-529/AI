у=1
class Pistolet:
    cnt = 0
    __cnt = 0       # Private
    _cnt = 0        # Protected

    def __init__(self,  color, max_capacity, model):              # инициализатор
        self.color = color
        self.max_capacity = max_capacity
        self.model = model
        Pistolet.cnt += 1
        Pistolet.__cnt += 1
        print(f"{self.model} делает БАХ!!!")

    def shoot(self):
        print(f"{self.model} делает БАХ!!!")

    @classmethod
    def get_cnt(cls):   # Доступ к приватному полю класса, а не объекта
        return Pistolet.__cnt

    @classmethod
    def set_cnt(cls, set_to):
        cls.__cnt = set_to



с = Pistolet
pistolet = Pistolet("red", 32, "TT")
pistolet2 = Pistolet("red", 32, "Glock")

pistolet.shoot()
pistolet2.shoot()

# Доступ к полям
print(Pistolet.cnt)
print(pistolet2.cnt)
pistolet2.cnt = 3
print(pistolet.cnt)
print(pistolet2.cnt)

# доступ к защищенным и приватным полям только через Set\Get
#print(pistolet.__cnt)    # Не может обратиться к переменной поскольку она Private
print(pistolet.get_cnt())
pistolet2.set_cnt(50)
print(pistolet.get_cnt())

# Наследование
class Machinegun:
    def _execute(self):
        print("ОГОНЬ!!!")
    def __call__(self, *args, **kwargs):
        self._execute()

l = [Pistolet("Red", "32", "TT") for _ in range(10)]
m_gun = Machinegun()

Weapon_Factory = [m_gun, m_gun, m_gun, m_gun, pistolet, pistolet, pistolet, pistolet]

class ToyPistol(Pistolet):
    def __init__(self, color, max_capacity, model, min_age):
        super(ToyPistol, self).__init__(color, max_capacity, model)
        self.min_age = min_age
        
    def shoot(self):
        print(f"{self.model} делает ПСЫК ПСЫК!!!")

class AnotherToyPistol(ToyPistol):
    def __init__(self, color, max_capacity, model, min_age, max_age):
        super(AnotherToyPistol, self).__init__(color, max_capacity, model, min_age)
        self.max_age = max_age
        if (self.min_age < 3):
            print(f"В таком маленьком возврасте ({self.min_age}) вам нельзя пользоваться пистолетом {self.model}")
        if self.max_age >5:
            print(f"В таком возврасте ({self.max_age}) вам неприлично пользоваться пистолетом {self.model}")



toy_pistol = ToyPistol("Green", 5, "WaterPistol", 3)
toy_pistol.shoot()
childpistol = AnotherToyPistol("Green", 5, "ChildPistol", 2, 10)

d = 1


class Laze:
    def __init__(self, level, long_sleep):
        self.__level = level
        self.__long_sleep = long_sleep

    def sleep(self):
        print(self.long_sleep * "zZZz")

    @property
    def level(self):
        return self.__level / 2
    @level.setter
    def level(self, value):
        print("Чем меньше - тем лучше")
        print(self.__level + value)
        return self.__level + value


    @property
    def long_sleep(self):
        return "Сплю сколько хочу"
    @long_sleep.setter
    def long_sleep(self, value):
        print("Нельзя меня будить")


kamil = Laze(80, 24*7)
# # kamil.sleep()
# print(kamil._Laze__long_sleep)
# print(kamil.long_sleep)
# kamil.long_sleep = 8
# print(kamil.long_sleep)
print(kamil.level)
kamil.level = 10

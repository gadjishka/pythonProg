import os, time
os.system("cls")
print("#"*49)
print("#"*17 + "  ПРЕДИСЛОВИЕ  " + "#"*17)
print("#"*49)
print("Апокалипсис наступил внезапно.Когда он начался,вы покупали шаурму[эх , жаль вы ее больше не попробуете.Ой,отвлекся от темы]")
print("Ну так вот , вы никак не ожидали этого и конечно же не были готовы.")
print("Но у вас в машине всегда лежат пистолет , дубинка , пулемет , пара гранат и самурайский меч")
print("Оружие у вас в машине , т.к. вы полицейский , а самурайский меч вы везли в музей , но он , наверное , закрыт")
print("Вы сразу побежали к машине,но по двум причинам: за пистолетом и за пакетом , ведь вы взяли много шаурмы и уже отдали деньги ")
input("Для продолжения нажмите Enter ")
os.system("cls")
class No_such_weapon(Exception):
    pass
class Human:
    def init(self):
        self.hp = 0
        self.damage = 0

    def attack(self, target):
        target.hp -= self.damage
        print(self.name,"нанес урон", self.damage)

    def your_name(self):
         print("$"*40)
         self.name = input("Скажи свое имя , боец : ")

    def your_class(self):
        print("$"*40)
        print("Выбери свой класс,боец : ")
        print(" КЛАССЫ        КОЛ-ВО HP       КОЛ-ВО АПТЕЧЕК    ")
        print(" Медик           80                  6 ")
        print(" Дрищ            90                  2 ")
        print(" Слабак          70                  4 ")
        print(" Бодибилдер      150                 0 ")
        lan = input("Кто-ты , солдат : ")
        if lan == "1":
            print("Выбран класс медиков.")
            self.hp = 80
            self.count_kit = 8
        elif lan == "2":
             print("Выбран класс дрищей.")
             self.hp = 90
             self.count_kit = 2
        elif lan == "3":
              print("Выбран класс слабаков.")
              self.hp = 70
              self.count_kit = 4
        elif lan == "4":
              print("Выбран класс бодибилдеров.")
              self.hp = 150
              self.count_kit = 2

    def your_weapon(self):
        print("="*50)
        print("="*10,"Выбор оружия для следущей атаки","="*20)
        print("="*50)
        print("Оружия                             их Урон")
        print("1)Пистолет                              15")
        print("2)Пулемет                               25")
        print("3)Дубинка                               10")
        print("4)Граната                               30")
        print("5)Самурайский меч                       20")
        i = input("Чем будешь убивать зомби? Ваш выбор : ")
        if i == "1":
            print("ПИУ ПИУ (звук стрельбы пистолета)")
            self.damage = 15
        elif i == "2":
            print("РАТАТАТАТАТААТААТААТАТАТАТ (звук стрельбы пулемета)")
            self.damage = 25
        elif i == "3":
            print("ТАААА ШАААААААА (звук удара дубинкой)")
            self.damage = 10
        elif i == "4":
            print("БАААААААААААХ (звук взрыва гранаты)")
            self.damage = 30
        elif i == "5":
            print("КИЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ (звук удара самурайского меча)")
            self.damage = 20
        if int(i) > 5:
            raise No_such_weapon("Такого оружия нет в рюкзаке! Выбери другое.")
class Player(Human):
    def __init__(self):
        self.hp = 0
        self.damage = 0
        self.count_kit = 0
        self.name = 0
    def heal(self):
        if self.count_kit > 0:
            self.count_kit -= 1
            self.hp += 30
            print("Вы воспользовались аптечкой. Ваше здоровье",self.hp,"уведичилось на 30 единиц")
        else:
            print("Сорян , аптечек больше нет!")



class Zombie:
    def __init__(self):
        self.hp = 25
        self.damage = 5
    def death(self):
        print("Уааааааа")
        print("Зомби мертв")
    def attack(self, target):
        target.hp -= self.damage
        print("Зомбарь нанес урон", self.damage)
def game():
    count_kill = 0
    gamer = Player()
    gamer.your_name()
    gamer.your_class()
    zombie = Zombie()
    time.sleep(1)
    os.system("cls")

    while True:
        try:
            print("Первая волна")
            print("HP  у зомби = 25. DAMAGE у зомби = 5")
            gamer.your_weapon()
            gamer.attack(zombie)
            zombie.attack(gamer)
            if zombie.hp <= 0:
                zombie.death()
                count_kill +=1

            if count_kill >= 5:
                print("Вторая волна")
                print("Зомби стали сильнее. HP = 45. DAMAGE = 20")
                zombie.hp = 45
                zombie.damage = 20

            input("Для продолжения нажмите Enter ")
            os.system("cls")
            print("#"*70)
            print("#"*70)
            print("#"*70)
            print("Ваш уровень здоровья -",gamer.hp)
            print("Вы хотите воспользоваться аптечкой?")
            print("1)Да 2)Нет")
            i = int(input("Ваш выбор : "))
            if i == 1:
                gamer.heal()
            if gamer.hp <= 0:
                os.system("cls")
                print("&"*50)
                print("&"*10,"Грустный конец","&"*10)
                print("&"*50)
                print(gamer.name,"погиб в бою с зомбарями-алкашами...")
                print( " ______       ____      ____ ___    ______")
                print( "/   ___|     /   |     /   |/   |  |  ____|")
                print( "|  |        / /| |    / /|   /| |  |  |___")
                print( "|  |  _    / /_| |   / / |/ | | |  |   ___|")
                print( "|  |_| |  / /  | |  / /       | |  |  |___")
                print( "\______/ /_/   |_| /_/        |_|  |______|")
                print("")
                print( " ________   __     ___   ______     ______")
                print( "/   __   \ |  |   /  /  |  ____|   |   _  \ ")
                print( "|  |  |  | |  |  /  /   |  |___|   |  |_| |")
                print( "|  |  |  | |  | /  /    |   ___|   |   _  /")
                print( "|  |__|  | |  |/  /     |  |___|   |  | \ \ ")
                print( "\________/ |_____/      |______|   |__|  \_\ ")
                break
        except No_such_weapon as sms:
            print(sms)
game()

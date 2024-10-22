# Определяем родительский класс Hero
class Hero:
    def __init__(self, name, level=1, experience=0):
        # Инициализация свойств героя: имя, уровень и опыт
        self.name = name           # Имя героя
        self.level = level         # Уровень героя, по умолчанию 1
        self.experience = experience  # Опыт героя, по умолчанию 0

    def level_up(self):
        # Метод для повышения уровня героя
        self.level += 1            # Увеличивает уровень на 1
        self.experience = 0        # Сбрасывает количество опыта
        print(f"{self.name} повысел уровень до {self.level}!")  # Выводит сообщение о повышении уровня

    def get_info(self):
        # Метод для получения информации о герое
        return f"{self.name} | уровень: {self.level} | опыт: {self.experience}"


# Класс Warrior (Воин) наследует свойства от родительского класса Hero
class Warrior(Hero):
    def __init__(self, name, strength, defense, attack):
        # Инициализация свойств воина, включая свойства родителя
        super().__init__(name)      # Вызывает конструктор родительского класса
        self.strength = strength     # Сила героя
        self.defense = defense       # Защита героя
        self.attack = attack         # Атака героя

    def attack_enemy(self):
        # Метод для атаки противника
        print(f"{self.name} атакует с {self.attack} силы атаки!")  # Выводит сообщение об атаке

    def defend(self):
        # Метод для повышения защиты
        print(f"{self.name} повышает защиту до {self.defense + 5}!")  # Выводит сообщение об увеличении защиты


# Класс Mage (Маг) наследует свойства от родительского класса Hero
class Mage(Hero):
    def __init__(self, name, magic_power, mana):
        # Инициализация свойств мага
        super().__init__(name)      # Вызывает конструктор родительского класса
        self.magic_power = magic_power  # Сила магии
        self.mana = mana              # Количество маны
        self.spellbook = []           # Список заклинаний (изначально пуст)

    def cast_spell(self, spell):
        # Метод для использования заклинания
        if self.mana > 0:              # Проверяет, есть ли мана
            self.mana -= 1              # Уменьшаем ману на 1
            print(f"{self.name} использует {spell} с силой магии {self.magic_power}!")  # Выводит сообщение о заклинании
        else:
            print(f"{self.name} кончилась мана!")  # Если маны не осталось, выводит сообщение

    def recharge_mana(self, amount):
        # Метод для восстановления маны
        self.mana += amount            # Увеличивает количество маны на указанное значение
        print(f"{self.name} мана востановлена до {self.mana}!")  # Выводит сообщение о восстановлении маны


# Класс Ranger (Стрелок) наследует свойства от родительского класса Hero
class Ranger(Hero):
    def __init__(self, name, agility, ranged_attack, arrows):
        # Инициализация свойств стрелка
        super().__init__(name)         # Вызывает конструктор родительского класса
        self.agility = agility          # Ловкость героя
        self.ranged_attack = ranged_attack  # Урон от выстрела
        self.arrows = arrows            # Количество стрел

    def shoot(self):
        # Метод для стрельбы
        if self.arrows > 0:             # Проверяет, есть ли стрелы
            self.arrows -= 1             # Уменьшает количество стрел на 1
            print(f"{self.name} стреляет из лука с {self.ranged_attack} урона!")  # Выводит сообщение о стрельбе
        else:
            print(f"{self.name} закончились стрелы!")  # Если стрел не осталось, выводит сообщение

    
    def reload(self):
        # Метод для перезарядки стрел
        self.arrows += 5                # Увеличивает количество стрел на 5
        print(f"{self.name} стрел востановлено до: {self.arrows}")  # Выводит сообщение о перезарядке стрел


# Вывод для тестирования системы
if __name__ == "__main__":
    # Создаем героев с их характеристиками
    warrior = Warrior("Артас", strength=10, defense=7, attack=15)  # Создаем воина
    mage = Mage("Гендальф", magic_power=20, mana=5)                     # Создаем мага
    ranger = Ranger("Легалас", agility=15, ranged_attack=10, arrows=3) # Создаем стрелка

    # Вывод информации о каждом герое
    print(warrior.get_info())  # Информация о воине
    print(mage.get_info())     # Информация о маге
    print(ranger.get_info())   # Информация о стрелке

    # Выполняем действия героев
    warrior.attack_enemy()      # Воин атакует
    mage.cast_spell("Fireball") # Маг использует заклинание
    ranger.shoot()              # Стрелок стреляет

    # Увеличиваем уровень воина
    warrior.level_up()          # Увеличиваем уровень воина
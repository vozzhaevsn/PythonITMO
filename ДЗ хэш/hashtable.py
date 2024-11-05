class HashTable: #Создаёт класс HashTable, который будет представлять собой хэш таблицу.
    #Конструктор класса принимает параметр size, который определяет размер таблицы (по умолчанию 128). 
    #Инициализирует список table, который будет хранить элементы хэш таблицы.
    def __init__(self, size=128): 
        self.size = size
        self.table = [None] * size

    def hash_function(self, key): #Определяет хэш функцию, которая принимает ключ и возвращает индекс в диапазоне от 0 до размера таблицы. 
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value): #Метод insert для добавления пары ключ-значение в таблицу. Сначала вычисляет хэш индекс для данного ключа.
        index = self.hash_function(key)

        while self.table[index] is not None: #Пока ячейка по вычисленному индексу не пустая (существует коллизия), выполняется следующий блок.            
            if self.table[index][0] == key: #Если ключ уже существует, обновляет его значение и завершает выполнение метода.
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size #Если ячейка занята другим элементом, происходит линейное пробирование: индекс увеличивается на 1 с учетом кольцевой структуры.

        self.table[index] = (key, value) #Если ячейка свободна, вставляем в неё пару ключ-значение.

    def get(self, key): #Определяет метод get, который запрашивает значение по ключу.
        index = self.hash_function(key)

        while self.table[index] is not None: #Цикл продолжает работать, пока не найдет None в таблице.
            if self.table[index][0] == key: #Если найден нужный ключ, возвращает соответствующее значение.
                return self.table[index][1]
            index = (index + 1) % self.size #Как и в методе insert, происходит линейное пробирование. Если ключ не найден, возвращает None.
        return None

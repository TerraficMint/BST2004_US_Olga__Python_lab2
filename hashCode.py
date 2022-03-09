import random
random.seed(113)

# Простое хеширование


class SimpleHash:
    def __init__(self):
        # хэш таблица из 10 эл-ов
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        # генерация хэш кода посимвольно по ключу каждого из значений
        for char in key:
            hash += ord(char)
        # остаток от деления чтобы определить место в хэш таблице
        return hash % self.MAX

# поиск элемента по ключу
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

# поиск места для элемента
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)


# l = SimpleHash()
# l['Mom'] = 'Jan 20'
# l['Dad'] = 'July 02'
# l['Timon'] = 'Sep 1'
# l['Dda'] = 'June 02'
# l.arr

# Метод цепочек


class ChainHash:
    def __init__(self):
        self.MAX = 7
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for element in self.arr[arr_index]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]


# l = SimpleHash()
# l['Mom'] = 'Jan 20'
# l['Dad'] = 'July 02'
# l['Timon'] = 'Sep 1'
# l['Dda'] = 'June 02'
# l.arr


class SemiRand:
    def __init__(self):
        # хэш таблица из 10 эл-ов
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        # генерация хэш кода посимвольно по ключу каждого из значений
        for char in key:
            hash = hash + ord(char) + (random.randint(1, 50))
        # остаток от деления чтобы определить место в хэш таблице
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # item not found so return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)


l = SemiRand()
l['Mom'] = 'Jan 20'
l['Dad'] = 'July 02'
l['Timon'] = 'Sep 1'
l['Dda'] = 'June 02'
l.arr

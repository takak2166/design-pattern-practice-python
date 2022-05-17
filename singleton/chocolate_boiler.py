class ChocolateBoiler:
    __instance = None
    __empty = True
    __boiled = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def fill(self):
        if self.is_empty():
            print("🥛と🍫を混ぜてボイラを満たす")
            self.__empty = False 
            self.__boiled = False

    def drain(self):
        if not self.is_empty() and self.is_boiled():
            print("ボイラを空にする")
            self.__empty = True

    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            print("中身を沸騰させる🔥")
            self.__boiled = True

    def is_empty(self):
        return self.__empty

    def is_boiled(self):
        return self.__boiled

if __name__ == '__main__':
    boiler1 = ChocolateBoiler()
    boiler1.fill()
    
    boiler2 = ChocolateBoiler()
    boiler2.boil()

    boiler3 = ChocolateBoiler()
    boiler3.drain()

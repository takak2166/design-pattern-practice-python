class ChocolateBoiler:
    __instance = None
    __empty = False
    __boiled = False

    def __new__(cls):
         raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        cls.__empty = True
        cls.__boiled = False
        return super().__new__(cls)
 
    @classmethod
    def get_instance(cls):
         if not cls.__instance:
             cls.__instance = cls.__internal_new__()  # ε€ζ΄
 
         return cls.__instance

    def fill(self):
        if self.is_empty():
            print("π₯γ¨π«γζ··γγ¦γγ€γ©γζΊγγ")
            self.__empty = False 
            self.__boiled = False

    def drain(self):
        if not self.is_empty() and self.is_boiled():
            print("γγ€γ©γη©Ίγ«γγ")
            self.__empty = True

    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            print("δΈ­θΊ«γζ²Έι¨°γγγπ₯")
            self.__boiled = True

    def is_empty(self):
        return self.__empty

    def is_boiled(self):
        return self.__boiled

if __name__ == '__main__':
    boiler1 = ChocolateBoiler.get_instance()
    boiler1.fill()
    
    boiler2 = ChocolateBoiler.get_instance()
    boiler2.boil()

    boiler3 = ChocolateBoiler.get_instance()
    boiler3.drain()

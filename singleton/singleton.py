class NormalSingleton:
    _instance = None

    def __init__(self, input):
        self.input = input

    @classmethod
    def get_instance(cls, input):
        if cls._instance is None:
            cls._instance = cls(input)

        return cls._instance

class SimpleSingleton:
    _instance = None

    def __init__(self, input):
        self.input = input

    def __new__(cls, input):
        if cls._instance is None:
            cls._instance = super().__new__(cls) # ここをcls(input)にすると__new__がもう一回呼び出されて無限ループ
        return cls._instance

if __name__ == '__main__':
    a = NormalSingleton.get_instance(1)
    b = NormalSingleton.get_instance(2)
    print("a.input={0}, b.input={1}".format(a.input, b.input))

    c = NormalSingleton(3) 
    b = NormalSingleton(4) 
    print("c.input={0}, b.input={1}".format(c.input, b.input))

    d = SimpleSingleton(1)
    e = SimpleSingleton(2)
    print("d.input={0}, e.input={1}".format(d.input, e.input))

    e.input = 100
    print("d.input={0}, e.input={1}".format(d.input, e.input))

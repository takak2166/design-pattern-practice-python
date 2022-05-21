from logging import raiseExceptions

# 本の内容を愚直にPythonで書き直してみた例
class NormalSingleton:
    _instance = None

    def __init__(self, input):
        self.input = input

    @classmethod
    def get_instance(cls, input):
        if cls._instance is None:
            cls._instance = cls(input)

        return cls._instance

# PythonなりのSingletonの実装
class SimpleSingleton:
    _instance = None

    def __init__(self, input):
        self.input = input

    def __new__(cls, input):
        if cls._instance is None:
            cls._instance = super().__new__(cls) # ここをcls(input)にすると__new__がもう一回呼び出されて無限ループ
        return cls._instance

# 正確な（？）Singletonの実装
class Singleton:
    _instance = None

    def __new__(cls, input):
        raise NotImplementedError('Cannot initialize via Constructor')
    
    @classmethod
    def __internal_new__(cls, input):
        cls.input = input
        return super().__new__(cls)

    @classmethod
    def get_instance(cls, input):
        if not cls._instance:
            cls._instance = cls.__internal_new__(input)  # 変更

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

    f = Singleton.get_instance(1)
    g = Singleton.get_instance(2)
    print("f.input={0}, g.input={1}".format(f.input, g.input))

    h = Singleton(3) # error!
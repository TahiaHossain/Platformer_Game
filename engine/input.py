class Key:
    def __init__(self, value):
        self.value = value


class Keys:
    ESC = Key(b'\x1b')
    SPACE = Key(b' ')
    w = Key(b'w')
    a = Key(b'a')
    s = Key(b's')
    d = Key(b'd')
    e = Key(b'e')
    f = Key(b'f')
    g = Key(b'g')
    

    LEFT = Key(100)
    UP = Key(101)
    RIGHT = Key(102)
    DOWN = Key(103)
    ENTER = Key(257)

    LMB = Key(-1000)
    RMB = Key(-1001)

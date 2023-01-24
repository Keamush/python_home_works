class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("Недопустимое имя атрибута")
        else:
            object.__getattribute__(self, key, value)


pt1 = Point(1, 2)
pt2 = Point(10, 20)

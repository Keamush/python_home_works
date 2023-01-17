class VectorGraphic:
    MAX_COORDINATE = 100
    MIN_COORDINATE = 0

    @classmethod
    def validate_coordinate(cls, coord):
        return cls.MIN_COORDINATE <= coord <= cls.MAX_COORDINATE

    @staticmethod
    def get_quadratic_form(x, y):
        return x * x + y * y

    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.validate_coordinate(x) and self.validate_coordinate(y):
            self.x = x
            self.y = y


vector_point = VectorGraphic(200, 3)
print(vector_point.x, vector_point.y)
print(VectorGraphic.get_quadratic_form(2, 3))

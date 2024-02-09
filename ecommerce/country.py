class Country:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self._cities = []

    def discount(self, discount):
        pass

    def __str__(self):
        return self.name

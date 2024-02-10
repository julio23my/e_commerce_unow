class Country:
    def __init__(self, name, code, symbol='$'):
        self.name = name
        self.code = code
        self.symbol = symbol

    def discount(self, discount):
        pass

    def __str__(self):
        return self.name


class ListCountries:
    def __init__(self):
        self.countries = []
        self.make_principal_countries()

    def add(self, country):
        if country not in self.countries:
            self.countries.append(country)

    def __str__(self):
        countries = []
        for country in self.countries:
            countries.append(str(country.name + '-' + country.code))
        return f'{[country for country in countries]}'

    def make_principal_countries(self):
        self.add(Country('Spain', 'ES', '€'))
        self.add(Country('United Kingdom', 'GB', '£'))
        self.add(Country('Italy', 'IT', '€'))
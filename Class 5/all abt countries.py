#Country 1 (India)
class India:
    def capital(self):
        print("The Indian capital is New Delhi.")
    def language(self):
        print("The Indian language is Hindi.")
    def population(self):
        print("The Indian population is approximately 1.3 billion.")
    def currency(self):
        print("The Indian currency is the Indian Rupee.")
#Country 2 (USA)
class USA:
    def capital(self):
        print("The USA capital is Washington, D.C.")
    def language(self):
        print("The Primary language in the USA is English.")
    def population(self):
        print("The USA population is approximately 331 million.")
    def currency(self):
        print("The American currency is the US Dollar.")
#Country 3 (Australia)
class Australia:
    def capital(self):
        print("The Australian capital is Canberra.")
    def language(self):
        print("The Primary language in Australia is English.")
    def population(self):
        print("The Australian population is approximately 25 million.")
    def currency(self):
        print("The Australian currency is the Australian Dollar.")
#Country 4 (Russia)
class Russia:
    def capital(self):
        print("The Russian capital is Moscow.")
    def language(self):
        print("The Primary language in Russia is Russian.")
    def population(self):
        print("The Russian population is approximately 144 million.")
    def currency(self):
        print("The Russian currency is the Russian Ruble.")
#Country 5 (Japan)
class Japan:
    def capital(self):
        print("The Japanese capital is Tokyo.")
    def language(self):
        print("The Primary language in Japan is Japanese.")
    def population(self):
        print("The Japanese population is approximately 126 million.")
    def currency(self):
        print("The Japanese currency is the Japanese Yen.")
#Object creation
India_obj = India()
USA_obj = USA()
Australia_obj = Australia()
Russia_obj = Russia()
Japan_obj = Japan()
#Calling methods for each country
for country in (India_obj, USA_obj, Australia_obj, Russia_obj, Japan_obj):
    print("\n")
    country.capital()
    country.language()
    country.population()
    country.currency()
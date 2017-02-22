# -*- coding: utf-8 -*- 

class Prefecture:

    def __init__(self, pref_name):
        self.pref_name = pref_name


class City(Prefecture):

    def __init__(self, pref_name, city_name):
        Prefecture.__init__(self, pref_name)
        self.city_name = city_name

    def show_name(self):
        print(self.city_name)

city = City('Miyagi','Ishinomaki')
city.show_name()
from src.item import Item

class MixinLog:
    '''
    Миксин для хранения и изменения раскладки клавиатуры
    '''
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        '''
        Приватный метод для хранения свойства language
        '''
        return self.__language

    def change_lang(self):
        '''
        Метод для изменения раскладки клавиатуры
        '''
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        else:
            self.__language = 'EN'
            return self.__language

class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        '''
        Добавляем аттрибуты класса Item и миксин MixinLog
        '''
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

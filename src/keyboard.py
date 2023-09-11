from src.item import Item

class MixinLog:
    '''
    Миксин для хранения и изменения раскладки клавиатуры
    '''
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        '''
        Приватный метод для хранения свойства language
        '''
        return self._language

    def change_lang(self):
        '''
        Метод для изменения раскладки клавиатуры
        '''
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'

class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        '''
        Добавляем аттрибуты класса Item и миксин MixinLog
        '''
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

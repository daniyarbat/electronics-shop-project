from src.keyboard import Keyboard, MixinLog


# тесты для MixinLog
def test_mixinlog_initial_language():
    mixin_log = MixinLog()
    assert mixin_log.language == 'EN'

def test_mixinlog_change_language():
    mixin_log = MixinLog()
    mixin_log.change_lang()
    assert mixin_log.language == 'RU'
    mixin_log.change_lang()
    assert mixin_log.language == 'EN'

# Тесты для Keyboard

def test_keyboard_initial_language():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert keyboard.language == 'EN'

def test_keyboard_change_language():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'

def test_keyboard_repr():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert repr(keyboard) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"

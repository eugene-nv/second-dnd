def modifier(characteristic):
    if characteristic == 1:
        return -5
    if characteristic in (2, 3):
        return -4
    if characteristic in (4, 5):
        return -3
    if characteristic in (6, 7):
        return -2
    if characteristic in (8, 9):
        return -1
    if characteristic in (10, 11):
        return 0
    if characteristic in (12, 13):
        return 1
    if characteristic in (14, 15):
        return 2
    if characteristic in (16, 17):
        return 3
    if characteristic in (18, 19):
        return 4
    if characteristic in (20, 21):
        return 5
    if characteristic in (22, 23):
        return 6
    if characteristic in (24, 25):
        return 7
    if characteristic in (26, 27):
        return 8
    if characteristic in (28, 29):
        return 9
    if characteristic == 30:
        return 10


def check_level(hero):
    if hero.experience <= 299:
        return 1
    if 300 <= hero.experience <= 899:
        return 2
    if 900 <= hero.experience <= 2699:
        return 3
    if 2700 <= hero.experience <= 6499:
        return 4
    if 6500 <= hero.experience <= 13999:
        return 5
    if 14000 <= hero.experience <= 22999:
        return 6
    if 23000 <= hero.experience <= 33999:
        return 7
    if 34000 <= hero.experience <= 47999:
        return 8
    if 48000 <= hero.experience <= 63999:
        return 9
    if 64000 <= hero.experience <= 84999:
        return 10
    if 85000 <= hero.experience <= 99999:
        return 11
    if 100000 <= hero.experience <= 119999:
        return 12
    if 120000 <= hero.experience <= 139999:
        return 13
    if 140000 <= hero.experience <= 164999:
        return 14
    if 165000 <= hero.experience <= 194999:
        return 15
    if 195000 <= hero.experience <= 224999:
        return 16
    if 225000 <= hero.experience <= 263999:
        return 17
    if 265000 <= hero.experience <= 304999:
        return 18
    if 305000 <= hero.experience <= 354999:
        return 19
    if 355000 <= hero.experience:
        return 20


def dice_hp(klass_char):
    if klass_char == 'Варвар':
        return 12
    if klass_char in ('Воин', 'Паладин', 'Следопыт'):
        return 10
    if klass_char in ('Бард', 'Жрец', 'Друид', 'Монах', 'Плут', 'Колдун'):
        return 8
    if klass_char in ('Чародей', 'Волшебник'):
        return 6


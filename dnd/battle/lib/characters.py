from characters.models import Character


def get_first_character_list(characters):
    character_list = []
    for c in characters:
        character_list.append((f'{c.name}', f'{c.name}'))

    return character_list


FIRST_CHARACTER = get_first_character_list(Character.objects.all())

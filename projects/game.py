full_dot = '●'
empty_dot = '○'

name = "ren"
strength = 4
intelligence = 'p'
charisma = 1

def create_character(name, strength, intelligence, charisma):
    if type(name) != str:
        message = "The character name should be a string"
    elif len(name) > 10:
        message = "The character name is too long"
    elif " " in name:
        message = "The character name should not contain spaces"    
    elif type(strength) != int or type(intelligence) != int or type(charisma) != int:
        message = "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        message = "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        message = "All stats should be no more than 4"
    elif strength + intelligence + charisma != 7:
        message = "The character should start with 7 points"
    else:
        message = f'{name}\nSTR {full_dot * strength}{empty_dot * (10 - strength)}\nINT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\nCHA {full_dot * charisma}{empty_dot * (10 - charisma)}'

    return message

character = create_character(name, strength, intelligence, charisma)
print(character)
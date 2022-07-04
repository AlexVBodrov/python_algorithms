bad = ['a', 'b', 'c' ]
good = ['good']

def bad_words_checker(text: str) -> str:
    for word in text.split():
        if word in bad:
                return 'Проверка не пройдена'
        elif word not in good:
            continue
        elif word in good:
            return 'Проверка пройдена'
    return 'Проверка не пройдена'


text_string1 = 'a f'
text_string2 = 'ab good'
text_string3 = 'a d good'
text_string4 = 'ab d bad'

assert bad_words_checker(text_string1) == 'Проверка не пройдена'
assert bad_words_checker(text_string2) == 'Проверка пройдена'
assert bad_words_checker(text_string3) == 'Проверка не пройдена'
assert bad_words_checker(text_string4) == 'Проверка не пройдена'
print('All tests => ok!!!')
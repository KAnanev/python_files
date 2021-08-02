
def length_of_last_word(string):
    fr = string.split()
    if fr:
        return len(fr[-1])
    return 0





# length_of_last_word('')
# length_of_last_word(' \t\n')
length_of_last_word('hi')
length_of_last_word('  cat')
length_of_last_word('man in black')
length_of_last_word('hello, world!')
length_of_last_word('hello, wOrLd!    ')
length_of_last_word('hello\t\nworld')








def test_length_of_last_word():
    assert length_of_last_word('') == 0
    assert length_of_last_word(' \t\n') == 0
    assert length_of_last_word('hi') == 2
    assert length_of_last_word('  cat') == 3
    assert length_of_last_word('man in black') == 5
    assert length_of_last_word('hello, world!') == 6
    assert length_of_last_word('hello, wOrLd!    ') == 6
    assert length_of_last_word('hello\t\nworld') == 5
    print('Тест пройден')

test_length_of_last_word()
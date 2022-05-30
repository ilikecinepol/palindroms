'''Программа для поиска полиндромов'''
import sys


def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            # loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as er:
        print('Ошибка чтения')
        sys.exit(1)


def is_palindrome(word):
    return True if len(word) > 1 and word == word[::-1] else False


# Отыскать палинграммы словарных пар
def find_paligrams(word_list):
    # Отыскать палинграммы в словаре
    palin_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        reverse_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reverse_word[:end - i] and reverse_word[end - i:] in word_list:
                    palin_list.append((word, reverse_word[end - i:]))
                if word[:i] == reverse_word[end - i:] and reverse_word[:end - i] in word_list:
                    palin_list.append((reverse_word[:end - i], word))
        print(palin_list)
    return palin_list


if __name__ == '__main__':
    file = load('RUS.txt')
    poli_words = []
    for word in file:
        if is_palindrome(word):
            poli_words.append(word)
    # print(poli_words)
    print(find_paligrams(file))

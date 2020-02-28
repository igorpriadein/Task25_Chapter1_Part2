# Напишите функцию которая находит самою длинную слово в строке.

word_list = input('input your word')

def find_longest_word(word_list):
    longest_word =  max(word_list, key=len)
    print (longest_word)

find_longest_word(word_list)
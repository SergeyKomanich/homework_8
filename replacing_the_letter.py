"""
 Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.

Понадобятся: срезы и функции replace(), rfind(), find().
"""
# he has three children, she is always busy around the house

string = input("Enter the sentence: ")
string = string.replace('h', 'H', string.count('h') - 1)
new_string = string.replace('H', 'h', 1)
print(new_string)


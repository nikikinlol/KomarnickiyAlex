# numbers = []
# strings = []
# names = ["John", "Eric", "Jessica"]
#
# # write your code here
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
#
# strings.append("hello")
# strings.append("world")
#
# second_name = names[1]
#
# # this code should write out the filled arrays and the second name in the names list (Eric).
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)

# x = object()
# y = object()
#
# x_list = [x] * 10
# y_list = [y] * 10
# big_list = x_list + y_list
#
# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))
#
# # testing code
# if x_list.count(x) == 10 and y_list.count(y) == 10:
#     print("Almost there...")
# if big_list.count(x) == 10 and big_list.count(y) == 10:
#     print("Great!")

# Exercise 4
data = ("nikikinlol", "Ніканоров", 53.44)
format_string = "Hello"
#
print("Hello %s %s. Ваш баланс становить $%s." %(data[0], data[1], data[2]))
s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

s = " Gorilesascakeeeeeee"
# Кількість рядків тепер 20
print("Length of s = %d" % len(s))

# Перше входження рядка "а" в "Goriles as cake"
print("The first occurrence of the letter a = %d" % s.index("a"))

# Кількість рядків "а" в "Goriles as cake"
print("a occurs %d times" % s.count("a"))

# Нарізаємо рядки
# Перші п'ять строк'
print("The first five characters are '%s'" % s[:5])
#Від 5 до 10
print("The next five characters are '%s'" % s[5:10])
#Дванадцятий символ
print("The thirteenth character is '%s'" % s[12])
#Від 0 кожен четвертий символ
print("The characters with odd index are '%s'" %s[0::4])
#Останні п'ять символів, але тут вже рахується з кінця не від 0 а від -1
print("The last five characters are '%s'" % s[-5:])

#Перевод у нижній регістр
print("String in uppercase: %s" % s.lower())

#Перевод у верхній регістр
print("String in lowercase: %s" % s.upper())

# Якщо починається з Gor
if s.startswith(" Gor"):
    print("String starts with 'Gor'. Good!")

# Якщо закінчуєтсья на cake
if s.endswith("eeee"):
    print("String ends with 'eeee!'. Good!")

# Розділяє строку на масив по заданому в split елементу (наприклад " ", "," або люба інша строка"
# Якщо не було передано елементів розділителів то розділяє строку орієнтуючись по пробілам
# Якщо не передано розділювача і строка не передбачає пробілів то повертає масив з цілою строкою
print("Split the words of the string: %s" % s.split())
#                                           PR3
# change this code
number = 20
second_number = 0 > 1
first_array = [1,22,32]
second_array = [1,2]

if number > 15:
    print("1")
#Тепер масив не пустий, тому повертає True
if first_array:
    print("2")
#Кількість елементів в масиві
if len(second_array) == 2:
    print("3")
#Кількість елементів масиву first_array та масиву second_array в суммі
if len(first_array) + len(second_array) == 5:
    print("4")
#Якщо first_array == true і перший (нульовий) елемент first_array рівний 1
if first_array and first_array[0] == 1:
    print("5")
#Якщо second_name рівне false
if not second_number:
    print("6")
#                                       PR4
#Функція повертає строки
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", \
           "Allowing programmers to share and connect code together"
#У функцію передається параметр benefit, вона поверне строку в якій %s буде замінено на benefit
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

#Функція створює внутрішню змінну і одразу викликає list_benefits яка повертає строки
#Перебирає масив строк list_of_benefits за допомогою for in
#І на кожній ітерації буде повертати у print() результат роботи build_sentence(benefit)
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

# # 1)დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს და დააბრუნებს ამ რიცხვებს შორის 
# # შესრულებული არითმეტიკული ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება).
# x = eval(input("Please enter first number..."))
# y = eval(input("Please enter second number..."))
# print(f"{x} + {y} = {x + y}")
# print(f"{x} - {y} = {x - y}")
# print(f"{x} * {y} = {x * y}")
# print(f"{x} / {y} = {x / y}")
# print(f"{x} ** {y} = {x ** y}")
# print(f"{x} // {y} = {x // y}")
# print(f"{x} % {y} = {x % y}")

# # 2)დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი 
# # დიაგონალის სიგრძე.
# a = eval(input("Please enter length of the first diagonal of rhombus..."))
# b = eval(input("Please enter length of the second diagonal of rhombus..."))
# c =  a * b / 2
# print("Rhombus aea =", c)

# # 3)მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, 
# # მილიმეტრებში, მილში.
# m = eval(input("Please enter meter volume..."))
# u_sm = (m * 100)
# u_dm = (m * 10)
# u_mm = (m * 1000)
# u_ml = (m * 0.00062137)
# print(m, "Meter = ", u_sm, "Centimeter")
# print(m, "Meter = ", u_dm, "Decimeter")
# print(m, "Meter = ", u_mm, "Millimeter")
# print(m, "Meter = ", u_ml, "Mile")

# # 4)დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის 
# # სიმაღლისა და ფუძის მნიშვნელობა.
# a = eval(input("Please enter triangle height..."))
# b = eval(input("Please enter triangle base..."))
# c = a * b / 2
# print("triangle area =", c) 


# # 1)შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს
# # თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.
# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
# a = eval(input("enter a number..."))
# if a in num_list:
#     print(f"the number {a} is in list")
# else:
#     print(f"the number {a} is not in list")

# # 2)დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი 
# # ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.
# a = int(input("Please enter an integer:..."))
# if a % 2 == 0:
#     print(f"The number {a} is 'even'")
# else:
#     print(f"The number {a} is 'odd'")

# # 3)შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ 
# # ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"
# #Same
# st1 = "xy"
# st2 = "xy"
# if st1 is st2:
#     print("Same object")
# else: 
#     print("Different object")
# #Different
# st1 = "xyz"
# st2 = "xy"
# if st1 is st2:
#     print("Same object")
# else: 
#     print("Different object")

# # 4)შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
# # თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი 
# # "More than list elements"; თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
# # სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
# # რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.
# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
# a = eval(input("Please enter number..."))
# if a > num_list[2] and a < num_list[7]:
#     print("More than list elements")
# elif a == num_list[5]:
#     print("Equal")
# else:
#     print("None of the conditions were met")


# # 1)დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების 
# # ჯამს.
# # კომენტარი: ჯამი კეთდება n-რიცხვამდე და მასში არ შედის n რიცხვი. მაგ: თუ n = 4 ჯამი იქნება 1+2+3=6.
# # თუ აქ გვენდომებოდა ჯამი n-ის ჩათვლით, მაშინ დავწერდით stop = n+1 და არა stop = n
# n = int(input("Please enter your number "))
# start = 1
# stop = n
# total = sum(range(start, stop))
# print("the sum of numbers from 1 to", n, "=", total)

# # 2)დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ 
# # რევესრულად დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1
# num = int(input("Please enter your number "))
# while True:
#     if num == 0:
#         break
#     print (num, end = " ")
#     num -= 1

# # 3)დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ 
# # განსაზღვრული რიცხვი.  როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.
# # კომენტარი: თუ მოგვინდებოდა რთული თამაშის შექმნა, სადაც თამაში არ მოგვცემდა მინიშნეებს არის მეორე ვარიანტიც.
# from random import randint

# num = randint(1, 1000)
# i = 0

# print("Was guessed a number between 1 and 1000, guess it !\n")

# while True:
#    i +=1
#    guess = int(input(f"Step {i}. Your guess:  "))
#    if guess == num:
#       print(f"You guessed a number! it was {num}.")
#       break
#    elif guess > num:
#       print("Too great")
#    else:
#       print("Too less")

#       print()

# print("\nGame Over!")

# # 4) დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი  total_sum = 0, 
# # შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. ეს პროცესი გაგრძელდეს იქამდე 
# # სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება  შეყვანილი დადებითი რიცხვების ჯამი.
# total_sum = 0

# x = int(input(f"enter number:  "))
# while True:
#    if x > 0:
#       total_sum = total_sum + x
#       x = int(input(f"enter number:  "))
#    elif  x < 0:
#       print("Wrong number")
#       break
#    elif x== 0:
#       print("Total sum of numbers you entered is:  ", total_sum)
#       break


# # 1)დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.
# text = input("Please enter your text?")
# print(text.encode("utf-8"))

# # 2)დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო 
# # გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს სიტყვა 
# # "python", ჩაანაცვლეთ "Python"-ით.
# text = input("Please enter your text?")
# text = text.strip()
# text = text.lower()
# text = text + " Python"
# text = text.replace("python", "Phyton")
# print(text)

# # 3)დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, 
# # რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.
# text = input("Please enter your text ")
# x = int(len(text) / 2)
# print(text[0:x])

# # 4) დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება. 
# # სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები
# #  ('!', '~', '#', '$' და ა.შ.)
# import string
# text = input ("Please enter your text ")
# digit = any(char in string.digits for char in text) 
# letter = any(char in string.ascii_letters for char in text)
# digit_letter = string.ascii_letters + string.digits

# validation = all(char in digit_letter for char in text)
# if validation and digit and letter:
#     print("text is valid")
# else:
#     print("text not valid")

# # 5)დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და 
# # შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.
# text = input("Please enter your text ")
# print(text,"\n")
# text = text.encode("utf-32")
# print(text,"\n")
# text = text.decode("utf-32")
# print(text,"\n")


# #1)დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 
# # 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს 
# # შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
# # მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:
# # a – append
# # r – remove
# # e – exit
# # მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.

# user_list=[]

# while True:
#     ask_user = input("enter 'a' append\n'r' for remove\n'e' for exit" + 
#                      "and number separated by space").split
    
#     command = ask_user[0]

#     if command == "a":    
#        number = eval(ask_user[1])   
#        user_list.appened(number)  
#        print(user_list)

#     elif command == "r":    
#        number = eval(ask_user[1]) 
#        if number in user_list:
#           user_list.remove(number)
#        else: 
#           print(f"{number} not in {user_list}")
#        print(user_list) 

#     elif command == "e":
#        print(user_list)
#        break
#     else:
#        print("Invalid command")

# # 2)დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს 
# # შემდეგ ნაბიჯებს:
# # a. დაბეჭდავს 210-ის ინდექსს;
# # b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
# # c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
# # d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის 4
# # მნიშნველობა და დაბეჭდეთ ორივე სია.
# my_list = [43, '22', 12, 66, 210, ["hi"]]
# print("index of 210 is", my_list.index(210))
# my_list.append("hello")
# del my_list[2]

# print(my_list)

# my_list_2 = my_list.copy()

# for i in range(4):
#     poped_element = my_list_2.pop()

# print("my_list is:", my_list)
# print("my_list_2 is:", my_list_2)

# 3)დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს 
# თუ არა "(123) 456-789" ფორმატს, თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში 
# გამოიტანეთ "Invalid format" ტექსტი.

# import re
# input = input("Enter your number")
# pattern = r"^[(.]{1,1}+[0-9.]{3,3}+\){1,1}+\ {1,1}+[0-9.]{3,3}+\-+[0-9.]{3,3}$"
# if (re.match(pattern, input)) is None:
#     print("Invalid format")
# else:
#     print("number is",input)


# import re
# input1 = input("Enter your number")
# pattern = r"\(\d{3}\)\s\d{3}-\d{3}" #იგივე r"\([0-9]{3}\)\s[0-9]{3}-[0-9]{3}"
# if (re.match(pattern, input1)) is None:
#     print("Invalid format")
# else:
#     print("number is",input1)



#     user_list = []
# while True:
#     ask_user = input("enter "a" for append\n"r" for remove\n"e" for exit" + "and number separated by space").split()

#     command = ask_user[0]
#     if command == "a":
#        number = eval(ask_user[1])
#        user_list.appened(number)
#        print(user_list)
#     elif command =="r":
#        number = eval(ask_user[1])
#     if number in user_list:
#         user_list.remove(number)
#     print(user_list)
#     elif command == "e":
#     print(user_list)
#     break


# # 1)დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.
# def fibonacci(n):
#   if n in (1, 2):
#     return 1
  
#   return fibonacci(int(n) - 1) + fibonacci(int(n) - 2)

# n = input("Enter number please: ")
# res = fibonacci(n)
# print(n, "for fibonacci =", res)

# for i in range(1, int(n) + 1):
#   print(fibonacci(i), end=" ")

# # 2)დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები 
# # ანაგრამები. (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების 
# # გადაადგილებით). მაგ.: race და care ანაგრამებია.
# string1 = input("Enter your first word: ")
# string2 = input("enter your second word: ")
# def checkAnagram(string1, string2): 
#     string1 = string1.lower()
#     string2 = string2.lower()
#     if(len(string1) != len(string2)):
#      print("Not Anagram\n")
#     else:
#         sortString1 = sorted(string1)
#         sortString2 = sorted(string2)
#         if(sortString1 == sortString2):
#           print("Are Anagram\n")
#         else:
#           print("Not Anagram\n")
# checkAnagram(string1, string2)

# # 3)დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
# def factorial(number):
#   if int(number) < 2:
#    return 1
  
#   return int(number) * factorial(int(number) - 1)  

# num = input("enter number: ")
# result = factorial(num)
# print(f"{num}! = {factorial(num)}")

# # 4)დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. 
# # ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი 
# # რაოდენობა.
# str = input("Enter word please: ").lower()
# symbol = input("enter symbol please: ").lower()

# def count_symbol(str, symbol):
#     result = str.count(symbol)
#     return (f"ammount of symbol {symbol} in word {str} is: {result}")
# print(count_symbol(str, symbol))


# # 1)შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს რიცხვს 
# # პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.
# # ვარიანტი1
# list = [10, 20, 30, 40]
# number = int(input("Enter number"))
# list.append(number)
# print(list)
      
# # 2)დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
# # პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].
# list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# def sum_list(list):
#     sum = 0
#     for i in range(len(list)):
#         sum += list[i]
#     return sum
# sum = sum_list(list)
# print(sum)

# # 3)შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ 
# # #ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას
# gl_str = "Global"
# def my_func():
#     gl_str = "Local"
#     return gl_str

# print(my_func())

# # 4)რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს 
# # ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).
# def sum_of_digit(n):
#     if n == 0:
#         return 0
#     return (n % 10 + sum_of_digit(int(n/10)))
 
# num = int(input("Enter number: "))
# result = sum_of_digit(num)
# print("Sum of digits of",num,"is", result)

# # 5)რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს 
# # მის შებრუნებულ (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)
# text = input("Enter the text: ")
# def reversed_string(text):
#     if len(text) == 1:
#         return text
#     return reversed_string(text[1:]) + text[:1]

# print(reversed_string(text))


# # 1)დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის 
# # გამოყენებით დააჯგუფეთ სიების ელემენტები.
# # params: [1, 2, 3], ['a', 'b', 'c']  
# # outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

# # წინასწარ მოცემული პარამეტრების შემთხვევაში:
# arr1 = [1, 2, 3]
# arr2 = ["a", "b", "c"]
# print(list(zip(arr1, arr2)))

# # Input-ის შემთხვევაში:
# arr1 = input("enter numbers with space  ").split()
# arr2 = input("enter letters with space  ").split()
# if(len(arr1) == len(arr2)):
#    print(list(zip(arr1, arr2)))
# else:
#    print("lengs of lists are different")

# 2) დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. 
#ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
# params:[1, 2, 3, 4, 5] 
# output: 120

# from functools import reduce
# try:
#    numbers = list(map(eval,(input("Insert numbers: ").split())))
#    result = reduce(lambda x, y: x * y, numbers)
#    print(result)
# except NameError:
#    print("Not a valid choice! Try again")
# except SyntaxError:
#    print("Not a valid choice! Try again")
# except TypeError:
#    print("Not a valid choice! Try again")

##ვარიანტი 2
# from functools import reduce

# def multiplay(arr):
#  try:
#   for i in arr:
#    if type(i) != int and type(i) != float:
#     raise TypeError("incorrect type")  #-->გამოვიწვიე შეცდომა ჩემით.
   
#    product = reduce(lambda x, y: x * y, arr)
#    return product
#  except Exception as e:
#   print(e)

# #==============
# nums = [1, 2, 3, 4, 5]
# result = multiplay(nums)
# print(result)

##ვარიანტი 3 პაატა
# from functools import reduce

# def multiplay(arr):
#  arr = list(filter(lambda x: type(x) == int or type(x) == float, arr))
#  return reduce (lambda x, y: x * y, arr)


# #==============
# try:
#  nums = [1, 2, 3, 4, 5]
#  result = multiplay(nums)
#  print(result)
# except NameError as e:
#  print("name error")

# 3)დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

# N = list(map(eval,(input("Insert numbers: ").split())))
# evens = filter(lambda x: x % 2 != 0, N)

# print(*evens)

##ვარიანტი 2
# arr = [12, 25, 69, 14, 33, 37, 44]
# odds = list(filter(lambda x: x % 2 ==1, arr))
# print(odds)

# list1 = input("enter text ").split()
# list2 = input("enter string ")
# try:
#  A = filter(lambda x: x.endswith((list2)), list1)
#  print("Element of list that ends with entered sting:")
#  print(*A)
# except TypeError:
#  print("Not a valid choice! Try again")
# except NameError:
#  print("Not a valid choice! Try again")
# except SyntaxError:
#  print("Not a valid choice! Try again")

## ვარიანტი 2 
# def ends_with_subwords(str_arr, ending):
#     try:
#         return(list(filter(lambda x: x.endswith(ending), str_arr)))
#     except TypeError as e:
#         print("type error")
#     except AttributeError as e:
#         print("atribut error")

# #===========
# words = ["hello", "world", "coding"]
# end_words = "ing"

# result = ends_with_subwords(words, end_words)

# print(result)


# 1)დავალება
# import requests

# def get_products():
#   try:
#     api_url = "https://fakestoreapi.com/products"
#     response = requests.get(api_url)

#     # print(response)
#     print(response.status_code,"\n")
#     # print(response.text)

#     if response.status_code != 200:
#       print(f"ERROR: can't get data. Status {response.status_code}")
#       return False
    
#     return response.json()
#   except requests.exceptions.HTTPError as http_err:
#     print(f"ERROR: {http_err}")
#   except requests.exceptions.ConnectionError as con_err:
#     print(f"Connectio error: {con_err}")
#   except Exception as err:
#     print("Something wrong! {err}")


# def parese_data():
#   products = get_products()

#   products_price = []
#   products_rating = []
#   products_category = set()
#   men_women = {'men': [], 'women': []}

#   print(products[0].keys(), "\n")

#   for product in  products:
#     products_price.append({'id': product['id'], 'price': product['price']})
#     products_rating.append({'id': product['id'], 'rating': product['rating']})
#     products_category.add(product['category'])

#     if 'Women' in product['title'].title():
#       men_women['women'].append(product['title'])
#     elif 'Men' in product['title'].title():
#       men_women['men'].append(product['title'])
  
#   print(products_price, "\n")
#   print(products_rating, "\n")
#   print(products_category, "\n\n")

#   print(men_women['men'], "\n")
#   print(men_women['women'], "\n")


# parese_data()


##1)დავალება
# my_dict = {
#   "students": [
#     {"id": 20, "name": "giorgi", "age": 25},
#     {"id": 25, "name": "giorgi", "age": 23},
#     {"id": 100, "name": "nika", "age": 22},
#     {"id": 56, "name": "nika", "age": 25},
#     {"id": 1232, "name": "dato", "age": 22},
#     {"id": 846723, "name": "archili", "age": 32}
#   ],
#   "subjects": [
#     {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
#     {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
#     {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
#     {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
#     {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
#   ]
# }
# print("Student IDs are: ")
# for student in my_dict['students']:
#   st_id = student.get('id')
#   print(st_id)

# print("")

# selected_id = int(input("please enter student's ID from 20, 25, 100, 56, 1232 or 846723:  "))
# print("")

# for student in my_dict['students']:
#     if student['id'] == selected_id:
#         print(f"Student's Details/information:")
#         print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

#         print("\ngrades by Subjects:")
#         for subject in my_dict['subjects']:
#             grade = subject['grades'].get(str(selected_id))
#             print(f"subject: {subject['name']}, grade: {grade}")
        
#         break
# else:
#     print(f"No student found with ID {selected_id}")

#2
# my_dict = {
#   "students": [
#     {"id": 20, "name": "giorgi", "age": 25},
#     {"id": 25, "name": "giorgi", "age": 23},
#     {"id": 100, "name": "nika", "age": 22},
#     {"id": 56, "name": "nika", "age": 25},
#     {"id": 1232, "name": "dato", "age": 22},
#     {"id": 846723, "name": "archili", "age": 32}
#   ],
#   "subjects": [
#     {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
#     {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
#     {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
#     {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
#     {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
#   ]
# }
# print("Student IDs are: ")
# for student in my_dict['students']:
#   st_id = student.get('id')
#   print(st_id)

# print("")

# selected_id = int(input("please enter student's ID from 20, 25, 100, 56, 1232 or 846723:  "))
# print("")

# for student in my_dict['students']:
#     if student['id'] == selected_id:
#         print(f"Student's Details/information:")
#         print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

#         print("\ngrades by Subjects:")
#         for subject in my_dict['subjects']:
#             grade = subject['grades'].get(str(selected_id))
#             print(f"subject: {subject['name']}, grade: {grade}")
        
#         break
# else:
#     print(f"No student found with ID {selected_id}")


##დავალება
# chess_players = [
#   {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
#   {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
#   {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
#   {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
#   {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
#   {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
#   {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
#   {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
#   {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
# ]

# import json

# def create_json_file(path, file_name, data):
#     file_path = f"{path}/{file_name}.json"

#     try:
#         with open(file_path, mode='x', encoding='utf-8') as file:
#             json.dump(data, file, indent=4)  # Write JSON data to the file with indentation
#         print(f"File '{file_path}' created successfully!")
#     except FileExistsError:
#         print(f"File '{file_path}' already exists")
#         print("Continue working...\n")

#     return file_path

# file_path = create_json_file(".", "chess_players", chess_players)

# def read_json_file(path):
#     with open(path, mode='r', encoding='utf-8') as file:
#         data = json.load(file)
#         print("JSON data read successfully:")
#         print(data)
#         return data
# data = read_json_file("chess_players.json")

# import json

# def update_json_file(path, json_data):
#     with open(path, mode='w', encoding='utf-8') as file:
#         json.dump(json_data, file)
#     print(f"File '{path}' updated successfully!")

    
# def update_json_file(path, additional_data):
#     for player in additional_data:
#         chess_players.append(player)
    
#     with open(path, mode='w', encoding='utf-8') as file:
#         json.dump(chess_players, file, indent=4)
    
#     print(f"File '{path}' updated successfully!")

# additional_data = [
#     {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#     {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
# update_json_file("chess_players.json", additional_data)
# print()

# updated_data = read_json_file("chess_players.json")


# შექმენით csv ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:
# id,name,age,grade,subject_name,marks
# 1.დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას 
# (id,name,age,grade,subject_name,marks) და თქვენ სტუდენტს დაამატებთ csv ფაილში.
# 2.დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული 
# სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.
# 3.დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. 
# მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს და განახლებულ ქულას.

# import os, csv   

# def create_csv_file(path, csv_file):
#   file_path = f"{path}/{csv_file}.csv"

#   try:
#       os.mkdir(path)
#   except FileExistsError:
#       ...

#   try:
#       with open (file_path, mode='x', encoding='utf-8') as file:
#           ...
#   except FileExistsError:
#       print(f"File '{file_path}' exists, Continue working...\n")

#   return file_path

# def create_csv_data():
#     data = [
#         ['id', 'name', 'age', 'grade', 'subject_name', 'marks']
#     ]
#     id = 1

#     while True:
#         name = input("Name [Ender -- exit]: ")
        
#         if not name:
#             print()
#             break

#         age = int(eval(input("Age: ")))
#         grade = input("Grade: ")
#         subject_name = input("Subject_name: ")
#         marks = int(eval(input("Marks: ")))
        

#         data.append([id, name, age, grade, subject_name, marks])

#         id += 1

#         print(f"\n{data}\n")

#     return data


# def write_data_into_csv_file(path, csv_data):
#     with open(path, mode='w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)

#         writer.writerows(csv_data)



# def read_data(path, student_name=''):
#     with open(path, mode='r', encoding='utf-8') as file:
#         reader = list(csv.reader(file))

#         if not student_name:
#             return reader
        
#         st_row = [['id', 'name', 'age', 'grade', 'subject_name', 'marks']]
    

#     for row in reader:
#         if row[1] == student_name:
#             st_row.append(row)

#     return st_row

# def append_data(path, row_data):
#     data = read_data(path)
#     row_data.insert(0, int(data[-1][0]) + 1)

#     with open(path, mode='a', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)

#         writer.writerow(row_data)


# def update_data(path, id, subject_name, mark):
#     data = read_data(path)

#     for row in data[1:]:
#         if int(row[0]) == id and row[4] == subject_name:
#             row[3] = mark
#             break
#     else:
#         print("can't update")

#     write_data_into_csv_file(path, data)


#==================
# path = 'file'
# file_name = 'hw_15'

# file_path = create_csv_file(path, file_name)


# data = create_csv_data()
# print(data)

# write_data_into_csv_file(file_path, data)

# file_content = read_data(file_path)
# print(file_content)

# file_content = read_data(file_path, 'Paata')
# print(file_content)

# row_data = ['Tengizi', 26, 'B', 'Math', 82]
# append_data(file_path, row_data)

# id = 2
# subject_name = 'Physic'
# mark = 22
# update_data(file_path, id, subject_name, mark)
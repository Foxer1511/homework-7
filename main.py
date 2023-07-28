#Завдання 1.
#Написати рекурсивну функцію знаходження ступеня числа.

# def find_degree(number, degree):
#     if degree <= 1:
#         return number
#
#     return number * find_degree(number, degree - 1)
#
# print (find_degree(4, 4))
#
# #find_degree(4, 4) -> 4 * find_degree(4, 4-1)
# #find_degree(4, 3) -> 4 * find_degree(4, 3-1)
# #find_degree(4, 2) -> 4 * find_degree(4, 2-1)
# #find_degree(4, 1) -> 4

# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)


def print_stars(n):

    if n <= 0:
        return
    else:
        print("*", end="")
        print_stars(n - 1)
num_stars = int(input("Enter number of stars "))
try:
    print_stars(num_stars)
except Exception as e:
    print()
    print(e)

# #n_stars(star, 5) -> star * n_stars(star, 5-1)
# #n_stars(star, 4) -> star * n_stars(star, 4-1)
# #n_stars(star, 3) -> star * n_stars(star, 3-1)
# #n_stars(star, 2) -> star * n_stars(star, 2-1)
# #n_stars(star, 1) -> star

#v2

# N = int(input("Enter number of stars "))
# star = "*"
#
# def n_star(star, N):
#     if N > 0:
#         result = print(star, end="") + n_star(star, N - 1)
#         print(result)
#     else:
#         result = 0
# try:
#     n_star(star, N)
# except Exception as e:
#     print()
#     print(e)

#Завдання 3
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.


# a = int(input("Enter a number "))
# b = int(input("Enter b number "))
#
# if a > b:
#     a, b = b, a
#
# def ab_sum(a, b):
#     if b == a:
#         return a
#
#     return a + ab_sum(a + 1, b)
# try:
#     print(ab_sum(a, b))
# except Exception as e:
#     print()
#     print(e)

# #ab_sum(2, 5) -> 4 + ab_sum(4 + 1, 5)
# #ab_sum(3, 5) -> 3 + ab_sum(3 + 1, 5)
# #ab_sum(4, 5) -> 2 + ab_sum(2 + 1, 5)
# #ab_sum(5, 5) -> 2
#!!!

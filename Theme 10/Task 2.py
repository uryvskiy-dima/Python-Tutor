"""
Условие
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""


print(len(set(input().split()).intersection(set(input().split()))))

# Два велосипеда
# Все языки	OpenJDK Java 11
# Ограничение времени	0.5 секунд	0.7 секунд
# Ограничение памяти	121Mb	121Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность). В процессе накопления Вася не вынимает деньги из копилки.

# У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.

# Ваша задача — по заданной стоимости велосипеда определить

# первый день, в которой Вася смог бы купить один велосипед,
# и первый день, в который Вася смог бы купить два велосипеда.
# Подсказка: решение должно работать за O(log n).

# Формат ввода
# В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.

# В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.

# В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.

# Формат вывода
# Нужно вывести два числа — номера дней по условию задачи.

# Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.


# Пример 1
# 6
# 1 2 4 4 6 8
# 3

# 3 5


# Пример 2
# 6
# 1 2 4 4 4 4
# 3

# 3 -1


# Пример 3
# 6
# 1 2 4 4 4 4
# 10

# -1 -1
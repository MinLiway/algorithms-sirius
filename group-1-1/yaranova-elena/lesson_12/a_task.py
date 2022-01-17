# A. Построить список смежности

# Для очень большого числа ориентированных графов необходимо преобразовать их список рёбер 
# в список смежности. Необходимо написать программу, которая по списку рёбер графа будет строить его список смежности.

# Аргументы функции
# В первом дано число вершин n (1 ≤ n ≤ 100) 
# Во втором - число ребер m (1 ≤ m ≤ n(n-1)). 
# В третьем - список ребер в виде пар вершин (u,v), если ребро ведет от u к v.

# Формат вывода
# Выведите информацию о рёбрах, исходящих из каждой вершины.

# В строке i надо написать число рёбер, исходящих из вершины i, а затем перечислить вершины, 
# в которые ведут эти рёбра –— в порядке возрастания их номеров.

def solution(n, m, edges):
    pass

def test(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')

test(
    solution(5, 3, [[1, 3], [2, 3], [5, 2]]), 
    [[1, 3], [1, 3], [0], [0], [1, 2]]
)

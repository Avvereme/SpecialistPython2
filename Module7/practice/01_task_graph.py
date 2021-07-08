graph = [
[1], # 0
[0, 2, 4], # 1
[1, 3, 4], # 2
[2], # 3
[1, 2, 5, 7], # 4
[4], # 5
[4, 7, 8], # 6
[6], # 7
[6], # 8
[10], # 9
[9], # 10
]

visited = [False] * (len(graph))
prev = [None] * (len(graph))
finish = 6


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


dfs(finish)

print(visited)
Points = [1, 3, 9]
for a in Points:
    if a == True:
        print(f"из {a} можно добраться до финиша")
    else:
        print(f'Из {a} нельзя добравться до финиша')



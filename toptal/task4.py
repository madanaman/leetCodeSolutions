from collections import deque


def addEdge(v, w, adjency_matrix):
    if adjency_matrix.get(v) is None:
        adjency_matrix[v] = []
    if adjency_matrix.get(w) is None:
        adjency_matrix[w] = []
    if w > v:
        adjency_matrix[v].append(w)
    if v > w:
        adjency_matrix[w].append(v)


def reach(s, d, adjency_matrix):
    print(adjency_matrix)
    if s not in adjency_matrix.keys():
        return False
    if s == d:
        return True
    visited = [False for i in range(d)]
    queue = deque()
    visited[s] = True
    queue.append(s)
    while len(queue) > 0:
        s = queue.popleft()
        print(s)
        for i in adjency_matrix[s]:
            if i == d:
                if False in visited:
                    continue
                return True
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return False


def solution(N, A, B):
    # write your code in Python 3.6
    adjency_matrix = {}
    for i in range(0, len(A)):
        addEdge(A[i], B[i], adjency_matrix)
    if reach(1, N, adjency_matrix):
        return True
    else:
        return False


# 4, [1, 2, 1, 3], [2, 4, 3, 4]
N = 4
A = [1, 2, 1, 3]
B = [2, 4, 3, 4]
print(solution(N, A, B))
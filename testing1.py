def Solution(startState, endState, N, deadlock):
    first_solved = False
    second_solved = False
    third_solved = False
    fourth_solved = False
    while not first_solved or not second_solved and not third_solved and not fourth_solved:
        if startState[0] == endState[0]:
            first_solved=True
        if startState[1] == endState[1]:
            first_solved=True
        if startState[2] == endState[2]:
            first_solved=True
        if startState[3] == endState[3]:
            first_solved=True
    return 0



startState = input()
endState = input()
N= int(input())
deadlock = []
for i in range(N):
    deadlock.append(input())
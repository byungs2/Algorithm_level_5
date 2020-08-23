arrow = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]

def expand_arrow(arrow):
    arrow2 = []
    for i in arrow:
        arrow2.append(i)
        arrow2.append(i)
    return arrow2

def draw_line(arrow):
    position = [(0, 0)]
    init_nx = 0
    init_ny = 0
    line = []
    line_set = set()
    for i in arrow:
        if i == 6:
            init_nx = init_nx -1
            position.append((init_nx , init_ny))
        elif i == 1:
            init_nx = init_nx +1
            init_ny = init_ny +1
            position.append((init_nx, init_ny))
        elif i == 2:
            init_nx = init_nx +1
            position.append((init_nx, init_ny))
        elif i == 3:
            init_nx = init_nx +1
            init_ny = init_ny -1
            position.append((init_nx, init_ny))
        elif i == 4:
            init_ny = init_ny -1
            position.append((init_nx, init_ny))
        elif i == 5:
            init_nx = init_nx -1
            init_ny = init_ny -1
            position.append((init_nx, init_ny))
        elif i == 7:
            init_nx = init_nx -1
            init_ny = init_ny +1
            position.append((init_nx, init_ny))
        elif i == 0:
            init_ny = init_ny + 1
            position.append((init_nx, init_ny))
    for index, i in enumerate(position):
        if index < len(position) - 1:
            line_set = {position[index], position[index +1]}
            line.append(line_set)
    return position, line

def solution(arrow):
    room_count = 0
    line_index = []
    position = draw_line(expand_arrow(arrow))[0]
    position_set = list(set(position))
    line = draw_line(expand_arrow(arrow))[1]
    for i in line:
        if line_index.count(i) == 0:
            line_index.append(i)
    line_count = [line.count(i) for i in line_index]
    pointer = [position.count(i) for i in position_set]

    for i in pointer:
        room_count = room_count + (i-1)
    for i in line_count:
        room_count = room_count - (i-1)
    answer = room_count
    return answer

print(solution(arrow))
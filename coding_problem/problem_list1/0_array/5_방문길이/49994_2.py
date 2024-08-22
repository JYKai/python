def solution(dirs):
    answer = 0
    coords = [0, 0]
    visited = set()
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for d in dirs:
        new_x, new_y = coords[0] + move[d][0], coords[1] + move[d][1]
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            new_coords = [new_x, new_y]
            path = tuple(coords + new_coords)
            r_path = tuple(new_coords + coords)
            if path not in visited:
                visited.add(path)
                visited.add(r_path)
                answer += 1
            coords = new_coords

    return answer

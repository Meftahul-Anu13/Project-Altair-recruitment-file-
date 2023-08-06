def process_instructions(instructions, grid_size):
    i=0 
    j=0
    k = 0 #for 3d xi+yj+k vector 
    x, y = 0, 0


    directions = ['N', 'E', 'S', 'W']
    for s in instructions:
        if s == 'F':
            if directions[k] == 'N':
                j += 1
            elif directions[k] == 'E':
                i += 1
            elif directions[k] == 'S':
                j -= 1
            elif directions[k] == 'W':
                i -= 1
        elif s == 'R':
            k = (k + 1) % 4
        elif s == 'L':
            k = (k - 1 + 4) % 4
        
      
        if i < 0:
            x = 0
        elif i >= grid_size[0]:
            x = grid_size[0] - 1
        else:
            x = i

        if j < 0:
            y = 0
        elif j >= grid_size[1]:
            y = grid_size[1] - 1
        else:
            y = j

    direction = directions[k]
    return x, y, direction


instructions = input()
x1, y1 = map(int, input().split())
grid_size = (x1, y1)
result = process_instructions(instructions, grid_size)
print(result[0], result[1], result[2])

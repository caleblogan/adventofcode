# Squares with Three Sides

INPUT_FNAME = 'res/day3_inp.txt'

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        temp = [[], [], []]
        for line in fh:
            a, b, c = [int(side.strip()) for side in line.split(' ') if side is not '']
            temp[0].append(a)
            temp[1].append(b)
            temp[2].append(c)
            if len(temp[0]) == 3:
                res.append(tuple(temp[0]))
                res.append(tuple(temp[1]))
                res.append(tuple(temp[2]))
                temp = [[], [], []]
    return res

def is_triangle(sides):
    a, b, c = sides
    return (a + b > c) and (b + c > a) and (a + c > b)

def main():
    triangles = read_input()
    n = 0
    for triangle in triangles:
        if is_triangle(triangle):
            n += 1
    print('Valid triangles:', n)

if __name__ == '__main__':
    print('*--------------------------*')
    print('|-Squares with Three Sides-|')
    print('*--------------------------*')
    main()

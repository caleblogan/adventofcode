# No Time for a Taxicab

INPUT_FNAME = 'res/day1_inp.txt'

class Santa:
    DIRECTION = ['North', 'East', 'South', 'West']
    def __init__(self):
        self.pos = [0, 0]
        self.facing = 0
        self.visited = set()

    def blocks_away(self):
        return abs(self.pos[0]) + abs(self.pos[1])

    def step(self, direction):
        d = direction[0]
        steps = int(direction[1:])
        self.update_facing(d)
        for i in range(1, steps+1):
            self.update_pos(1)
            if tuple(self.pos) in self.visited:
                print(self.pos)
            else:
                self.visited.add(tuple(self.pos))

    def update_facing(self, direction):
        if direction is 'R':
            rotation = 1
        else:
            rotation = -1
        self.facing = (self.facing + rotation + 4) % 4

    def update_pos(self, steps):
        if self.facing == 0:
            self.pos[1] += steps
        elif self.facing == 1:
            self.pos[0] += steps
        elif self.facing == 2:
            self.pos[1] -= steps
        else:
            self.pos[0] -= steps

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        for line in fh:
            for direction in line.split(','):
                res.append(direction.strip())
    return res

def follow_directions(directions):
    santa = Santa()
    for step in directions:
        santa.step(step)
    return santa.blocks_away()

def main():
    directions = read_input()
    blocks = follow_directions(directions)
    print(blocks)

if __name__ == '__main__':
    print('No Time for a Taxicab')
    main()

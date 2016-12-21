# Bathroom Security

INPUT_FNAME = 'res/day2_inp.txt'

class KeypadSolver:
    def __init__(self, keypad):
        """Keypad is multidimensional array"""
        self.keypad = keypad
        self.cur_key = [len(keypad)//2, len(keypad[0])//2]
        self.code = []

    def step(self, key, direction):
        """Takes a key and a direction(L,R,U,D) & returns a key in bounds"""
        row, col = key
        width, height = len(self.keypad), len(self.keypad[0])
        if direction is 'U':
            temp = row - 1
            if temp >= 0 and self.keypad[temp][col] is not None:
                row = temp
        elif direction is 'R':
            temp = col + 1
            if temp < width and self.keypad[row][temp] is not None:
                col = temp
        elif direction is 'D':
            temp = row + 1
            if temp < height and self.keypad[temp][col] is not None:
                row = temp
        elif direction is 'L':
            temp = col - 1
            if temp >= 0 and self.keypad[row][temp] is not None:
                col = temp
        return [row, col]

    def process_instruction(self, instruction):
        """Takes an instruction line and returns a key from the keypad"""
        key = self.cur_key
        for s in instruction:
            key = self.step(key, s)
        return key

    def solve(self, instructions):
        """Takes an array of instructions and returns a code for the keypad"""
        for instruction in instructions:
            self.cur_key = self.process_instruction(instruction)
            row, col = self.cur_key
            self.code.append(self.keypad[row][col])
        return ''.join([str(c) for c in self.code])

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        for line in fh:
            res.append(line.strip())
    return res

def build_keypad(size):
    keypad = []
    for row in range(size[0]):
        keypad.append([])
        for col in range(1, size[1]+1):
            keypad[row].append(col + (row * size[0]))
    return keypad


def main():
    instructions = read_input()
    # keypad = build_keypad((3, 3))
    keypad = [
        [None, None, '1', None, None],
        [None, '2', '3', '4', None],
        ['5', '6', '7', '8', '9'],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None],
    ]
    keypad_solver = KeypadSolver(keypad)
    code = keypad_solver.solve(instructions)
    print(code)

if __name__ == '__main__':
    main()

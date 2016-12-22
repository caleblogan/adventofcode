#

INPUT_FNAME = 'res/day6_inp.txt'
TEST_INPUT_FNAME = 'res/day6_test_inp.txt'

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        for line in fh:
            res.append(line.strip())
    return res

def main():
    codes = read_input()
    counts = [{}, {}, {}, {}, {}, {}, {}, {}]
    for line in codes:
        for i, char in enumerate(line):
            if char not in counts[i]:
                counts[i][char] = 1
            else:
                counts[i][char] += 1
    code = ''
    for d in counts:
        code += min(d, key=lambda k:d[k])
    print(codes[0])
    print(code)

if __name__ == '__main__':
    main()

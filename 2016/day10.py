from collections import defaultdict

INPUT_FNAME = 'res/day10_inp.txt'
# INPUT_FNAME = 'res/day10_test_inp.txt'

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        for line in fh:
            res.append(line.strip())
    return res

class Bot:
    def __init__(self, number):
        self.number = number
        self.instruction = None
        self.chips = []

    def ready(self):
        """Returns True if bot has two chips and an instruction"""
        return len(self.chips) == 2 and self.instruction

    def exec_instruction(self, bots, outputs):
        # print('--------------------------------------------------------------')
        print('Executing instruction for bot {}'.format(self.number))
        lo = self.instruction[0]
        hi = self.instruction[1]
        lo_val = min(self.chips)
        hi_val = max(self.chips)
        if lo[0] == 'output':
            outputs[lo[1]].append(lo_val)
        else:
            if lo[1] not in bots:
                bots[lo[1]] = Bot(lo[1])
            bots[lo[1]].chips.append(lo_val)

        if hi[0] == 'output':
            outputs[hi[1]].append(hi_val)
        else:
            if hi[1] not in bots:
                bots[hi[1]] = Bot(hi[1])
            bots[hi[1]].chips.append(hi_val)
        self.reset()
        # print(bots, outputs)
        # print('--------------------------------------------------------------')

    def reset(self):
        self.instruction = None
        self.chips = []

    def has_chips(self, chip1, chip2):
        return chip1 in self.chips and chip2 in self.chips

    def __repr__(self):
        return 'chips={}'.format(self.chips)

def parse_input_to_bot_instuction(tokens):
    return (int(tokens[1]), int(tokens[5]))

def parse_bot_exec_instruction(tokens):
    bot = int(tokens[1])
    lo = (tokens[5], int(tokens[6]))
    hi = (tokens[10], int(tokens[11]))
    return bot, lo, hi

def assign_instructions(tokens, bots, outputs):
    """
    Takes instruction tokens, parses them and assigns the instruction to a
    bot.
    """
    if tokens[0] == 'value':
        chip, bot = parse_input_to_bot_instuction(tokens)
        if bot not in bots:
            bots[bot] = Bot(bot)
        bots[bot].chips.append(chip)
    elif tokens[0] == 'bot':
        bot, lo, hi= parse_bot_exec_instruction(tokens)
        if bot not in bots:
            bots[bot] = Bot(bot)
        bots[bot].instruction = (lo, hi)
    else:
        print('Invalid instruction')


def main():
    instructions = read_input()
    bots = {}
    outputs = defaultdict(list)
    for instruction in instructions:
        tokens = instruction.split(' ')
        assign_instructions(tokens, bots, outputs)
        while True:
            executed = False
            for bot in bots.values():
                # if len(bot.chips) == 2 and bot.has_chips(61, 17):
                #     print('Bot {} has chips 61 and 17'.format(bot.number))
                #     return
                if bot.ready():
                    bot.exec_instruction(bots, outputs)
                    executed = True
                    break
            if not executed:
                break
    print(outputs[0][0] * outputs[1][0] * outputs[2][0])

if __name__ == '__main__':
    main()

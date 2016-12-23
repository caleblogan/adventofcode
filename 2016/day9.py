INPUT_FNAME = 'res/day9_inp.txt'

def read_input():
    with open(INPUT_FNAME, 'r') as fh:
        return fh.readlines()[0]

def decompress_level(seq):
    cur = 0
    count = 0
    while cur < len(seq):
        if seq[cur] is '(':
            rh_paren = seq.find(')', cur)
            marker = seq[cur+1:rh_paren]
            n_chars, n = [int(elem) for elem in marker.split('x')]
            cur = rh_paren + 1
            repeat_chunk = seq[cur:cur+n_chars]
            count += decompress_level(repeat_chunk) * n
            cur += n_chars
        else:
            cur += 1
            count += 1
    return count

def is_decompressed(seq):
    """If seq has no markers return True"""
    return True if seq.find('(') == -1 else False

def main():
    seq = read_input()
    # seq = 'ADVENT'
    # seq = 'A(1x5)BC'
    # seq = '(3x3)XYZ'
    # seq = 'A(2x2)BCD(2x2)EFG'
    # seq = '(6x1)(1x3)A'
    # seq = 'X(8x2)(3x3)ABCY'
    # seq = 'X(8x2)(3x3)ABCY'  #18
    # seq = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    # seq = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

    print('Count:', decompress_level(seq.strip()))


if __name__ == '__main__':
    main()

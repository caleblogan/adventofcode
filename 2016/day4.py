# Security Through Obscurity
INPUT_FNAME = 'res/day4_inp.txt'

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        for line in fh:
            res.append(line.strip())
    return res

def is_decoy(room):
    """
    Takes in a encrypted room and returns true if room is a decoy.
    A room is real if the checksum[abxyz] is the five most common letters in
    the encrypted text.
    """
    room_name = room[0].replace('-', '')
    checksum = room[2]
    # print(room)
    letters = {}
    for i, char in enumerate(room_name):
        if char not in letters:
            letters[char] = [i, 1]
        else:
            letters[char][1] += 1
    letters = [(k, val[1]) for k, val in letters.items()]
    letters = sorted(letters, key=lambda l: l[1], reverse=True)
    # print(letters)
    cur = 0
    while cur < len(checksum):
        if ties(letters, cur):
            t = ties(letters, cur)
            # print(cur, ')', 'ties:', t)
            for i in range(len(t)):
                if cur >= len(checksum):
                    break
                char = checksum[cur]
                if char not in t or not in_checksum_order(checksum, cur, t):
                    return True
                cur += 1
        elif checksum[cur] is letters[cur][0]:
            # print(cur, ')no ties:', checksum[cur])
            cur += 1
        else:
            return True
    return False

def in_checksum_order(checksum, cur, t):
    """
    Takes part of a checksum and cur index into checksum and returns True if
    char is in the correct pos starting from cur to the right.
    Only checks curs right neighbour, not the whole checksum.
    """
    if cur >= len(checksum) - 1:
        return True
    elif checksum[cur+1] not in t:
        return True
    elif checksum[cur] <= checksum[cur+1]:
        return True
    return False

def ties(letters, i):
    """checks for ties from starting index i to elem with smaller index"""
    res = []
    start_count = letters[i][1]
    for char, count in letters[i:]:
        if count == start_count:
            res.append(char)
        else:
            break
    return res if len(res) > 1 else []

def parse_room(raw_room):
    id_start = raw_room.rfind('-') + 1
    checksum_start = raw_room.find('[') + 1
    room_id = int(raw_room[id_start:checksum_start-1])
    checksum = raw_room[checksum_start:len(raw_room)-1]
    room_name = raw_room[:id_start-1]
    return (room_name, room_id, checksum)

def sum_room_ids(rooms):
    total = 0
    for room in rooms:
        total += room[1]
    return total

def rotate(char, r_id):
    o = ord(char) - ord('a')
    o = (o + r_id) % 26
    return chr(o + ord('a'))

def decrypt_room(room):
    name = room[0]
    r_id = room[1]
    res = []
    for char in name:
        if char is '-':
            res.append(' ')
        else:
            res.append(rotate(char, r_id))
    return (''.join(res), r_id, room[2])

def main():
    rooms = read_input()
    trooms = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]',
    ]
    valid_rooms = []
    for raw_room in rooms:
        room = parse_room(raw_room)
        if not is_decoy(room):
            valid_rooms.append(room)
    print(valid_rooms)
    for i, room in enumerate(valid_rooms):
        # valid_rooms[i] = decrypt_room(room)
        print(decrypt_room(room))

    print('All Rooms:', len(rooms))
    print('Valid Rooms:', len(valid_rooms))
    # print('Valid Rooms ID Sum:', sum_room_ids(valid_rooms))
    # print(valid_rooms)

if __name__ == '__main__':
    main()

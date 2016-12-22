# How About a Nice Game of Chess
import hashlib

def valid_index(hashcode):
    return hashcode[0:5] == '00000'

def update_password(password, hashcode):
    pos = hashcode[5]
    char = hashcode[6]
    if int(pos, 16) < 8 and password[int(pos)] == None:
        password[int(pos)] = char
    # print(hashcode)
    # print(pos, char)
    print(password)

def valid_password(password):
    for char in password:
        if not char:
            return False
    return True

def main():
    puzzle_input = 'ojvtpuvg'  # door id
    # puzzle_input = 'abc'
    password = [None] * 8
    for i in range(100000000):
        m = hashlib.md5()
        m.update((puzzle_input + str(i)).encode())
        hashcode = m.hexdigest()
        if valid_index(hashcode):
            update_password(password, hashcode)
        if valid_password(password):
            break
    print(''.join(password))

if __name__ == '__main__':
    main()

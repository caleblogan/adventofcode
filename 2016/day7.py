#

INPUT_FNAME = 'res/day7_inp.txt'

def read_input():
    res = []
    with open(INPUT_FNAME, 'r') as fh:
        for line in fh:
            res.append(line.strip())
    return res

def is_ABBA(section):
    if section[0] is section[1]:
        return False
    elif section[0:2] == ''.join(reversed(section[2:4])):
        return True
    return False

def supports_tls(ip):
    """Returns true if ip supports tls"""
    in_hypernet = False
    has_abba = False
    for i, char in enumerate(ip[:-3]):
        if char is '[':
            in_hypernet = True
        elif char is ']':
            in_hypernet = False
        elif is_ABBA(ip[i:i+4]):
            if in_hypernet:
                return False
            else:
                has_abba = True
    return has_abba

def is_ABA(ip):
    return ip[0] is ip[2] and ip[0] is not ip[1]

def to_bab(aba):
    return aba[1] + aba[0] + aba[1]

def supports_ssl(ip):
    """Returns True if ip supports ssl"""
    in_hypernet = False
    hypernet_abas = []
    supernet_abas = []
    for i, char in enumerate(ip[:-2]):
        if char is '[':
            in_hypernet = True
        elif char is ']':
            in_hypernet = False
        elif is_ABA(ip[i:i+3]):
            if in_hypernet:
                hypernet_abas.append(ip[i:i+3])
            else:
                supernet_abas.append(ip[i:i+3])
    for aba in supernet_abas:
        if to_bab(aba) in hypernet_abas:
            return True
    return False

def main():
    ips = read_input()
    # ips = ['abba[mnop]qrst', 'abcd[bddb]xyyx']
    tls_ips = []
    ssl_ips = []
    for ip in ips:
        if supports_ssl(ip):
            ssl_ips.append(ip)
    print(len(ssl_ips))

if __name__ == '__main__':
    main()

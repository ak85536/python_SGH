f = 'Oliver_Twist_Dickens.txt'
with open(f, 'r') as infile:
    line = infile.readline()
    d = dict()
    while line:
        line = infile.readline()
        for char in '<>`~=+_[]{}|?":;.,!\\@#$%^&*()\'0123456789/\t':
            line = line.replace('--', ' ')
            line = line.replace(char, '')
        for l in line:
            words = line.strip().lower().split(' ')
        for i in words:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
    d.pop('', None)

    for word in list(d.keys()):
        print(word, "-", d[word])

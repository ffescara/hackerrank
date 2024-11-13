def atas(n, m):
    separator = ".|."
    for i in range(n//2):
        print((separator*(i+i+1)).center(m, "-"))

def bawah(n, m):
    separator = ".|."
    for i in reversed(range(n//2)):
        print((separator*(i+i+1)).center(m, "-"))

if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    atas(n, m)
    print('WELCOME'.center(m, '-'))
    bawah(n, m)
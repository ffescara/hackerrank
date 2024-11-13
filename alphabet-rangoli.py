import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase

    patterns = [(("-".join(alphabet[size-1:i:-1] + alphabet[i:size])).center(4*size-3, "-")) for i in range(size)]

    print(patterns)
    
    print("\n".join(patterns[-1:-size:-1] + patterns))      

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
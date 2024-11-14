def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    kevin = {}
    stuart = {}
    i = 0
    while i < len(string):
        if string[i] not in vowels:
            if string[i] in kevin:
                kevin[string[i]] += 1
            else:
                kevin[string[i]] = 1
        print(i)
        print(kevin)
        i += 1

if __name__ == '__main__':
    s = input()
    minion_game(s)
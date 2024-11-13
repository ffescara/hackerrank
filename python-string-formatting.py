def print_formatted(number):
    width = len(bin(number)) - 1

    for i in range(1, number + 1):
      print(str(int(i)).rjust(width-1) + str(oct(i)[2:]).rjust(width) + str(hex(i).upper()[2:]).rjust(width) + str(bin(i)[2:]).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
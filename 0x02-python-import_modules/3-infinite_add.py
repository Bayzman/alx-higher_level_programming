#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv)
    total = 0
    for i in range(1, arg_len):
        total += int(argv[i])

    print(f'{total}')

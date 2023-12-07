#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length <= 1:
        print("0 arguments.")
    else:
        if length == 2:
            print(f"{length - 1} argument:")
        else:
            print(f"{length - 1} arguments:")
        for i in range(1, length):
            print(f"{i}: {sys.argv[i]}")

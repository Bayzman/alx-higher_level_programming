#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dirs = dir(hidden_4)
    for i in range(len(dirs)):
        if "__" not in dirs[i]:
            print(dirs[i])

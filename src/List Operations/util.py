def perform_operation(arr, cmd):
    if cmd[0] == "insert":
        i = int(cmd[1])
        e = int(cmd[2])
        arr.insert(i, e)

    elif cmd[0] == "print":
        print(arr)

    elif cmd[0] == "remove":
        e = int(cmd[1])
        arr.remove(e)

    elif cmd[0] == "append":
        e = int(cmd[1])
        arr.append(e)

    elif cmd[0] == "sort":
        arr.sort()

    elif cmd[0] == "pop":
        arr.pop()

    elif cmd[0] == "reverse":
        arr.reverse()
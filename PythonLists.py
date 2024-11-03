# Python Lists
if __name__ == '__main__':
    N = int(input())
    lst = list()

    for i in range(N):

        ip = input()

        if ip == "print":
            print(lst)
        elif ip == "pop":
            lst.pop()
        elif ip == "sort":
            lst.sort()
        elif ip == "reverse":
            lst.reverse()
        elif ip[0] == "i":
            lst.insert(int(ip[7]), int(ip[9:]))
        elif ip[0:6] == "remove":
            lst.remove(int(ip[7:]))
        elif ip[0] == "a":
            lst.append(int(ip[7:]))

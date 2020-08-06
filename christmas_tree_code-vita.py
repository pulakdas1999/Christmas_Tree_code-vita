N = int(input())
if N <= 1:
    print("You cannot generate christmas tree")
elif N > 20:
    print("Tree is no more")
else:
    for i in range(1,N):
        if i == 1:
            c = 1
            for j in range(0,N+1):
                print("  " * (N - j) + "* " * (j + c),sep="")
                c += 1
        elif i == 2:
            c = 1
            for j in range(0, N):
                if j != 0:
                    print("  " * (N - j) + "* " * (j + c), sep="")
                c += 1
        else:
            c = 1
            for j in range(0, N - i + 2):
                if j != 0:
                    print("  " * (N - j) + "* " * (j + c), sep="")
                c += 1
    print("  " * N + "*",sep="")
    print("  " * N + "*",sep="")
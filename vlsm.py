def netArray(bits):
    h = int(2 ** ((bits - bits % 2)/2))
    w = 2 * h if bits % 2 else h
    net = []

#    net.append([int(bin(c)[2:],4) + 2 * int(bin(r)[2:], 4) for c in range(w) for r in range(h)])


    for r in range(h):
        net.append([int(bin(c)[2:],4) + 2 * int(bin(r)[2:], 4) for c in range(w)])
    return net



netMaskBits = 8
net = netArray(netMaskBits)

for n in net:
    for ip in n:
        print(str(ip).rjust(4), end=" ")
    print("\n")


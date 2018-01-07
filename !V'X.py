def interpret(prgm):
    if prgm[-3:] != ".vx": prgm += ".vx"
    p = open(prgm).read()
    print(p)
    x = 0
    m = 0
    a = 0
    c = 0
    while True:
        if x == len(p): break
        elif p[x] == "[": m = x
        elif p[x] == "]": x = m
        elif p[x] == "_": break
        elif p[x] == "-": a -= 1
        elif p[x] == "+": a += 1
        elif p[x] == "&":
            print(a,end=' ',flush=True)
            if type(a) == str: a = int(a)
        elif p[x] == "!": a = chr(a)
        elif p[x] == "#":
            if a == convert(p[x+1:x+5]): x += 5
        x += 1
def convert(b):
    n = ["0","0","0","0","0","0","0","0"]
    t = {".":[3,2,1,0],";":[7,6,5,4],":":[(7,3),(6,2),(5,1),(4,0)]}
    for x in range(4):
        if b[x] == "|": continue
        elif b[x] == ".": n[t["."][x]] = "1"
        elif b[x] == ";": n[t[";"][x]] = "1"
        elif b[x] == ":": n[t[":"][x][0]] = "1"; n[t[":"][x][1]] = "1"
    return int("".join(n),2)
interpret(input("!V'X> "))

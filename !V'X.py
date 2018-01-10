import time
def interpret(prgm, *args):
    s = time.time()
    if prgm[-3:] != ".vx": prgm += ".vx"
    try: p = open(prgm).read()
    except FileNotFoundError: return "File not found"
    for a in args: a = int(a)
    x = 0
    a = 0
    l = [0,0,0,0]
    lp = 0
    e = 0
    m = [0 for x in range(256)]
    mp = 0
    while True:
        if x == len(p): break
        elif p[x] == "[":
            if e == 1: lp += 1
            l[lp] = x
            e = 1
        elif p[x] == "]": x = l[lp]
        elif p[x] == "#":
            if m[mp] == convert(p[x+1:x+5]):
                x += 5
                if p[x] == "]" and lp != 0: lp -= 1
                elif p[x] == ">": x += 1
            else: x += 4
        elif p[x] == "!":
            if a == len(args): continue
            else: m[mp] = args[a]; a += 1
        elif p[x] == ">": mp = convert(p[x+1:x+5])
        elif p[x] == "&":
            if mp == 255: print(chr(m[mp]),end='',flush=True)
            else: print(m[mp],end=' ',flush=True)
        elif p[x] == "+":
            m[mp] += 1
            if m[mp] == 256: m[mp] = 0
        elif p[x] == "-":
            m[mp] -= 1
            if m[mp] < 0: m[mp] = 255
        x += 1
    del x, l, lp, e, m, mp, a; print(); return "Finished interpreting program successfully\nTime: %s"%(time.time()-s)
def convert(b):
    n = ["0","0","0","0","0","0","0","0"]
    t = {".":[4,5,6,7],";":[0,1,2,3],":":[(4,0),(5,1),(6,2),(7,3)]}
    for x in range(4):
        if b[x] == "|": continue
        elif b[x] == ".": n[t["."][x]] = "1"
        elif b[x] == ";": n[t[";"][x]] = "1"
        elif b[x] == ":": n[t[":"][x][0]] = "1"; n[t[":"][x][1]] = "1"
    return int("".join(n),2)
a = ""
def next_0_reg(l):
    for n in range(256):
        if l[n] == 0: return n
    return 0
while True:
    a = input("!V'X> ").split()
    if a[0] == ".quit": break
    else: print(interpret(a[0], *a[1:]))

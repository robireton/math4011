def pair(a):
    """take a number in the range 0---2^{14}-1 and
    return a pair in the range 0---2^7-1"""
    return 128*a[0]+a[1]


def unpair(z):
    """undoes what pair() does"""
    t = z % 128
    s = (z-t)/128
    return [s, t]


a = "Hi"
a = [ord(x) for x in a]
z = pair(a)
b = unpair(z)
c = "".join([chr(x) for x in b])

print(a, z, b, c)


def pairlist(dt):
    """takes a digitized list and pairs its entries returning
    a list with bigger numbers"""
    ans = []
    while len(dt) >= 2:
        ans.append(pair(dt[0:2]))
        dt = dt[2:]
    if len(dt) == 1:
        dt.append(0)
        ans.append(pair(dt))
    return ans


a = "abcdefghijklmnopq"
dt = [ord(x) for x in a]
print(dt)
ans = pairlist(dt)
print(ans)


def unpairlist(pl):
    """undoes what pairlist() does"""
    up = []
    for x in pl:
        up.extend(unpair(x))

    if up[len(up)-1] == 0:
        up.pop()
    return up


up = unpairlist(ans)

print("".join([chr(x) for x in up]))

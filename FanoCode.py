
s = 'тепайкин_максим_андреевич_пока_ещё_студент_203_группы'

lets = dict()

for sym in s:
    if sym in lets.keys():
        lets[sym] += 1
    else:
        lets[sym] = 1

lets = (sorted(lets.items(), key=lambda pr: pr[1]))




def get_border(lets, l, r):
    if r - l == 1:
        return l
    pref = 0
    summ = 0
    for i in range(l, r):
        summ += lets[i][1]
    minEl = summ
    border = 0
    for i in range(l, r):
        pref += lets[i][1]
        if abs(pref - (summ-pref)) >= minEl:
            border = i - 1
            pref -= lets[i][1]
            break
        else:
            minEl = abs(pref - (summ-pref))
    return border


def get_tern_border(lets, l, r):
    if r - l <= 2:
        return l
    summ = 0
    for i in range(l, r):
        summ += lets[i][1]
    min_dif = summ
    b1 = 0
    b2 = 0
    pref1 = 0
    pref2 = 0
    for i in range(l, r-1):
        pref1 += lets[i][1]
        pref2 = 0
        for j in range(i + 1, r):
            pref2 += lets[j][1]
            dif = abs(pref1 - (summ - pref1 - pref2)) + abs(pref2 - (summ - pref1 - pref2)) + abs(pref2-pref1)
            if dif < min_dif:
                min_dif = dif
                b1 = i
                b2 = j

    return [b1, b2]





ans = ['' for zero in range(len(lets))]


def fano(lets, l, r):
    global ans
    if r - l == 1:
        return

    bord = get_border(lets, l, r)
    for i in range(l, bord+1):
        ans[i] += '1'
    for i in range(bord+1, r):
        ans[i] += '0'

    fano(lets, l, bord+1)
    fano(lets, bord+1, r)


def tern_fano(lets, l, r):
    global ans
    if r - l <= 2:
        return

    b1, b2 = get_tern_border(lets, l, r)
    xxxx = 10
    for i in range(l, b1 + 1):
        ans[i] += '2'
    for i in range(b1 + 1, b2 + 1):
        ans[i] += '1'
    for i in range(b2 + 1, r):
        ans[i] += '0'

    tern_fano(lets, l, b1 + 1)
    tern_fano(lets, b1 + 1, b2 + 1)
    tern_fano(lets, b2 + 1, r)



fano(lets, 0, len(lets))
#tern_fano(lets, 0, len(lets))



for i in range(len(lets)):
    newItem = list(lets[i])
    newItem.append(ans[i])
    lets[i] = newItem


for i in reversed(range(len(lets))):
    print(lets[i])


code = dict()
for item in lets:
    code[item[0]] = item[2]

ans = ''
for sym in s:
    ans += code[sym]

print()
print(ans)


lSr = 0
for item in lets:
    lSr += len(item[2]) * item[1]
print(lSr)
print(lSr / len(s))




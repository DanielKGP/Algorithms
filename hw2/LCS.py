#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


def lcs_len(a, b):
    n = len(a)
    m = len(b)

    l = [([0] * (m + 1)) for i in range(n + 1)]
    direct = [([0] * m) for i in range(n)]

    for i in range(n + 1)[1:]:
        for j in range(m + 1)[1:]:
            if a[i - 1] == b[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            elif l[i][j - 1] > l[i - 1][j]:
                l[i][j] = l[i][j - 1]
                direct[i - 1][j - 1] = -1
            else:
                l[i][j] = l[i - 1][j]
                direct[i - 1][j - 1] = 1

    return l, direct

def get_lcs(direct, a, i, j):
    lcs = []
    get_lcs_inner(direct, a, i, j, lcs)
    return lcs

def get_lcs_inner(direct, a, i, j, lcs):
    if i < 0 or j < 0:
        return

    if direct[i][j] == 0:
        get_lcs_inner(direct, a, i - 1, j - 1, lcs)
        lcs.append(a[i])

    elif direct[i][j] == 1:
        get_lcs_inner(direct, a, i - 1, j, lcs)
    else:
        get_lcs_inner(direct, a, i, j - 1, lcs)


a = "xzyzzyx"
b = "zxyyzxz"
l, direct = lcs_len(a, b)
lcs1 = get_lcs(direct, a, len(a) - 1, len(b) - 1)

print 'the longest number is:',l[len(a)][len(b)]
#print lcs1
print "".join(lcs1)

c = "ALLAAQANKESSSESFISRLLAIVAD"
d = "KLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG"
l, direct = lcs_len(c, d)
lcs2 = get_lcs(direct, c, len(c) - 1, len(d) - 1)


print 'the longest number is:',l[len(c)][len(d)]
#print lcs2
print "".join(lcs2)

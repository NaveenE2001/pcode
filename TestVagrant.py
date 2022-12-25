inp = int(input(("enter the value ")))
tot_news = [26.5, 20.5, 34, 10.5, 18]
dct = {26.5: 'toi', 20.5: 'hindu', 34: 'et', 10.5: 'bm', 18: 'ht'}
cmbn = it.combinations(tot_news, 2)
ls = []
for i in cmbn:
    val = list(i)
    # print(f)
    if (sum(val) < inp):
        ls.append(val)
ls2 = []
for j in range(len(ls)):
    val1 = ls[j][0]
    val2 = ls[j][1]
    ls2.append((dct[val1], dct[val2]))
# print(ls2)
for i in ls2:
    cnvset = set(i)
    print(cnvset, end=',')

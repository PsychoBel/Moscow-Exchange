string = input()
string = string.replace(",", "")
string = string.split()
res = {i: string.count(i)  for i in string}
print(sorted(res.items(), key = lambda pair: (pair[1], pair[0]))[-1][0])


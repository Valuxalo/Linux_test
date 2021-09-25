
import requests
import re
flag = 0
a, b = (input() for i in range(2))
pattern_s = r"href=.*?html"
res = requests.get(a)
st = res.status_code
s_url = []
#print(st)
if str(st) == '200':
    in_a = str(res.content)
    #print(res.content)
    summ = re.findall(pattern_s, in_a)
    #print(len(summ))
    for j in range(len(summ)):
        idx_1 = re.search(pattern_s, in_a)
        s_url.append(in_a[idx_1.start()+6:idx_1.end()])
        #print(s_url)
        in_a = in_a[idx_1.end()+1:]

    for j in s_url:
        res = requests.get(j)
        st = res.status_code
        if str(st) == '200':
            in_c = str(res.content)
            summ = re.findall(pattern_s, in_c)
            for n in range(len(summ)):
                idx_2 = re.search(pattern_s, in_c)
                if in_c[idx_2.start()+6:idx_2.end()] == b:
                    flag = 1
                    break
                in_c = in_c[idx_2.end() + 1:]


if flag == 1:
    print('Yes')
else:
    print('No')

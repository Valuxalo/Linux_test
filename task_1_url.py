
import requests
import re
def url_check(a):
    pattern = r"href=.*?html"
    s_url = []
    res = requests.get(a)
    st = res.status_code
    if str(st) == '200':
        in_a = str(res.content)
        summ = re.findall(pattern, in_a)
        for j in range(len(summ)):
            idx_1 = re.search(pattern, in_a)
            s_url.append(in_a[idx_1.start() + 6:idx_1.end()])
            in_a = in_a[idx_1.end() + 1:]
    return s_url

flag = 0
a, b = (input() for i in range(2))
ss = url_check(a)
for j in ss:
    bb = url_check(j)
    if b in bb:
        flag = 1
        break

if flag == 1:
    print('Yes')
else:
    print('No')

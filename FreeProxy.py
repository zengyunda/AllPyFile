import re,requests
url="http://www.xicidaili.com"
def get_proxy(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
    ipcheck = []
    content = requests.get(url,headers=headers).text
    iplist = re.findall('''<tr class=".*?">.*?<td>([0-9.]*?)</td>\s*?<td>([0-9]*?)</td>\s*?<td>(\w*?)</td>\s*?<td class="country">.*?</td>\s*?<td>(.*?)</td>.*?</tr>''',content, flags=re.S)
    print(iplist)
    print(len(iplist))
    for i in iplist:
        dic1 = {"地区": i[2], "IP": i[0], "端口": i[1], "协议": i[3]}
        ipcheck.append(dic1)
    print(ipcheck)
    return ipcheck
get_proxy(url)
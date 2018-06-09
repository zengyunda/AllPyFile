import urllib.request
import re
import xlwt
import time
import threading
def JobPython(url):
    list11=[]
    list21=[]
    list31=[]
    list41=[]
    list51=[]
    for i in range(1,50):
        response=urllib.request.urlopen(url+str(i)).read()
        list1=re.compile('class="t1 ">.*?<a target="_blank" title="(.*?)"',re.S).findall(response.decode('gbk'))
        list11.extend(list1)
        list2=re.compile(' <span class="t2"><a target="_blank" title="(.*?)"',re.S).findall(response.decode('gbk'))
        list21.extend(list2)
        list3=re.compile(' <span class="t2"><a target="_blank" title=".*? <span class="t3">(.*?)</span>',re.S).findall(response.decode('gbk'))
        list31.extend(list3)
        list4=re.compile(' <span class="t2"><a target="_blank" title=".*? <span class="t4">(.*?)</span>',re.S).findall(response.decode('gbk'))
        list41.extend(list4)
        list5=re.compile(' <span class="t2"><a target="_blank" title=".*? <span class="t5">(.*?)</span>',re.S).findall(response.decode('gbk'))
        list51.extend(list5)
    list11.insert(0,'职位')
    list21.insert(0,'公司名称')
    list31.insert(0,'城市')
    list41.insert(0,'薪资')
    list51.insert(0,'发布日期')
    workbook=xlwt.Workbook()#新建一个工作簿
    sheet=workbook.add_sheet('前程无忧')#在工作簿中新建 一个sheet，并命名为前程无忧
    j=0
    for i in range(0,len(list11)):
        sheet.write(i,j,list11[i])#i表示行，j表示列，list11[i]就是列表1中每循环一次的内容，从第0行0列开始，即Excel的第一行第一列
        sheet.write(i,j+1,list21[i])
        sheet.write(i,j+2,list31[i])
        sheet.write(i,j+3,list41[i])
        sheet.write(i,j+4,list51[i])
    workbook.save('D:/前程无忧.xls')

def JobAnalyse(url):
    list11=[]
    list21=[]
    list31=[]
    list41=[]
    list51=[]
    for i in range(1,50):
        response=urllib.request.urlopen(url+str(i)+'.html?').read()
        list1=re.compile('class="t1 ">.*?<a target="_blank" title="(.*?)"',re.S).findall(response.decode('gbk'))
        list11.extend(list1)
        list2=re.compile(' <span class="t2"><a target="_blank" title="(.*?)"',re.S).findall(response.decode('gbk'))
        list21.extend(list2)
        list3=re.compile(' <span class="t2"><a target="_blank" title=".*? <span class="t3">(.*?)</span>',re.S).findall(response.decode('gbk'))
        list31.extend(list3)
        list4=re.compile(' <span class="t2"><a target="_blank" title=".*? <span class="t4">(.*?)</span>',re.S).findall(response.decode('gbk'))
        list41.extend(list4)
        list5=re.compile(' <span class="t2"><a target="_blank" title=".*? <span class="t5">(.*?)</span>',re.S).findall(response.decode('gbk'))
        list51.extend(list5)
    list11.insert(0,'职位')
    list21.insert(0,'公司名称')
    list31.insert(0,'城市')
    list41.insert(0,'薪资')
    list51.insert(0,'发布日期')
    workbook=xlwt.Workbook()#新建一个工作簿
    sheet=workbook.add_sheet('前程无忧')#在工作簿中新建 一个sheet，并命名为前程无忧
    j=0
    for i in range(0,len(list11)):
        sheet.write(i,j,list11[i])#i表示行，j表示列，list11[i]就是列表1中每循环一次的内容，从第0行0列开始，即Excel的第一行第一列
        sheet.write(i,j+1,list21[i])
        sheet.write(i,j+2,list31[i])
        sheet.write(i,j+3,list41[i])
        sheet.write(i,j+4,list51[i])
    workbook.save('D:/数据分析.xls')

#未设置线程
if __name__ == '__main__':
    starttime = time.time()
    JobPython('http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=030000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=Python&keywordtype=2&curr_page=')
    JobAnalyse('https://search.51job.com/list/030000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,')
    endtime = time.time()
    dtime = endtime -starttime
    print("常规时间为：",dtime)
#多线程一起跑，两个线程10次循环相差5s，循环20次，常规是50秒，多线程是37秒
t1 = threading.Thread(target=JobPython,args=('http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=030000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=Python&keywordtype=2&curr_page=',))
t2 = threading.Thread(target=JobAnalyse,args=('https://search.51job.com/list/030000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,',))
starttime = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
endtime = time.time()
dtime = endtime - starttime
print("2个线程时间为：",dtime)


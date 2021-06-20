from bs4 import BeautifulSoup
import os 
import re
import requests

def askUrl(url):
    head = {
        "Connection": "keep-alive"
        ,"Cookie": "wdcid=549ff78b84129b28; sso_c=0; sfr=1; HMF_CI=98e82ed3ffed503b67f7f01df042c9365579e6d9889bcf9fb554dfbfe54d64170c; wdlast=1623911474; wdses=026f119bc8eb98d7; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1623848210,1623911475; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1623911475"
        ,"Upgrade-Insecure-Requests": "1"
        ,"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

    
    }    
    html = requests.get(url,headers = head)
    html.encoding = 'GBK'
    
    return html.text


def get_content(html):
    bs = BeautifulSoup(html,'html.parser')
    
    srcs = []
    div = bs.find('div',class_= 'list2 cf')
    
    find_src = re.compile(r'<a href="(.*?)" target="_blank">')
    
    for li in div.find_all('a'):
        li = str(li)
        src = re.findall(find_src,li)[0]
        srcs.append(src)
    return srcs

def main_text(srcs):
    fst_paras = []
    titles = []
    for src in srcs:
        # print(src)


        html = askUrl(src)
        bs = BeautifulSoup(html,'html.parser')
        try:
            main_text = bs.find('div',class_="rm_txt_con cf")
            fst_paras.append(main_text.text)
            h1 = bs.find('div',class_="layout rm_txt cf").find('h1').text
            titles.append(h1)
        except:
            h1 = '0'
            main_text = '0'
            fst_paras.append(main_text)
            titles.append(h1)
            continue
    return fst_paras,titles

def save(srcs,titles,main_text):
    path = r'/home/baoquanlong/data/news'
    
    if not os.path.exists(path):
        os.mkdir(path)
        
    for i,src,title,main_text in zip(range(len(titles)),srcs,titles,main_text):
        with open(path+'/{}.txt'.format(i+16),mode='w',encoding='utf-8') as f:
            f.write('\t'+src)          
            f.write('\n')
            f.write('\t'+title)
            f.write('\n')
            f.write(main_text)
            print('成功')
            

def main():
    url = 'http://www.people.com.cn/'
    html = askUrl(url)
    srcs = get_content(html)

    
    ##获取每个网址所代表的文章的大意
    
    texts,titles  = main_text(srcs)

        
    #在~/data/news文件夹中创建各个txt文件来储存每一个新闻的内容和标题
    
    save(srcs,titles,texts)

main()
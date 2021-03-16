import requests
from bs4 import BeautifulSoup
import re
# 将用户代理信息放入请求头中，把爬虫伪装成浏览器，键值对需要加上''
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
'cookie': 'cna=qUyhGOotbz8CAbfKgpe41DnI; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _m_h5_tk=b7a320068aa0035ffb6d2c17be791796_1615192214309; _m_h5_tk_enc=1844b390521ecfeb95667372f955974c; t=0c8ae44b085f6b0ec780c7663cf8f121; _tb_token_=f1ee83ee30b4e; _samesite_flag_=true; cookie2=1690450b279c4105076d6c3aa73f4479; xlly_s=1; sgcookie=E100HOeeovLvSO51TnzOINLYDLtJk8vMq909ROdxtyyvSy8HTmFJ6hr5cwJ1sOispdcE4WBoJJ4i7q2dwKC88ZUJfw%3D%3D; uc3=vt3=F8dCuAVkEbBM0lFqUVk%3D&lg2=URm48syIIVrSKA%3D%3D&nk2=F5RBwfH8m48kg2RD&id2=UUphy%2FZybznDgQD12g%3D%3D; csg=eb4b8f07; lgc=tb4425496033; dnk=tb4425496033; skt=a0f2478d8b25c118; existShop=MTYxNTE4MTgyNw%3D%3D; uc4=nk4=0%40FY4KpC4lbzn8m3Y7jIzCfZWz7Lk%2F0iw%3D&id4=0%40U2grEJGNHKhr6d0BoN8rT0JXDZHuyFr6; tracknick=tb4425496033; _cc_=VFC%2FuZ9ajQ%3D%3D; mt=ci=44_1; enc=%2FCczcv4EZvgpiRnm0hq3OS93MP7tLE3bGptsdQzFhGORjLraDtqtFlJuUncPkyAUPgOYR3nrIvbfpEdhdt3lJpQ%2Bp0X66%2BT2VQbPGBOj3xk%3D; v=0; uc1=cookie21=W5iHLLyFe3xm&pas=0&cookie14=Uoe1hxgQNFKz%2Fg%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false; tfstk=c1GCBOgKoMjBcPvPT2TNa7amHcNCayJ_WpZZRx68HaDDsI3UXsmCgoaN-Yj16-U1.; l=eB_O_oS7jE0NDmzvBO5aourza779wIRbzsPzaNbMiIncC6ffwWJt9TxQD0w1yKKRR8XcMLYB4sz4jMwT2ek_JyTXlj6iuXOi8dopBef..; isg=BAwM0vzDgBq2lJQ8wbF8DlED3Wo-RbDvTRmMOWbNqrfX8a77jlQbf_0HkflJuehH'
}
base_url='https://rate.taobao.com/feedRateList.htm?'
def get_page(url):
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except Exception as e:
        print(e)

def get_info(page):
    try:
        items=re.findall(r'"content":"(.*?)"',page,re.S)
        for item in items:
            yield item
    except Exception as e:
         print(e)

def save_data(datas):
    with open("评论.txt","a",encoding="utf-8") as f:
        for data in datas:
            f.write(data)
            print(data)
            f.write('\n')
        f.close()


urls=[base_url.format(i) for i in range(1,11)]
for url in urls:
    page=get_page(url)
    print(url)
    datas=get_info(page)
    save_data(datas)

print("爬取成功！请查看当前文件夹的comment.txt!")
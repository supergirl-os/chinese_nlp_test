import requests
from bs4 import BeautifulSoup as bs
import json
import csv
import re
import time

COMMENT_PAGE_URL = []
# 生成链接列表
def Get_Url(num):
    urlFront = 'https://rate.tmall.com/list_detail_rate.htm?itemId=623346006409&spuId=1750654460&sellerId=1714128138&order=3&currentPage='
    urlRear = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvcQvbvnpvUvCkvvvvvjiWPL5Ogjlhn2MUQjEUPmPZtjlUPLFWtjtbPFF9QjDRRvhvCvvvphvgvpvhvvCvpvgCvvpvvPMMvvhvC9mvphvvvU9CvvOCvhE2gWmIvpvUvvCCRfFEf17gvpvIvvCvpvvvvvvvvh8TvvvCIvvvBZZvvvHIvvCHBpvvvxpvvhxHvvvCxv9CvhQmO40rjah65tyXayPIgE%2B4VCO0747BhCka%2BoHoDOm4jLeAnhjEKBmAdX3z8SLrPC0Adcpi%2BRZa%2Bu6OjLjBTC97bC6DNrClHuQa%2B3%2Bdi9hvCvvvpZoVvpvhvUCvpUvCvvswMv1NvnMwznsarlI%3D&needFold=0&_ksTS=1615686985909_795&callback=jsonp796'
    for i in range(0, num):
        COMMENT_PAGE_URL.append(urlFront + str(1 + i) + urlRear)


# 获取评论数据
def GetInfo(num):
    # 定义需要的字段
    nickname = []
    auctionSku = []
    ratecontent = []
    ratedate = []
    # 循环获取每一页评论
    headers = {
        'cookie': 'hng=CN%7Czh-CN%7CCNY%7C156; lid=tb4425496033; enc=%2FCczcv4EZvgpiRnm0hq3OS93MP7tLE3bGptsdQzFhGORjLraDtqtFlJuUncPkyAUPgOYR3nrIvbfpEdhdt3lJpQ%2Bp0X66%2BT2VQbPGBOj3xk%3D; cna=qUyhGOotbz8CAbfKgpe41DnI; xlly_s=1; dnk=tb4425496033; uc1=pas=0&cookie15=URm48syIIVrSKA%3D%3D&cookie21=W5iHLLyFe3xm&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie14=Uoe1hx8xO1%2FFtA%3D%3D; uc3=vt3=F8dCuAotWDpk0HY4D0E%3D&id2=UUphy%2FZybznDgQD12g%3D%3D&nk2=F5RBwfH8m48kg2RD&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=tb4425496033; _l_g_=Ug%3D%3D; uc4=nk4=0%40FY4KpC4lbzn8m3Y7jIzCfZW0neznfgw%3D&id4=0%40U2grEJGNHKhr6d0BoN8rT0JXCq8E4ecy; unb=2201480757263; lgc=tb4425496033; cookie1=VWfFHBXtxklwndzh8yC6eZ28y4gvX%2FtfgqTlJ%2FRgkJA%3D; login=true; cookie17=UUphy%2FZybznDgQD12g%3D%3D; cookie2=186b33032487703a90aa2593e6b8781d; _nk_=tb4425496033; sgcookie=E100bWuk%2Fvs4SA3jolvWehM%2BNQ5dsO589WL%2FPV6nh0lEh35N%2BCW6nv5nhy6Y1I%2Fq%2BTbekURMaqQBTCums45As%2BsILA%3D%3D; sg=337; t=0c8ae44b085f6b0ec780c7663cf8f121; csg=7f1ee2b6; _tb_token_=e873e553533e5; _m_h5_tk=9d14f632e00cc8141ebc4f3163b3eba9_1615695882105; _m_h5_tk_enc=13c8fe2d633c37273da3c53fbce0c7bc; x5sec=7b22726174656d616e616765723b32223a22646638363335613138303036653535666666306162356531613065636363636143494c6174594947454e363436646537744a617a30674561447a49794d4445304f4441334e5463794e6a4d374d5367434d4f32352f397a2b2f2f2f2f2f77453d227d; l=eBgkDvNejYitR7r8BOfZourza77OjIRbnuPzaNbMiOCPO41W5nDhW6NIDQLXCnGVnsODR354uljQBjY3qyUClZXRFJXn9MptndLh.; isg=BGRk2e8h2JqXWCxe-8R0fyMUNWJW_YhntdFUIX6F_y_2KQXzpgwk9xuP6YExy8C_; tfstk=cl0RBNiSbKvoK3Nx_0KcOmhdmYDdZZ78p_wNJQHEzNuen7QdiN3iWcZMV5B8kIC..',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.5cb15c9czickYw&id=623346006409&skuId=4588731727284&areaId=510100&user_id=1714128138&cat_id=50024400&is_b=1&rn=4e8c2a5c8f9b74d45bae08086cb91704',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    for i in range(num):
        # 头文件，没有头文件会返回错误的js
        params={
            'itemId': '623346006409',
            'spuId': '1750654460',
            'sellerId': '1714128138',
            'currentPage': i,
            'callback': 'jsonp796'
        }
        # 解析JS文件内容
        content= requests.get(COMMENT_PAGE_URL[i], params,headers=headers).text[12:-1]
        #result=json.loads(content)
        #print(result)
        #time.sleep(10)
        nk = re.findall('rateContent":"(.*?)"', content)
        nickname.extend(nk)
        print(nk)
       # auctionSku.extend(re.findall('"auctionSku":"(.*?)"', content))
        #ratecontent.extend(re.findall('"rateContent":"(.*?)"', content))
        #ratedate.extend(re.findall('"rateDate":"(.*?)"', content))
    # 将数据写入TEXT文件中
    for i in list(range(0, len(nickname))):
        text = nickname[i]+ '\n'
        with open("../texts/text_tmall.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            print(i + 1, ":写入成功")


# 主函数
if __name__ == "__main__":
    Page_Num = 200
    Get_Url(Page_Num)
    GetInfo(Page_Num)
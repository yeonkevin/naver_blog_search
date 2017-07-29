import requests
from bs4 import BeautifulSoup
from itertools import count
from collections import OrderedDict

def blog_search(q, max_page=None):
    url = 'https://search.naver.com/search.naver?'
    post_dict = OrderedDict()
    for page in count(1):
        params = {
            'where' : 'post',
            'query' : q,
            'start' : (page - 1) * 10 + 1,
        }
    
        html = requests.get(url, params=params).text
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = soup.select('.sh_blog_title')
        tag_list2 = soup.select('dd.txt_inline')
        dic = {1: tag_list, 2: tag_list2}

        for tag in tag_list:
            if tag['href'] in post_dict:
                return None

            print(tag.text, tag['href'])
            post_dict[tag['href']] = tag.text
        
        if max_page and (page >= max_page):
            break
    

blog_search('"yeonkevin"', 5)
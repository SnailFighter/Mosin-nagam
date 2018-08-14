#!/usr/bin/python
# -*- coding: utf-8 -*-

# 写个小栗子，抓取百度一个连接

from bs4 import BeautifulSoup
import requests
import re



def get_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


# dict_key 为字典类型，值也是字典类型
dict_key = {}


def search_info(product_name):
    product_name = product_name.strip()
    product_name_array = product_name.split(" ")
    if len(product_name_array) > 1:
        product_name = ""
        for name in product_name_array:
            if product_name!="":
                product_name = product_name + "_" + name
            else:
                product_name = name

    for n in range(5):
        url = "https://www.alibaba.com/products/" + product_name + ".html?IndexArea=product_en&page="+str(n);
        print(url)
        soup = get_html(url)
        url_list = []

        for x in soup.findAll("a", href=re.compile(".*.product-detail.*")):
            url_list.append(x['href'][2:])

        # find keywords

        for x in url_list:
            soup = get_html('https://' + x)
            keyword = soup.find("meta", attrs={"name": "keywords"})['content']
            company_info = soup.find("a", attrs={"class": "company-name"})

            print(keyword)
            str_array = keyword.split(",")
            for y in str_array:
                if hash(y) in dict_key.keys():
                    item = dict_key[hash(y)]  # get element
                    time = item["time"] + 1
                    item["time"] = time
                else:
                    item = {"key": y, "time": 1, "company": company_info['title'], "url": company_info['href']}
                    dict_key[hash(y)] = item

    return dict_key










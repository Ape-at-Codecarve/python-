from selenium_func import *
import selenium_func
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os

def re_much_css_selectsXigua_search(_selector,_position,_start_num,_end_num):# 根据选择器的child数字定位多个元素，并返回列表,需要确保child在1到9之间
    box_elements = []

    for i in range(_start_num,_end_num+1):
        try:
            list_selector = list(_selector)
            list_selector[_position] = f'{i}'
            current_selector = ''.join(list_selector)

            box_elements.append(re_css_select(current_selector))
        except Exception:
            return None

    return box_elements

def re_much_css_selectsXigua(_selector,_position,_start_num,_end_num):# 根据选择器的child数字定位多个元素，并返回列表,需要确保child在1到9之间
    box_elements = []

    for i in range(_start_num,_end_num+1):
        try:
            list_selector = list(_selector)
            list_selector[_position] = f'{i}'
            current_selector = ''.join(list_selector)

            box_elements.append(re_css_select(current_selector))
        except Exception:
            return None

    return box_elements

def re_LoopGet_attr(_element_box,_attr_name):# 接收一个元素列表和该元素的属性名称，遍历提取元素的属性值
    ForReturn_box = []
    for i in _element_box:
        ForReturn_box.append(re_get_attribute(i,_attr_name))
    return ForReturn_box

def op_ShaiXuan(_selector1,_selector2,_selector3,):
    安全点击元素(_selector1)
    安全点击元素(_selector2)
    安全点击元素(_selector3)
def op_进入Seed页面(_title):
    if '%' in _title:
        _title = _title.replace('%','%25')
    op_go_to_page(f'https://www.ixigua.com/search/{_title}','西瓜视频')
    op_ShaiXuan(
        "#App > div > main > div > div > div:nth-child(1) > div > div.searchPageV2__tabs > div > div > span > span",
        "#App > div > main > div > div > div:nth-child(1) > div > div.searchPageV2__header-categories-anim > div > div:nth-child(1) > ul > li:nth-child(2)",
        "#App > div > main > div > div > div:nth-child(1) > div > div.searchPageV2__header-categories-anim > div > div:nth-child(2) > ul > li:nth-child(4)"
    )

    wait_chao1()
    op_scroll_to_down()
    wait_chao2()
def redChar_check(_box_InfoElement,_start_num,_end_num,_redChar_rate):
    bool_box = []
    for x in range(_start_num,_end_num+1):
        length = 0
        for y in range(1,65535):
            lis_sel = list('#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(6) > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > a > span > i:nth-child(1)')
            lis_sel[114] = f'{x}'
            lis_sel[221] = f'{y}'
            selector = ''.join(lis_sel)
            try:
                element = re_css_select(selector)
                length += len(element.text)
                continue
            except Exception:
                break
        if length/len(_box_InfoElement[x-1].get_attribute('title')) >= _redChar_rate:
            bool_box.append(True)
        else:
            bool_box.append(False)
    return bool_box
def ViewTime_check(_start_num,_end_num):
    box = []
    for i in range(_start_num,_end_num+1):
        lis_sel = list("#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(1) > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > div.HorizontalFeedCard__bottomInfo.color-content-secondary > div > span")
        lis_sel[114] = f'{i}'
        selector = ''.join(lis_sel)
        element = selenium_func.driver.find_element(By.CSS_SELECTOR,selector)
        box.append(element.text)
    return box

def op_write(_title,_src,_hrefBox,_addr,_index):

    global a
    a = _title[_index]
    while True:
        if '\\' in a:
            a.replace('\\','')
            continue
        elif '/' in a:
            a.replace('/','')
            continue
        elif ':' in a:
            a.replace('：','')
            continue
        elif '*' in a:
            a.replace('*','')
            continue
        elif '?' in a:
            a.replace('？','')
            continue
        elif '\"' in a:
            a.replace('\"','')
            continue
        elif '<' in a:
            a.replace('<','')
            continue
        elif '>' in a:
            a.replace('>','')
            continue
        elif '|' in a:
            a.replace('|','')
            continue
        break
    src_file = open(f'{_addr}/封面/{len(os.listdir("C:/爬取的信息/封面"))+1}.{a}.jpg','wb')
    r = requests.get(_src[_index])
    src_file.write(r.content)
    src_file.close()

    file = open(f'{_addr}/爬取的链接.txt','a')
    file.write(f'{len(os.listdir("C:/爬取的信息/封面"))}.{_title[_index]}\n')
    for _i in range(6):
        file.write(f'{_hrefBox[_i]}\n')
    file.close()

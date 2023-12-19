from selenium_func import *
from xigua_func import *
import For_choose
import For_write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

redChar_rate = 0.3
def start(author_url,_start,_end):
    op_start()

    op_go_to_page(author_url,'西瓜视频')

    while True:
        SeedsElement_box = re_much_css_selectsXigua(
            "#App > div > main > div > div.userDetailV3__content > div:nth-child(1) > div:nth-child(2) > div.userDetailV3__main__list > div:nth-child(6) > div.HorizontalFeedCard__coverContainer > a > div.tt-img-wrapper > img",
            137,
            _start,
            _end
        )
        if SeedsElement_box == None:
            op_scroll_to_down()
            continue
        else:
            break

    ForWrite_SeedsTitle = re_LoopGet_attr(SeedsElement_box,"alt")
    ForWrite_SeedsSrc = re_LoopGet_attr(SeedsElement_box,"src")

    w_index = -1
    for i in ForWrite_SeedsTitle:
        w_index += 1
        try:
            op_进入Seed页面(i)
        except Exception:
            print('搜索到的结果少于16个，下一个...')
            continue
        box_InfoElement = re_much_css_selectsXigua_search(
            "#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(5) > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > a",
            114,1,16
        )
        if box_InfoElement == None:
            continue
        For_choose.redChar = redChar_check(box_InfoElement,1,16,redChar_rate)
        For_choose.ViewTime = ViewTime_check(1,16)
        For_choose.ViewTime = For_choose.a(For_choose.ViewTime)
        hrefBox = []
        for index in range(16):
            if For_choose.redChar[index] and For_choose.ViewTime[index]:
                hrefBox.append(box_InfoElement[index].get_attribute('href'))
            else:
                continue

        if len(hrefBox) >= 6:
            pass
        else:
            print('最终筛选出的结果少于6个,下一个')
            continue
        try:
            op_write(ForWrite_SeedsTitle,ForWrite_SeedsSrc,hrefBox,'C:/爬取的信息',w_index)
        except Exception:
            os.remove(f'C:/爬取的信息/封面/{len(os.listdir("C:/爬取的信息/封面"))}.{xigua_func.a}')
            continue
    driver = 0

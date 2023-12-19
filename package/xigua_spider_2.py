from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import ctime
from time import sleep
import requests
'''
def split_ctime(ctime_variable):
    lis = ctime_variable.split(' ')
    return lis[3]
'''
'''
def sub_time(A,B):
    A_hour,A_min,A_second = A.split(':')
    B_hour,B_min,B_second = B.split(':')
    A_hour=int(A_hour);A_min=int(A_min);A_second=int(A_second)
    B_hour=int(B_hour);B_min=int(B_min);B_second=int(B_second)

    if B_second >= A_second:
        C_second = B_second - A_second
    else:
        C_second = 60 - (A_second - B_second)
        B_min -= 1

    if B_min >= A_min:
        C_min = B_min - A_min
    else:
        C_min = 60 - (A_min - B_min)
        B_hour -= 1

    if B_hour >= A_hour:
        C_hour = B_hour - A_hour
    else:
        C_hour = 60 - (A_hour - B_hour)

    C_hour=str(C_hour);C_min=str(C_min);C_second=str(C_second)
    C_time = [C_hour,C_min,C_second]
    return ':'.join(C_time)
'''
def go_to_author_page():  # 去往作者页面
    global driver,\
           author_url,\
           wait,\
           wait_element,\
           A_time


    print(f'预计花费{round((-spider_times_a+spider_times_b+1)/12,2)}分钟，即将唤起浏览器，请不要与浏览器交互,绝对要保持浏览器为激活状态')
    #A_time = split_ctime(ctime())
    driver = webdriver.Edge()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(author_url)
    wait_element = wait.until(EC.title_contains("西瓜视频"))
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, f'#App > div > main > div > div.userDetailV3__content > div:nth-child(1) > div:nth-child(2) > div.userDetailV3__main__list > div:nth-child({spider_times_b}) > div.HorizontalFeedCard__coverContainer > a > div.tt-img-wrapper > img')
            break
        except Exception:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(2)

def loop_get_search_seeds(times_a,times_b):  # 循环爬取作者页面的标题和src
    global author_css_selector,\
           list_author_css_selector,\
           author_element,\
           author_title, author_src,\
           author_title_box, author_src_box



    author_title_box = []
    author_src_box = []
    author_css_selector = "#App > div > main > div > div.userDetailV3__content > div:nth-child(1) > div:nth-child(2) > div.userDetailV3__main__list > div:nth-child(1) > div.HorizontalFeedCard__coverContainer > a > div.tt-img-wrapper > img"
    list_author_css_selector = list(author_css_selector)

    for i in range(times_a, times_b + 1):
        list_author_css_selector[137] = f"{i}"
        author_css_selector = "".join(list_author_css_selector)
        list_author_css_selector[137] = f"{1}"
        author_element = driver.find_element(By.CSS_SELECTOR, author_css_selector)


        author_title = author_element.get_attribute("alt")
        print(author_title)
        author_title_box.append(author_title)

        author_src = author_element.get_attribute("src")
        print(author_src)
        author_src_box.append(author_src)


def loop_search_from_seeds_title():
    global search_css_selector, \
           list_search_css_selector,\
           author_boxes_index,\
           write_txt_link,\
           write_txt_title,\
           落选的数量


    author_boxes_index = -1
    search_css_selector = "#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(5) > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > a"
    list_search_css_selector = list(search_css_selector)

    write_txt_link = []
    write_txt_title = []

    落选的数量 = 0
    for i in author_title_box: # mainloop
        author_boxes_index += 1
        if '%' in i:
            percent_index = -1
            for o in i:
                percent_index += 1
                if o == '%':
                    i = list(i)
                    i[percent_index] = '%25'
                    i = ''.join(i)
        print(f"####正在搜索[{i}]({author_boxes_index+spider_times_a}/{spider_times_b})当前有({落选的数量})个不合格...####")
        driver.get(
            f"https://www.ixigua.com/search/{i}/?logTag=1e46bd88848752c2f91a&tab_name=pgc&fss=default_search"
        )
        print(EC.title_contains("西瓜视频"))
        wait_element = wait.until(EC.title_contains("西瓜视频"))
        print(EC.title_contains("西瓜视频"))
        # 筛选，最热，10~30分钟
        shai_xuan()
        try:
            error_element = driver.find_element(By.CSS_SELECTOR, '#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(16) > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > a')
        except Exception:
            落选的数量 += 1
            print('搜索到的结果过少，搜索下一个标题')
            author_title_box[author_boxes_index] = 'wait_to_be_deleted'
            author_src_box[author_boxes_index] = 'wait_to_be_deleted'
            continue

        subloop_get_search_title_and_link(16)

        delete_current_box()

################################################################################
                                                                               #
                                                                               #
        if len(current_title_box) >= 6:                                        #
            write_txt_title.append(current_title_box)                          #
            write_txt_link.append(current_link_box)                            #
                                                                               #
        else:                                                                  #
            落选的数量 += 1
            author_title_box[author_boxes_index] = 'wait_to_be_deleted'        #
            author_src_box[author_boxes_index] = 'wait_to_be_deleted'          #
            print('合格的数量少于6个，搜索下一个标题')                               #
            continue                                                           #
################################################################################

def subloop_get_search_title_and_link(times):
    global search_element,\
           current_title_box,\
           current_link_box,\
           red_char_selector,\
           list_red_char_selector,\
           red_char_index,\
           red_char_length_total,\
           red_char_bool,\
           i


    current_title_box = []
    current_link_box = []
    red_char_selector = '#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(3) > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > a > span > i:nth-child(1)'
    list_red_char_selector = list(red_char_selector)
    red_char_index = 0
    red_char_length_total = 0

    for i in range(1, times + 1):

        list_search_css_selector[114] = f"{i}"
        search_css_selector = "".join(list_search_css_selector)
        list_search_css_selector[114] = f"{1}"


        search_element = driver.find_element(By.CSS_SELECTOR, search_css_selector)
        search_title = search_element.get_attribute("title")
        for x in range(65535):
            red_char_index += 1
            list_red_char_selector[221] = f'{red_char_index}'
            list_red_char_selector[114] = f'{i}'
            red_char_selector = ''.join(list_red_char_selector)
            list_red_char_selector[221] = f'{1}'
            list_red_char_selector[114] = f'{1}'

            try:
                red_char_element = driver.find_element(By.CSS_SELECTOR, red_char_selector)

                red_char_length_total += len(red_char_element.text)
            except Exception:
                if red_char_length_total/len(search_title) >= 0:
                    red_char_bool = True
                    break
                else:
                    red_char_bool = False
                    break
        red_char_index = 0
        red_char_length_total = 0

        views_times_selector = '#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(3) > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > div.HorizontalFeedCard__bottomInfo.color-content-secondary > div > span'
        list_views_times_selector = list(views_times_selector)
        char_box = []

        list_views_times_selector[114] = f'{i}'
        views_times_selector = ''.join(list_views_times_selector)
        list_views_times_selector[114] = f'{1}'

        views_and_times_element = driver.find_element(By.CSS_SELECTOR, views_times_selector)
        before, sep, after = views_and_times_element.text.partition('·')
        for i in before:
            if i == '次':
                views_string = ''.join(char_box)
                char_box = []
                break
            else:
                char_box.append(i)

        if '万' in views_string:
            views_bool = True
        else:
            if int(views_string) >= 1000:
                views_bool = True
            else:
                views_bool = False

        if '周' in after or '月' in after or '年' in after:
            times_bool = True
        elif '时' in after or '天' in after:
            times_bool = False
        if views_bool and times_bool:
            views_times_bool = True
        else:
            views_times_bool = False

        if red_char_bool and views_times_bool:

            current_title_box.append(search_title)

            search_link = search_element.get_attribute("href")

            current_link_box.append(search_link)
        else:
            continue

def shai_xuan():
    shai_xuan_element = driver.find_element(
        By.CSS_SELECTOR,
        "#App > div > main > div > div > div:nth-child(1) > div > div.searchPageV2__tabs > div > div > span",
    )
    shai_xuan_element.click()
    zui_re_element = driver.find_element(
        By.CSS_SELECTOR,
        "#App > div > main > div > div > div:nth-child(1) > div > div.searchPageV2__header-categories-anim > div > div:nth-child(1) > ul > li:nth-child(2)",
    )
    while True:
        try:
            zui_re_element.click()
            break
        except Exception:
            continue
    _10_30_mins_element = driver.find_element(
        By.CSS_SELECTOR,
        "#App > div > main > div > div > div:nth-child(1) > div > div.searchPageV2__header-categories-anim > div > div:nth-child(2) > ul > li:nth-child(4)",
    )
    _10_30_mins_element.click()

    wait.until(
        lambda driver: driver.find_element(By.CSS_SELECTOR,
        '#App > div > main > div > div > div.searchPageV2__content > div').get_attribute('class')=='searchPageV2__tab-component'
    )
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    waiting = WebDriverWait(driver,5)
    try:
        waiting.until(
            lambda driver: driver.find_element(By.CSS_SELECTOR,
            '#App > div > main > div > div > div > div > div.Feed-footer > div').get_attribute('class')=='Loading-2 light'
        )
    except Exception:
        pass
def delete_current_box():
    while 'wait_to_be_deleted' in current_title_box:
        current_title_box.remove('wait_to_be_deleted')
        current_link_box.remove('wait_to_be_deleted')

def delete_author_box():
    while 'wait_to_be_deleted' in author_title_box:
        author_title_box.remove('wait_to_be_deleted')
        author_src_box.remove('wait_to_be_deleted')

def write_to_txt():
    global file_titles_and_links

    for i in range(65535):

        if open(f'C:/爬取的信息/文本文件/{i+1}.视频标题和链接.txt',
                'r',
                encoding = 'utf-8'
                ).read() == '':
            file_titles_and_links = open(f'C:/爬取的信息/文本文件/视频标题和链接.txt','w',encoding = 'utf-8')
            file_titles_and_links = open(f'C:/爬取的信息/文本文件/视频标题和链接.txt','a',encoding = 'utf-8')
        else:
            continue


    for i in range(start_num,start_num+len(write_txt_title)):
        file_titles_and_links.write(f'{i+1}.{author_title_box[i-start_num]}\n')
        for x in range(6):
            file_titles_and_links.write(f'{write_txt_link[i-start_num][x]}\n')

def views_and_times():
    global views_times_bool

def write_to_jpg():
    for i in range(start_num,start_num+len(write_txt_title)):
        res = requests.get(author_src_box[i-start_num])
        file_jpg = open(f'C:/爬取的信息/封面/{i+1}.{author_title_box[i-start_num]}.jpg', 'wb')
        file_jpg.write(res.content)

def op_write_xlsx(_pos,_content):
    sheet_I[_pos] = _content


def launch(can_shu1,can_shu2):#要爬取博主的第几个到第几个视频？\n>>>
    global spider_times_a,spider_times_b,\
           start_num

    spider_times = can_shu1
    spider_times_a,spider_times_b = spider_times.split(' ')
    spider_times_a = int(spider_times_a)
    spider_times_b = int(spider_times_b)

    start_num = can_shu2#输入序号\n>>>
    start_num = int(start_num)


    # TO DO:去往作者页面
    go_to_author_page()
    # TO DO:在当前页面爬取标题种子,并装进box变量中
    loop_get_search_seeds(spider_times_a,spider_times_b)
    # TO DO:循环搜索
    loop_search_from_seeds_title()

    delete_author_box()

    write_to_txt()

    file_titles_and_links.close()

    write_to_jpg()

    print(f'从{spider_times_a}到{spider_times_b}中,筛选出了{len(write_txt_title)}个合格的，有{落选的数量}个不合格\n\
    合格率为{round(len(write_txt_title)*100/spider_times_b-spider_times_a+1,4)}'+'%')
    #B_time = split_ctime(ctime())
    #the_time = sub_time(A_time,B_time)
    #a,b,c = the_time.split(':')
    #print(f'耗时{a}时{b}分{c}秒')

    driver.quit()
author_url = input("提供西瓜视频作者的url\n>>>")

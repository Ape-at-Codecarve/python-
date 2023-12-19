from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def re_get_attribute(_element,_attribute_name):
    return _element.get_attribute(_attribute_name)

def op_scroll_to_down():# 下滑到页面最底端
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

def op_start():# 启动浏览器,创建wait对象
    global driver,wait
    driver = webdriver.Edge()
    wait = WebDriverWait(driver,10)
    driver.maximize_window()

def op_go_to_page(self_url,_page_header_string):# 去往一个页面,会等待
    driver.get(self_url)
    try:
        wait.until(EC.title_contains(_page_header_string))
    except Exception:
        print('WARNING:页面加载超时!!!')
        time.sleep(5)

def re_css_select(self_selector):# 根据选择器定位一个元素，并返回
    element = driver.find_element(By.CSS_SELECTOR, self_selector)
    return element


def re_much_css_selects(_selector,_position,_start_num,_end_num):# 根据选择器的child数字定位多个元素，并返回列表,需要确保child在1到9之间
    box_elements = []

    for i in range(_start_num,_end_num+1):
        try:
            list_selector = list(_selector)
            list_selector[_position] = f'{i}'
            current_selector = ''.join(list_selector)

            box_elements.append(re_css_select(current_selector))
        except Exception:
            print('WARNING:元素定位失败!!!')
            time.sleep(5)
            continue

    return box_elements

def 安全点击元素(_selector): # 参数:一个CSS选择器
    element = re_css_select(_selector)
    while True:
        try:
            element.click()
            break
        except Exception:
            continue

def re_更改selector的child数字(_selector,_position,_child数字):
    list_selector = list(_selector)
    print(list_selector[_position])
    list_selector[_position] = f'{_child数字}'
    _selctor = ''.join(list_selector)
    return _selector

def re_更改selector的child数字并且将其定位(_selector,_position,_child数字):
    list_selector = _selector
    list_selector[_position] = f'{_child数字}'
    _selctor = ''.join(list_selector)
    element = re_css_select(_selctor)
    return element

def wait_chao1():
    wait.until(
    lambda driver: driver.find_element(By.CSS_SELECTOR,
    '#App > div > main > div > div > div.searchPageV2__content > div').get_attribute('class')=='searchPageV2__tab-component'
)
def mod_wait(self):
    try:
        driver.find_element(By.CSS_SELECTOR,"#App > div > main > div > div > div.searchPageV2__content > div > div.searchPageV2__complex > div > div:nth-child(16) > div.HorizontalFeedCard__coverContainer > a > div.tt-img-wrapper > img")
        return True
    except Exception:
        return False

def wait_chao2():
    waiting = WebDriverWait(driver,5)
    waiting.until(mod_wait)
def op_quit():
    driver.quit()

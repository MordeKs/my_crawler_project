# -*- encoding: utf-8 -*-
"""
@File    : kanzhun.py
@Time    : 2020/8/18 9:16
@Author  : Morde
@Software: PyCharm
@Description: 看准网
"""
import requests
from selenium import webdriver
import time
import random

from selenium.webdriver.common.keys import Keys


class Kanzhun:
    def __init__(self):
        proxy = "http://10.2.1.31:8070"
        # self.browser_options = webdriver.ChromeOptions()
        self.browser_options = webdriver.FirefoxOptions()
        self.browser_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0')
        self.browser_options.add_argument('--user-data-dir=C:/Program Files/Mozilla Firefox/User Data')
        # self.browser_options.add_argument('--headless')
        # self.browser_options.add_argument('--disable-gpu')
        # self.browser_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # self.browser = webdriver.Chrome(chrome_options=self.browser_options)
        self.browser = webdriver.Firefox(firefox_options=self.browser_options, proxy=proxy)
        self.browser.set_page_load_timeout(15)

    def login(self):
        try:
            self.browser.get('https://www.kanzhun.com/')
        except:
            self.browser.execute_script('window.stop()')
        self.browser.find_element_by_xpath('//div[@class="btn-login"]/a').click()
        time.sleep(3)
        # 切换为账号登录
        self.browser.find_element_by_xpath('//div[@class="tabs_nav clearfix"]/a[2]').click()
        time.sleep(2)
        # 切换为用户名密码登录
        self.browser.find_element_by_xpath('//a[@class="js-password-login"]').click()
        time.sleep(2)
        # 切换为邮箱登录
        self.browser.find_element_by_xpath('//input[@class="js-toggle-email-login"]').click()
        time.sleep(2)
        self.browser.switch_to.active_element.send_keys(Keys.TAB)
        # self.browser.find_element_by_name('account').send_keys('240427721@qq.com')
        # self.browser.find_element_by_name('password').send_keys('351496116Gjh')
        self.browser.switch_to.active_element.send_keys('240427721@qq.com')
        time.sleep(0.3)
        self.browser.switch_to.active_element.send_keys(Keys.TAB)
        self.browser.switch_to.active_element.send_keys(Keys.TAB)
        self.browser.switch_to.active_element.send_keys('351496116Gjh')
        time.sleep(0.3)
        on_element = self.browser.find_element_by_id('nc_6_n1z')
        # 获取验证拖动的长度
        width = self.browser.find_element_by_id('nc_6_n1t').size['width']
        try:
            self.slide(on_element, width)
            # webdriver.ActionChains(self.browser).drag_and_drop_by_offset(on_element, width, 0).perform()
        except Exception as e:
            self.browser.execute_script('window.stop()')
            # self.browser.close()


    def slide(self, slider, distance):
        """
        滑动验证
        """
        # 鼠标点击并按住不松
        webdriver.ActionChains(self.browser).click_and_hold(slider).perform()
        # webdriver.ActionChains(self.browser).move_by_offset(xoffset=0, yoffset=100).perform()
        # 设置滑动距离
        tracks = self.get_track(distance)
        time.sleep(0.15)
        for item in tracks:
            webdriver.ActionChains(self.browser).move_by_offset(xoffset=item, yoffset=random.randint(-2, 2)).perform()
        # 稳定一秒再松开
        time.sleep(1)
        webdriver.ActionChains(self.browser).release(slider).perform()

    @staticmethod
    def get_track(distance):
        '''
        拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
        匀变速运动基本公式：
        ①v=v0+at
        ②s=v0t+(1/2)at²
        ③v²-v0²=2as
        :param distance: 需要移动的距离
        :return: 存放每0.2秒移动的距离
        '''
        # 初速度
        v = 0
        # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
        t = 0.3
        # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
        tracks = []
        # 当前的位移
        current = 0
        # 到达mid值开始减速
        mid = distance * 5 / 8

        distance += 10  # 先滑过一点，最后再反着滑动回来
        # a = random.randint(1,3)
        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
                a = random.randint(25, 30)  # 加速运动
            else:
                a = -random.randint(1, 3)  # 减速运动

            # 初速度
            v0 = v
            # 0.2秒时间内的位移
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表
            tracks.append(round(s))

            # 速度已经达到v,该速度作为下次的初速度
            v = v0 + a * t

        # 反着滑动到大概准确位置
        for i in range(4):
            tracks.append(-random.randint(1, 3))
        # for i in range(4):
        #    tracks.append(-random.randint(1,3))
        random.shuffle(tracks)
        return tracks


if __name__ == '__main__':
    k = Kanzhun()
    k.login()


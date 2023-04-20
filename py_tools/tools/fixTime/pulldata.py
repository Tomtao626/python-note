from pyquery import PyQuery as Pq
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
chrome_options = webdriver.ChromeOptions()
# 无窗口模式
chrome_options.add_argument('--headless')
# 禁止硬件加速，避免严重占用cpu
chrome_options.add_argument('--disable-gpu')
# 关闭安全策略
chrome_options.add_argument("disable-web-security")
# 禁止图片加载
chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
# 隐藏Chrome正在受到自动软件的控制
chrome_options.add_argument('disable-infobars')
# no sandbox
chrome_options.add_argument('--no-sandbox')
# 设置开发者模式启动，该模式下webdriver属性为正常值
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

browser = webdriver.Chrome(options=chrome_options,
                           executable_path="/Users/tao626/Documents/workspaces/selenium_driver_path/mac/chromedriver")

browser.get('https://time.is/Baranya')

doc = Pq(browser.page_source)

print(doc('.infobox').text().split(" ")[-1].replace(".", ""))



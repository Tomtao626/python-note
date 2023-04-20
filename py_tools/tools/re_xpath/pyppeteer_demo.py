import asyncio
from pyppeteer import launch
import random
def screen_size():
    # 使用tkinter获取屏幕大小
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height
async def main():
    # 建立一个浏览器对象
    browser = await launch(headless=False)
    # 打开新的标签页
    page = await browser.newPage()
    # 设置网页视图大小
    width, height = screen_size()
    await page.setViewport(viewport={'width': width, 'height': height})
    # 访问目标url网页
    await page.goto('https://www.baidu.com/', options={'timeout': 5 * 1000})
    # 休眠
    await asyncio.sleep(10)
    # 对当前页面截图并保存为example1.png
    await page.screenshot({'path': 'example1.png'})
    # 搜索框输入  python Pyppeteer爬虫
    await page.type('#kw', 'python Pyppeteer爬虫')
    # 点击百度一下
    await page.click('#su')
    # 休眠
    await asyncio.sleep(random.randint(1, 3))
    # 对当前页面截图并保存为example2.png
    await page.screenshot({'path': 'example2.png'})
    # 关闭浏览器
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
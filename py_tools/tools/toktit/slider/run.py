import requests
import execjs


def dy_sign(method,kw=None):
    with open('signature.js', 'r', encoding='utf-8') as f:
        b = f.read()
    c = execjs.compile(b)
    d = c.call(method,kw)
    print(d)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.douyin.com/",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    e = requests.get(d, headers=headers)
    return e.text


if __name__ == '__main__':
    # 首页推荐视频
    # print(dy_sign(method='feed'))
    # 搜索视频
    #print(dy_sign(method='search_item',kw='Lx'))
    # 评论
    print(dy_sign(method='cooment',kw='6989198974582263070'))
    # 作品
    #print(dy_sign(method='aweme_post',kw='MS4wLjABAAAAIWFmTfNJmRajbViR_rK6iGgQMIq0lAWdFmQ5z6iU9Vd4uo9KXOgcJE0o5Dn0JAmW'))
    # TODO 其他的自行补充吧
    ...

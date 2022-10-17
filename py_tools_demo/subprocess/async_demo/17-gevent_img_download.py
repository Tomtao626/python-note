import urllib.request
import gevent
from gevent import monkey


monkey.patch_all()

def download_img(img_name,img_url):
	req = urllib.request.urlopen(img_url)

	img_content = req.read()

	with open(img_name, "wb") as f:
		f.write(img_content)


def main():
	gevent.joinall([
			gevent.spawn(download_img, "2.jpg", "http://wx2.sinaimg.cn/mw600/0076BSS5ly1g8t614h42jj30m40x7b29.jpg")
		])


if __name__ == "__main__":
	main()
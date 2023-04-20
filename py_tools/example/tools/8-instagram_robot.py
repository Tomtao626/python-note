# coding:utf-8
# instagram robot

from instabot import Bot

user = dict()

def Upload_Photo(img):
	robot = Bot()
	robot.login(user)
	robot.upload_photo(img, caption="Medium Article")
	print("Photo Uploaded")


def Upload_Video(video):
	robot = Bot()
	robot.login(user)
	robot.upload_video(video, caption="Medium Article")
	print("Video Uploaded")


def Upload_Story(img):
	robot = Bot()
	robot.login(user)
	robot.upload_story(img, caption="Medium Article")
	print("Story Photos Uploaded")


Upload_Photo("img.jpg")
Upload_Video("video.mp4")
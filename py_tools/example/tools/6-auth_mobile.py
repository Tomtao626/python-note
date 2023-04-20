# coding: utf-8
# auto mobile

import subprocess


def main_adb(cm):
	p = subprocess.Popen(cm.split(' '), stdout=subprocess.PIPE, shell=True)
	(output, _) = p.communicate()
	return output.decode('utf-8')


# Swipe
def swipe(x1, y1, x2, y2, duration):
	cmd = f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}"
	return main_adb(cmd)


# Tap or Clicking
def tap(x, y):
	cmd = f"adb shell input tap {x} {y}"
	return main_adb(cmd)


# Make a Call
def make_call(number):
	cmd = f"adb shell am start -a android.intent.action.CALL -d tel:{number}"
	return main_adb(cmd)


# Send SMS
def send_sms(number, message):
	cmd = f"adb shell am start -a android.intent.action.SENDTO -d  sms:{number} --es sms_body '{message}'"
	return main_adb(cmd)


# Download File From Mobile to PC
def download_file(file_name):
	cmd = f'adb pull /sdcard/{file_name}'
	return main_adb(cmd)


# Take a screenshot
def screenshot():
	cmd = 'adb shell screencap -p'
	return main_adb(cmd)


# Power On and Off
def power_off():
	cmd = '"adb shell input keyevent 26"'
	return main_adb(cmd)

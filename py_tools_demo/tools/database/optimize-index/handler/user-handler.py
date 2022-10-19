from db.User import User
import string
import random


def random_str(length=1):
	template = string.ascii_letters + string.digits
	chars = random.sample(template, length)
	return "".join(chars)


def generate_record():
	"""
	username/password/age/sex
	"""
	length = random.randint(6, 20)
	username = f"tom-{random_str(length)}"
	age = random.randint(10, 100)
	return username, age


def create_file(num=10000000):
	for i in range(num):
		# with open("user_data.txt", "w") as f:
		user_name, age = generate_record()
		# 	f.write(",".join(map(str, row)) + "\n")
		user_one = User()
		user_one.user_name = user_name
		user_one.age = age
		user_one.address = "杭州"
		user_one.save()
		print(f"insert one user-{user_one.id}-success")


if __name__ == '__main__':
	import datetime
	start = datetime.datetime.now()
	create_file()
	end = datetime.datetime.now()
	cost = (end - start).total_seconds()
	print("cost: %s" % cost)

import zmq
import time


def run():
    contect = zmq.Context()
    socket = contect.socket(zmq.PUB)
    socket.bind('tcp://*:6666')

    count = 1

    while True:
        time.sleep(1)
        dic = {
            "name": "tomtao626",
            "age": 18
        }
        socket.send_json(dic)
        print(dic)
        count += 1


if __name__ == '__main__':
    run()

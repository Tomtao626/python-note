class IndexError(Exception):

    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return 'dsfsd'
        # return self.message
try:
    name =[]
    name[3]
    # raise TomException('我的异常')  #触发异常
# except TomException as e:
except IndexError as e:
    print(e)

class ResponseCode(object):
    SUCCESS = 0
    FATIL = -1
    NO_RESOURCE_FOUND = 40001
    INVAILD_PARAMETER = 40002
    ACCOUNT_OR_PASSWORD_ERR = 40003


class ResponseMsg(object):
    SUCCESS = "成功"
    FAIL = "失败"
    NO_RESOURCE_FOUND = "未找到资源"
    INVALID_PARAMETER = "参数无效"
    ACCOUNT_OR_PASS_WORD_ERR = "账户或密码错误"


import hashlib

SIGN_KEY = 'feWTYYTHsdfa34821fdsr$R'

class RsaHelper:
    @staticmethod
    def is_sign_msg_verify(encryptStr):
        data = 'key=' + SIGN_KEY
        md5Obj = hashlib.md5()
        md5Obj.update(data.encode("utf-8"))
        h = md5Obj.hexdigest()
        # print(h)
        if(encryptStr == h):
            return True
        else:
            return False




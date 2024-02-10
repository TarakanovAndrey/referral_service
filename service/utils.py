# from service.models import ReferralCode
import random
import string


# def generates_code():
#     flag = False
#     length = 10
#
#     while not flag:
#         items = string.ascii_letters + string.digits
#         code = ''.join(random.choice(items) for _ in range(length))
#
#         return code
#
# print(generates_code())

def generates_code():
    length = 10
    items = string.ascii_letters + string.digits
    code = ''.join(random.choice(items) for _ in range(length))

    return code

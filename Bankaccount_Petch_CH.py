account={"นายA":5000,"นายB":0}

def getBalance():
    print("ยอดเงินคงเหลือในบัญชี :",account)

def deposit(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ต้องป้อนตัวเลขเท่านั้น")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ฝากเงินเข้าในบัญชี A :",money)
    account["นายA"]+=money

def withdraw(money):
    if money <= 0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception ("ยอดเงินในบัญชีไม่พอ")
    print("ถอนเงินจากบัญชี A :",money)
    account["นายA"]-=money

def tranfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ต้องป้อนตัวเลขเท่านั้น")
    if money<=0:
        raise Exception ("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ยอดเงินในบัญชีไม่พอ")
    print("ทำการโอนเงินไปที่บัญชี B :",money)
    account["นายB"]+=money
    account["นายA"]-=money

try:
    getBalance()
    tranfer(500.12)
    getBalance()

except Exception as e:
    print(e)
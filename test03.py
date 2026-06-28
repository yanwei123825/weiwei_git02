# test03.py 整数阶乘计算工具
def factorial(n):
    """计算数字n的阶乘 n! = 1*2*3*...*n"""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_range(start, end):
    """批量计算区间内每个数字的阶乘"""
    res_dict = {}
    for num in range(start, end + 1):
        res_dict[num] = factorial(num)
    return res_dict

if __name__ == "__main__":
    print("===== 阶乘计算工具 test03.py =====")
    print("1. 计算单个数字阶乘")
    print("2. 批量计算区间阶乘")
    while True:
        choose = input("\n请选择功能序号：")
        if choose == "1":
            while True:
                inp = input("输入一个非负整数：")
                try:
                    val = int(inp)
                    if val < 0:
                        print("不能输入负数！")
                        continue
                    fac = factorial(val)
                    print(f"{val}! = {fac}")
                    break
                except ValueError:
                    print("输入非法，请输入整数！")
            break
        elif choose == "2":
            while True:
                try:
                    s = int(input("输入区间起始："))
                    e = int(input("输入区间结束："))
                    if s < 0 or e < 0 or s > e:
                        print("区间数字必须为非负，且起始≤结束！")
                        continue
                    data = factorial_range(s, e)
                    print("\n区间阶乘结果：")
                    for k, v in data.items():
                        print(f"{k}! = {v}")
                    break
                except ValueError:
                    print("输入非法整数！")
            break
        else:
            print("只能输入1或2！")
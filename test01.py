# test01.py 独立脚本：打印指定范围内全部质数
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_all_prime(start, end):
    """打印 start 到 end 之间所有质数"""
    prime_list = []
    for n in range(start, end + 1):
        if is_prime(n):
            prime_list.append(n)
    return prime_list

if __name__ == "__main__":
    print("===== 区间质数打印工具(test01) =====")
    try:
        s = int(input("输入起始数字："))
        e = int(input("输入结束数字："))
        primes = print_all_prime(s, e)
        print(f"\n{s} ~ {e} 之间的质数：{primes}")
    except ValueError:
        print("请输入合法整数！")
# test02.py 斐波那契数列计算器
def fibonacci_list(count):
    """生成前 count 项斐波那契数列"""
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, count):
        next_num = fib[i-1] + fib[i-2]
        fib.append(next_num)
    return fib

def fib_nth(num):
    """获取第 n 位斐波那契数字"""
    fib_arr = fibonacci_list(num)
    return fib_arr[-1]

if __name__ == "__main__":
    print("===== 斐波那契数列工具 test02.py =====")
    while True:
        user_input = input("请输入想要生成的斐波那契项数（正整数）：")
        try:
            num = int(user_input)
            if num > 0:
                break
            else:
                print("错误：请输入大于0的数字！")
        except ValueError:
            print("错误：输入不是有效整数，重新输入！")
    
    fib_arr = fibonacci_list(num)
    print(f"\n前{num}项斐波那契数列：{fib_arr}")
    print(f"第{num}项数值：{fib_nth(num)}")
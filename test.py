# 数值累加脚本：计算 1 ~ n 的总和
def sum_num(n):
    """循环方式计算 1 到 n 连续整数累加和"""
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

def sum_formula(n):
    """数学公式 n*(n+1)/2 快速求和，对比循环结果"""
    return n * (n + 1) // 2

def is_prime(num):
    """判断一个数字是否为质数"""
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

# 主程序入口
if __name__ == "__main__":
    print("===== 1~n 整数累加计算器 =====")
    # 循环接收合法数字输入
    while True:
        input_str = input("请输入一个正整数作为累加上限：")
        try:
            max_num = int(input_str)
            if max_num > 0:
                break
            else:
                print("错误：请输入大于0的正整数！")
        except ValueError:
            print("错误：输入不是有效数字，请重新输入！")
    
    # 两种方式计算累加
    loop_result = sum_num(max_num)
    formula_result = sum_formula(max_num)

    print(f"\n循环计算结果：1 到 {max_num} 的累加和 = {loop_result}")
    print(f"公式快速计算结果：1 到 {max_num} 的累加和 = {formula_result}")

    # 新增质数判断功能
    print("\n===== 质数检测功能 =====")
    while True:
        prime_input = input("输入数字判断是否为质数：")
        try:
            p_num = int(prime_input)
            break
        except ValueError:
            print("请输入合法整数！")
    
    if is_prime(p_num):
        print(f"{p_num} 是质数")
    else:
        print(f"{p_num} 不是质数")
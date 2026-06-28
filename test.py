# 数值累加脚本：计算 1 ~ n 的总和
def sum_num(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

# 主程序入口
if __name__ == "__main__":
    # 设置累加上限，可自行修改数字
    max_num = 100
    result = sum_num(max_num)
    print(f"1 到 {max_num} 的累加结果为：{result}")
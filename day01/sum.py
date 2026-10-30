# 练习 2：读两个数，输出它们的和
# 运行方法：在 VS Code 里按 Ctrl+F5，或终端里执行  python day01\sum.py

# input() 读进来的是「字符串」，要先用 int() 变成整数才能相加
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))

# TODO: 把 a 和 b 加起来，结果存到 total 里（就一行）
total = a+b

print("它们的和是：", total)

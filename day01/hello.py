# 第 1 天：第一段能跑起来的代码
# 运行：.\.venv\Scripts\python.exe day01\hello.py

name = "随缘"
age = 0          # 改成你的年龄
height = 1.75    # 改成你的身高（米）

print("你好，" + name)                 # 字符串拼接
print(f"我今年 {age} 岁，身高 {height} 米")  # f-string，最常用
print("十年后我", age + 10, "岁")        # 逗号会把多段内容连起来，中间自动加空格

# 小计算：BMI = 体重(kg) / 身高(m) 的平方
weight = 65.0
bmi = weight / (height ** 2)
print(f"BMI = {bmi:.1f}")

if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
else:
    print("偏胖")

import random

random.seed(42)

money = 100
num_people = 100
num_rounds = 200000

people = [money] * num_people # 这就是在Python中我们如何构建元素都为100的列表

for round in range(num_rounds):
    for i in range(num_people):
        choice_range_dice = [j for j in range(num_people) if j != i]
        choice = random.choice(choice_range_dice)
        if people[i] == 0:
            continue
        else:
            people[i] -= 1
            people[choice] += 1


import matplotlib.pyplot as plt

# ================= 解决中文和负号显示问题 =================
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'SimHei']  # 优先使用文泉驿微米黑
plt.rcParams['axes.unicode_minus'] = False  # 保证坐标轴上的负号 '-' 正常显示
# ========================================================

# 接下来正常写画图代码...
plt.figure(figsize=(8, 5))
plt.hist(people, bins=20, edgecolor="black", color="skyblue")
plt.axvline(100, color="red", linestyle="--", label="初始/平均财富 (100)")

plt.title("财富分布直方图 (100个人 10万轮)")
plt.xlabel("金钱数量")
plt.ylabel("对应人数")
plt.legend()
plt.savefig("wealth_distribution.png", dpi=300)
print("图表已成功保存为 wealth_distribution.png")
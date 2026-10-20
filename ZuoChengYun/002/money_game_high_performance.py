import random

random.seed(42)

money = 100
num_people = 100
num_rounds = 200000

people = [money] * num_people # 这就是在Python中我们如何构建元素都为100的列表

for round in range(num_rounds):
    for i in range(num_people):
        if people[i] == 0:
            continue
        # 不可以放在上一个判断前面，不然就会浪费一次随机数生成。
        # choice = random.choice(range(num_people-1)) # 内部需要先拿到 range 序列对象再做索引。
        choice = random.randrange(num_people - 1) # 更高效
        if choice >= i:
            choice = choice + 1
        
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
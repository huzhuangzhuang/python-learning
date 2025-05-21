print("Hello GitHub原子化提交！")
#用户输入功能
name = input("请输入你的名字")
age = int(input("请输入年龄"))
print(f"{name},你明年就{age+1}岁啦！")

#列表
fruits = ["苹果","香蕉","橘子"]

#增删改查
fruits.append("西瓜")    # 添加元素
fruits.pop(1)           # 删除第二个元素（香蕉）
fruits[0] = "红富士苹果"  # 修改元素

# 循环遍历
print("我喜欢的水果：")
for fruit in fruits:
    print(f"- {fruit}")

# 让用户输入出生年份，用f-string直接算年龄
birth = int(input("出生年份："))
print(f"你的年龄是{2024-birth}岁")
name = input("你的名字：").strip() # .strip() 去掉首尾空格
age = int(input("你的年龄："))
print(f"{name.upper()},明年{age+1}岁，请珍惜时间！") # 名字转大写

# 条件判断
age = int(input("你的年龄："))

if age < 6:
    print("免费入园！")
elif 6 <= age <18:
    print("儿童票：50元")
elif 60 <= age < 70:
    print("长者票：30元")
else:
    print("成人票：80元")

# 字典进阶
# 导入datetime模块中的datetime
from datetime import datetime
# 创建智能应答知识库
qa_dict = {
    "你好":"你好！我是AI助手",
    "天气":"今天晴，气温25℃",
    "时间":f"现在是{datetime.now().strftime('%H:%M')}",
    "再见":"下次见哦！"
}
# 使用update()合并字典
qa_dict.update({
    "笑话":"为什么程序员总分不清万圣节和圣诞节？因为 Oct 31 == Der 25!😂",
    "菜单":"你发现了开发者藏得猫咪代码！🐱"
})
# 根据用户输入返回答案
user_input = input("你想问什么？（你好/天气/时间/再见）")
# 用in检查键是否存在
if user_input in qa_dict:
    print("我知道答案！",qa_dict.get(user_input))
else:
    print("请重新输入！")
#print(qa_dict.get(user_input,"这个问题我还需要学习~")) # get() 安全获取

# 应答系统
unknown_question = []
# 导入datetime模块中的datetime
from datetime import datetime
qa_dict = {
    "你好":"你好！我是AI助手",
    "天气":"今天晴，气温25℃",
    "时间":f"现在是{datetime.now().strftime('%H:%M')}",
    "再见":"下次见哦！"
}

while True:
    user_input = input("请输入问题：")

    # 先处理特殊指令
    if user_input == "退出":
        break
    if user_input == "帮助":
        print("支持的问题关键词：",list(qa_dict.keys()))
        continue

    # 核心逻辑：判断是否在知识库
    if user_input in qa_dict:
        print(qa_dict[user_input])
    else:
        print("请重新输入（问题不存在）")
        if user_input not in unknown_question: # 避免重复记录
            unknown_question.append(user_input)
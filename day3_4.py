import random
secret_number =random.randint(1,100)
count=0
print("我想到一个1到100之间的数字，你猜猜看！")
while True:
    guess=int(input("请输入你猜的数字："))
    count += 1
    if guess < secret_number:
        print("太小了！")
    elif guess > secret_number:
        print("太大了!")
    else:
        print(f"恭喜你猜对了！你一共猜了{count}次。")
        break
import random
secret_number = random.randint(1,100)
count = 0

min_num = 1
max_num = 100

print("我想到一个1到100之间的数字，你猜猜看!")

while True:
    guess = int(input(f"请输入你猜的数字(当前范围：{min_num}-{max_num}):"))
    count += 1

    if guess < secret_number:
        min_num = guess
        print(f"小了，范围更新为 {min_num}-{max_num}!")
    elif guess > secret_number:
        max_num = guess
        print(f"大了，范围更新为 {min_num}-{max_num}!")
    else:
        print(f"恭喜你，猜对了! 数字就是 {secret_number}")
        print(f"你总共猜了 {count} 次.")
        break
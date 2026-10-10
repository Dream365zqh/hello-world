weather = input("今天下雨了嘛？")
if "否" in weather or "晴" in weather or "不" in weather or "没" in weather:
    print("太好了，今天可以轻装出门了哦！☀")
elif "是" in weather or "下雨" in weather or "雨" in weather or "下了" in weather:
    print("记得带伞，别淋湿了哦！🌂")
else:
    print("抱歉，我是一只笨电脑，听不懂你的意思哦！")
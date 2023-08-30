from bs4 import BeautifulSoup
import requests  # 发起网络请求

response = requests.get("http://www.weather.com.cn/weather/101220301.shtml")
response.encoding = "utf-8"  # 设置编码为utf-8
soup = BeautifulSoup(response.text, "html.parser")

div = soup.find("div", id="7d")  # 获取div标签的内容
ul = div.find("ul")  # 获取ul标签的内容
li = ul.find_all("li")  # 获取所有li标签的内容
weatherForSevenDay = []  # 创建列表weatherForSevenDay

for weather in li:  # 遍历所有li标签的内容
    temp = []  # 创建列表temp，暂存数据
    date = weather.find("h1").string  # 获取h1标签的内容
    temp.append(date)  # 把h1标签的内容加到temp列表中
    p = weather.find_all("p")  # 获取所有p标签的内容
    weatherDetail = p[0].string if p[0].string else "" # 获取第一个p标签的内容

    if weatherDetail is not None:  # 判断第一个p标签的内容是否为空
        temp.append("天气为:%s" % weatherDetail)  # 将结果加入temp列表中
        Hightemprature = p[1].find("span").string if p[1].find("span") else ""
        if Hightemprature is not None:  # 判断第二个p标签中的span标签的内容是否为空
            temp.append("最高温为:%s ℃" % Hightemprature)  # 将结果加入temp列表中
        LowTemprature = p[1].find("i").string if p[1].find("i") else ""


        # 获取第二个p标签中的i标签的内容
        if LowTemprature is not None:  # 判断第二个p标签中的i标签的内容是否为空
            temp.append("最低温为:%s" % LowTemprature)  # 将结果加入temp列表中
        weatherForSevenDay.append(temp)  # 将temp列表中的内容加入weatherForSevenDay列表中

for weather in weatherForSevenDay:  # 遍历列表weatherForSevenDay
    print(weather)  # 打印

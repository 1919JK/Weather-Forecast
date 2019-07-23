from bs4 import BeautifulSoup as bs
import requests as rq
import datetime as dt
today = dt.date.today()
url = "https://www.yomiuri.co.jp/"
html = rq.get(url)
page = bs(html.content, "html.parser")
#pageから天気予報の部分を切り出し
weather_forecast = page.find("table", attrs = {"class", "home-weather-forecast-list"})
td = weather_forecast.find_all("td")
span = weather_forecast.find_all("span")
#↑からリストを取得するための関数。目的のデータは周期的に表れるためmodで選択。
def get_list (ls_in, freq, mod):
    j = 0
    ls_out = []
    for data in ls_in:
        if j % freq == mod:
            ls_out.append(data.contents[0])
        j += 1
    return ls_out

city = get_list(td, 2, 0) #リスト：都市
weather = get_list(span, 3, 0) #リスト：天気
temp_high = get_list(span, 3, 1) #リスト：最高気温
temp_low = get_list(span, 3, 2) #リスト：最低気温

tomorrow = today + dt.timedelta(days = 1)

print("<<" + tomorrow.strftime('%m') + "月" + tomorrow.strftime('%d') + "日の天気>>")
for i in range(len(city)):
    print(f"{city[i].rjust(3, '　')}:{weather[i].center(5, '　')}　最高気温:　{temp_high[i]}　/　最低気温:　{temp_low[i]}")

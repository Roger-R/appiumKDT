import requests
import datetime


#require API res
res = requests.get("https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml",verify=False)
res.encoding = res.apparent_encoding
resJSON = res.json()
forecases = resJSON.get("forecast_detail")


today = datetime.date.today()
todayStr = today.strftime("%Y%m%d")
targetDate = today + datetime.timedelta(days=2)
targetDateStr = targetDate.strftime("%Y%m%d")


for dayForcast in forecases:
    if dayForcast.get("forecast_date") == targetDateStr:
        print(str(dayForcast.get("min_rh"))+"-"+str(dayForcast.get("max_rh"))+"%")

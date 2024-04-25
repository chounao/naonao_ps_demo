import jsonpath
from jsonpath_ng import jsonpath, parse

json_data = {
    "error": 0,
    "status": "success",
    "date": "2014-05-10",
    "extra": {
        "rain": 3,
        "sunny": 2
    },
    "recorder": {
        "name": "qin",
        "time": "2014-05-10 22:00",
        "mood": "good",
        "address": {
            "provice": "ZJ",
            "city": "nanjing"
        }
    },
    "results": [
        {
            "currentCity": "南京",
            "weather_data": [
                {
                    "date": "周六今天,实时19",
                    "dayPictureUrl": "http://api.map.baidu.com/images/weather/day/dayu.png",
                    "nightPictureUrl": "http://api.map.baidu.com/images/weather/night/dayu.png",
                    "weather": "大雨",
                    "wind": "东南风5-6级",
                    "temperature": "18"
                },
                {
                    "date": "周日",
                    "dayPictureUrl": "http://api.map.baidu.com/images/weather/day/zhenyu.png",
                    "nightPictureUrl": "http://api.map.baidu.com/images/weather/night/duoyun.png",
                    "weather": "阵雨转多云",
                    "wind": "西北风4-5级",
                    "temperature": "21~14"
                }
            ]
        }
    ]
}

a = jsonpath.jsonpath(json_data,"$.results[*].weather_data[?(@.date == '周日')]")
a1 = parse()
b = jsonpath.jsonpath(json_data,"$.results[*].weather_data[?(@.weather in ['大雨'])]")
c = jsonpath.jsonpath(json_data,"$.results[*].weather_data[?(@.temperature =~ /\\d+/i)]")
d = jsonpath.jsonpath(json_data,"$.results[*].weather_data[?(@.temperature =~ /\\d+~\\d+/i)]")
e = jsonpath.jsonpath(json_data,"$.results[*].weather_data[?(@.temperature =~ /\\d+/i)].dayPictureUrl")
print(a)
print(b)
print(c)
print(d)
print(e)



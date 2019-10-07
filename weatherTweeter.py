import tweepy
import pyowm
from time import localtime, strftime

consumer_key = "xxxxxxxxx";
consumer_secret = "xxxxxxxxxx"
access_token = "xxxxxxxxxx"
access_token_secret = "xxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["North","North North East","North East","East North East","East","East South East", "South East", "South South East","South","South South West","South West","West South West","West","West North West","North West","North North West"]
    return arr[(val % 16)]


time = strftime("%H:%M:%S", localtime())
owm = pyowm.OWM('xxxx-xxxx-xxxx')
uvi = owm.uvindex_around_coords(53.4239, 7.9407)
obs = owm.weather_at_id(2966839)
uvText = uvi.get_exposure_risk()
weather = obs.get_weather()

degreeSign = u'\N{DEGREE SIGN}'

status = weather.get_detailed_status()
temp = weather.get_temperature(unit='celsius')['temp']
wind = weather.get_wind(unit='miles_hour')['speed']
wind = round(wind, 2)
windDir = str(degToCompass(wind))

temp = str(temp)
wind = str(wind)

tweet = 'The weather in Athlone, at '+time+', is currently '+status+' at '+temp+degreeSign+'C with winds of up to '+wind+'mph '+windDir+'. The UV exposure risk is currently '+uvText+'! #Athlone #Weather'

api.update_status(tweet)

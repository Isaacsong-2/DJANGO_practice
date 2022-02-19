import requests
import datetime


def get_exchange():
    today = datetime.datetime.now()
    if today.weekday() >= 5:
        diff = today.weekday() - 4
        today = today - datetime.timedelta(days=diff)
    today = today.strftime('%Y%m%d')
    auth = 'Rw8v5TJFdXTbwScce46fi5Z2S8LKr2fF'
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data=AP01'
    url = url.format(auth, today)
    res = requests.get(url)
    data = res.json()

    for d in data:
        print(d)
        if d['cur_unit'] == 'USD':
            return d['tts']
    return

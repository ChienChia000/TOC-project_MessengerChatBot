import os
import requests
from bs4 import BeautifulSoup


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        'message': {
            'attachment': {
                'type': 'image',
                'payload': {
                    'url':img_url
                }
            }
        }
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def THSRparse(payload):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResult",data=payload,headers=headers)
    soup=BeautifulSoup(res.text,features="html.parser")
    
    trainCode=[]
    arriveTime=[]
    result=''
    flag=0

    divs = soup.find_all('a', 'ui-block-a')
    for d in divs:
        #print(d.find('div').string.lstrip())
        trainCode.append(d.find('div').string.lstrip())
        flag+=1

    flag=0
    divs = soup.find_all('a', 'ui-block-b')
    for d in divs:
        #print(d.find('div').string.lstrip())
        arriveTime.append(d.find('div').string.lstrip())
        flag+=1
    
    flag=0
    for i in trainCode:
        result+="車次  "
        result+=trainCode[flag]
        result+="\n"
        result+="出發 - 到達（行駛時間）\n"
        result+=arriveTime[flag]
        result+="\n\n"
        flag+=1

    print(result)

    return result

def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    data = {
        "recipient": {
            "id": id
        },
        "message": {
            "attachment": {
            "type":"image",
            "payload": {
                "url": img_url,
                "is_reusable": True
                }
            }
        }
    }
    res = requests.post(url, json=data)
    if res.status_code != 200:
        print("Unable to send image message: " + res.text)
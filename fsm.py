from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import THSRparse

print("\n\n\n\n\n\n\n\n\nfsm.py start\n")

theDay=''
startStation=''
endStation=''
timeSelect=''
payload = {
    'startStation':startStation,
    'endStation':endStation,
    'theDay':theDay,
    'timeSelect':timeSelect,
    'waySelect':'DepartureInMandarin'
}

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    print("\n\nout\n",payload,"\n\n")

    def is_going_to_menu(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '嗨'
        return False

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '時刻表查詢'
        return False

    def is_going_to_date(self, event):
        #print(event['message']['text'])
        #if event.get("message"):
        if event.get("message"):
            text = event['message']['text']
            if text == '輸入格式為\nYYYY/MM/DD':
                return False
            elif "/" in text:
                return True
        return False
        #if :
        #    
        #    return text.lower() == 'go to state1'

    def is_going_to_start(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == '那要從哪一站出發呢？':
                return False
            elif "出發" in text:
                return True
        return False

    def is_going_to_end(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == '那要搭到哪一站呢？':
                return False
            elif "搭到" in text:
                return True
        return False

    def is_going_to_time(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text == '輸入格式為\nhh:mm\n記得要使用半形的冒號唷～':
                return False
            elif ":" in text:
                return True
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '車站資訊'
        return False

    def is_going_to_nangang(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '南港'
        return False

    def is_going_to_taipei(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台北'
        return False

    def is_going_to_banqiao(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '板橋'
        return False

    def is_going_to_taoyuan(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '桃園'
        return False

    def is_going_to_hsinchu(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '新竹'
        return False

    def is_going_to_miaoli(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '苗栗'
        return False

    def is_going_to_taichung(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台中'
        return False

    def is_going_to_chunghua(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '彰化'
        return False

    def is_going_to_yunlin(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '雲林'
        return False

    def is_going_to_chiayi(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '嘉義'
        return False

    def is_going_to_tainan(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台南'
        return False

    def is_going_to_zuoying(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '左營'
        return False

    def is_going_to_web(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '官方網站'
        return False

    def on_enter_menu(self, event):
        print("I'm entering menu")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "哈囉～")
        responese = send_text_message(sender_id, "我是高鐵服務機器人！")
        responese = send_text_message(sender_id, "我有以下功能\n●時刻表查詢\n●車站資訊\n●官方網站\n")
        responese = send_text_message(sender_id, "需要幫你什麼忙呢？？")
        self.go_back()

    def on_exit_menu(self):
        print('Leaving menu')

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請問哪一天要搭車呢？")
        responese = send_text_message(sender_id, "輸入格式為\nYYYY/MM/DD")
        #self.go_back()

    def on_exit_state1(self, event):
        print('Leaving state1')

    def on_enter_date(self, event):
        print("I'm entering date")

        sender_id = event['sender']['id']
        theDate=event['message']['text']
        payload['theDay']=theDate
        print("\n\n",payload,"\n\n")
        responese = send_text_message(sender_id, "好的，搭車日期是： "+theDate)
        responese = send_text_message(sender_id, "那要從哪一站出發呢？")
        #self.go_back()

    def on_exit_date(self, event):
        print('Leaving date')

    def on_enter_start(self, event):
        print("I'm entering start")

        sender_id = event['sender']['id']
        start=event['message']['text']
        station=''
        if "南港" in start:
            start='南港'
            station='2f940836-cedc-41ef-8e28-c2336ac8fe68'
        elif '台北' in start:
            start='台北'
            station='977abb69-413a-4ccf-a109-0272c24fd490'
        elif '板橋' in start:
            start='板橋'
            station='e6e26e66-7dc1-458f-b2f3-71ce65fdc95f'
        elif '桃園' in start:
            start='桃園'
            station='fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
        elif '新竹' in start:
            start='新竹'
            station='a7a04c89-900b-4798-95a3-c01c455622f4'
        elif '苗栗' in start:
            start='苗栗'
            station='e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'
        elif '台中' in start:
            start='台中'
            station='3301e395-46b8-47aa-aa37-139e15708779'
        elif '彰化' in start:
            start='彰化'
            station='38b8c40b-aef0-4d66-b257-da96ec51620e'
        elif '雲林' in start:
            start='雲林'
            station='5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f'
        elif '嘉義' in start:
            start='嘉義'
            station='60831846-f0e4-47f6-9b5b-46323ebdcef7'
        elif '台南' in start:
            start='台南'
            station='9c5ac6ca-ec89-48f8-aab0-41b738cb1814'
        elif '左營' in start:
            start='左營'
            station='f2519629-5973-4d08-913b-479cce78a356'
        payload['startStation']=station
        print("\n\nstart\n",payload,"\n\n")
        responese = send_text_message(sender_id, "好的，從"+start+"出發")
        responese = send_text_message(sender_id, "那要搭到哪一站呢？")
        #self.go_back()

    def on_exit_start(self, event):
        print('Leaving start')

    def on_enter_end(self, event):
        print("I'm entering end")

        sender_id = event['sender']['id']
        end=event['message']['text']
        station=''
        if "南港" in end:
            end='南港'
            station='2f940836-cedc-41ef-8e28-c2336ac8fe68'
        elif '台北' in end:
            end='台北'
            station='977abb69-413a-4ccf-a109-0272c24fd490'
        elif '板橋' in end:
            end='板橋'
            station='e6e26e66-7dc1-458f-b2f3-71ce65fdc95f'
        elif '桃園' in end:
            end='桃園'
            station='fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'
        elif '新竹' in end:
            end='新竹'
            station='a7a04c89-900b-4798-95a3-c01c455622f4'
        elif '苗栗' in end:
            end='苗栗'
            station='e8fc2123-2aaf-46ff-ad79-51d4002a1ef3'
        elif '台中' in end:
            end='台中'
            station='3301e395-46b8-47aa-aa37-139e15708779'
        elif '彰化' in end:
            end='彰化'
            station='38b8c40b-aef0-4d66-b257-da96ec51620e'
        elif '雲林' in end:
            end='雲林'
            station='5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f'
        elif '嘉義' in end:
            end='嘉義'
            station='60831846-f0e4-47f6-9b5b-46323ebdcef7'
        elif '台南' in end:
            end='台南'
            station='9c5ac6ca-ec89-48f8-aab0-41b738cb1814'
        elif '左營' in end:
            end='左營'
            station='f2519629-5973-4d08-913b-479cce78a356'
        payload['endStation']=station
        print("\n\nend\n",payload,"\n\n")
        responese = send_text_message(sender_id, "好的，搭到"+end)
        responese = send_text_message(sender_id, "那要幾點出發呢？")
        responese = send_text_message(sender_id, "輸入格式為\nhh:mm\n記得要使用半形的冒號唷～")
        #self.go_back()

    def on_exit_end(self, event):
        print('Leaving end')

    def on_enter_time(self, event):
        print("I'm entering time")

        sender_id = event['sender']['id']
        time=event['message']['text']
        
        payload['timeSelect']=time
        print("\n\ntime\n",payload,"\n\n")
        responese = send_text_message(sender_id, "好的，"+time+"出發")
        responese = send_text_message(sender_id, "搜尋中，請稍等...")
        result=THSRparse(payload)
        responese = send_text_message(sender_id, result)
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_time(self):
        print('Leaving time')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "想要查詢哪個車站呢？")
        #self.go_back()

    def on_exit_state2(self, event):
        print('Leaving state2')

    #Nan-gang
    def on_enter_nangang(self, event):
        print("I'm entering nangang")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵南港站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/2f940836-cedc-41ef-8e28-c2336ac8fe68")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_nangang(self):
        print('Leaving nangang')

    #Taipei
    def on_enter_taipei(self, event):
        print("I'm entering taipei")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵台北站\n"+"http://www.thsrc.com.tw/tw/StationInfo/prospect/977abb69-413a-4ccf-a109-0272c24fd490")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_taipei(self):
        print('Leaving taipei')

    #Banqiao
    def on_enter_banqiao(self, event):
        print("I'm entering banqiao")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵板橋站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/e6e26e66-7dc1-458f-b2f3-71ce65fdc95f")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_banqiao(self):
        print('Leaving banqiao')

    #Taoyuan
    def on_enter_taoyuan(self, event):
        print("I'm entering taoyuan")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵桃園站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/fbd828d8-b1da-4b06-a3bd-680cdca4d2cd")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_taoyuan(self):
        print('Leaving taoyuan')

    #Hsinchu
    def on_enter_hsinchu(self, event):
        print("I'm entering hsinchu")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵新竹站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/a7a04c89-900b-4798-95a3-c01c455622f4")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_hsinchu(self):
        print('Leaving hsinchu')

    #Miaoli
    def on_enter_miaoli(self, event):
        print("I'm entering miaoli")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵苗栗站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/e8fc2123-2aaf-46ff-ad79-51d4002a1ef3")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_miaoli(self):
        print('Leaving miaoli')

    #Taichung
    def on_enter_taichung(self, event):
        print("I'm entering taichung")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵台中站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/3301e395-46b8-47aa-aa37-139e15708779")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_taichung(self):
        print('Leaving taichung')

    #Chunghua
    def on_enter_chunghua(self, event):
        print("I'm entering chunghua")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵彰化站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/38b8c40b-aef0-4d66-b257-da96ec51620e")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_chunghua(self):
        print('Leaving chunghua')

    #Yunlin
    def on_enter_yunlin(self, event):
        print("I'm entering yunlin")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵雲林站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_yunlin(self):
        print('Leaving yunlin')

    #Chiayi
    def on_enter_chiayi(self, event):
        print("I'm entering chiayi")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵嘉義站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/60831846-f0e4-47f6-9b5b-46323ebdcef7")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_chiayi(self):
        print('Leaving chiayi')

    #Tainan
    def on_enter_tainan(self, event):
        print("I'm entering tainan")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵台南站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/9c5ac6ca-ec89-48f8-aab0-41b738cb1814")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_tainan(self):
        print('Leaving tainan')

    #Zuoying
    def on_enter_zuoying(self, event):
        print("I'm entering zuoying")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "高鐵左營站\n"+"http://www.thsrc.com.tw/tw/StationInfo/Prospect/f2519629-5973-4d08-913b-479cce78a356")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_zuoying(self):
        print('Leaving zuoying')

    #Official Website
    def on_enter_web(self, event):
        print("I'm entering web")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "官網再這裡唷～\nhttp://www.thsrc.com.tw/index.html")
        responese = send_text_message(sender_id, "有需要其他幫忙再跟我說～")
        self.go_back()

    def on_exit_web(self):
        print('Leaving web')


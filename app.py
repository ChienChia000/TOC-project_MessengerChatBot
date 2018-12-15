import os
from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']

machine = TocMachine(
    states=[
        'user',
        'menu',
        'state1',
        'date',
        'start',
        'end',
        'time',
        'state2',
        'nangang',
        'taipei',
        'banqiao',
        'taoyuan',
        'hsinchu',
        'miaoli',
        'taichung',
        'chunghua',
        'yunlin',
        'zuoying',
        'chiayi',
        'tainan',
        'web'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'menu',
            'conditions': 'is_going_to_menu'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'date',
            'conditions': 'is_going_to_date'
        },
        {
            'trigger': 'advance',
            'source': 'date',
            'dest': 'start',
            'conditions': 'is_going_to_start'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'end',
            'conditions': 'is_going_to_end'
        },
        {
            'trigger': 'advance',
            'source': 'end',
            'dest': 'time',
            'conditions': 'is_going_to_time'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'nangang',
            'conditions': 'is_going_to_nangang'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'taipei',
            'conditions': 'is_going_to_taipei'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'banqiao',
            'conditions': 'is_going_to_banqiao'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'taoyuan',
            'conditions': 'is_going_to_taoyuan'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'hsinchu',
            'conditions': 'is_going_to_hsinchu'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'miaoli',
            'conditions': 'is_going_to_miaoli'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'taichung',
            'conditions': 'is_going_to_taichung'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'chunghua',
            'conditions': 'is_going_to_chunghua'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'yunlin',
            'conditions': 'is_going_to_yunlin'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'chiayi',
            'conditions': 'is_going_to_chiayi'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'tainan',
            'conditions': 'is_going_to_tainan'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'zuoying',
            'conditions': 'is_going_to_zuoying'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'web',
            'conditions': 'is_going_to_web'
        },
        {
            'trigger': 'go_back',
            'source': [
                'menu',
                'time',
                'taipei',
                'nangang',
                'banqiao',
                'taoyuan',
                'hsinchu',
                'chunghua',
                'miaoli',
                'taichung',
                'yunlin',
                'chiayi',
                'tainan',
                'zuoying',
                'web'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)

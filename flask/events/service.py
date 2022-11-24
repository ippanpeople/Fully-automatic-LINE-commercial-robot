from urllib.parse import parse_qsl
import datetime
import sys 
sys.path.append("..") 
from api import *

services = {
    1: {
        'category' : 'personal',
        'img_url' : 'https://rimage.gnst.jp/rest/img/s88p3mar0000/s_0n5n.png',
        'title' : '台湾個人鍋予約',
        'description' : '当店の人気商品の一つ、寒い日の定番',
        'price' : 880,
        'post_url' : 'https://fdev.rinlink.jp',
    },
    2: {
        'category' : 'group',
        'img_url' : 'https://p.potaufeu.asahi.com/5d36-p/picture/14576086/7971c03dc28404cb51013c274d555680_640px.jpg',
        'title' : '和風団体鍋予約',
        'description' : '団体限定, 和風を味わい鍋料理',
        'price' : 880,
        'post_url' : 'https://fdev.rinlink.jp',
    },
}

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='予約したいカテゴリ',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://lh3.googleusercontent.com/p/AF1QipOhUotx8kwNK6Ojj1QYlce9LJ7Nk8B_CuLEhpI=w768-h768-n-o-v1',
                    action=PostbackAction(
                        label='台湾個人鍋',
                        display_text='台湾個人鍋について',
                        data='action=service&category=personal'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://lh3.googleusercontent.com/p/AF1QipOhUotx8kwNK6Ojj1QYlce9LJ7Nk8B_CuLEhpI=w768-h768-n-o-v1',
                    action=PostbackAction(
                        label='和風団体鍋',
                        display_text='和風団体鍋について',
                        data='action=service&category=group'
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message]
    )

def service_event(event):
    data = dict(parse_qsl(event.postback.data))

    bubbles = []

    for service_id in services:
        if services[service_id]['category'] == data['category']:
            service = services[service_id]
            bubble = {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:23",
                    "aspectMode": "cover",
                    "url": service['img_url'],
                    "align": "start"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": service['title'],
                            "wrap": True,
                            "weight": "bold",
                            "size": "xxl",
                            "flex": 0
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": service['description'],
                        "wrap": True,
                        "size": "xs",
                        "margin": "none"
                    },
                    {
                        "type": "text",
                        "text": f"￥{service['price']}",
                        "size": "lg",
                        "margin": "xxl"
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                            "type": "postback",
                            "data": f"action=select_date&service_id={service_id}",
                            "label": "個人鍋予約",
                            "displayText": f"{service['title']}を予約したい"
                            },
                            "color": "#E22222"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": f"{service['title']}について",
                            "uri": service['post_url']
                            }
                        }
                    ]
                }
            }
            bubbles.append(bubble)
            

    flex_message = FlexSendMessage(
        alt_text='カテゴリを選択してください',
        contents={
            "type": "carousel",
            "contents": bubbles
        }
    )
    line_bot_api.reply_message(
        event.reply_token,
        [flex_message]
    )

def service_select_date_event(event):
    
    data = dict(parse_qsl(event.postback.data))

    weekday_string = {
        0: '月',
        1: '火',
        2: '水',
        3: '木',
        4: '金',
        5: '土',
        6: '日',
    }

    business_day = [1, 2, 3, 4, 5, 6]

    quick_reply_buttons = []

    today = datetime.datetime.today().date()

    for x in range(1, 11):
        day = today + datetime.timedelta(days=x)

        if day.weekday() in business_day:
            quick_reply_button = QuickReplyButton(
                action=PostbackAction(label=f'{day} ({weekday_string[day.weekday()]})',
                                      text=f'{day} ({weekday_string[day.weekday()]}) に予約したい',
                                      data=f'action=select_time&service_id={data["service_id"]}&date={day}'))
            quick_reply_buttons.append(quick_reply_button)

    text_message = TextSendMessage(text='予約ご希望の日',
                                   quick_reply=QuickReply(items=quick_reply_buttons))

    line_bot_api.reply_message(
        event.reply_token,
        [text_message])


def service_select_time_event(event):

    data = dict(parse_qsl(event.postback.data))

    available_time = ['11:00', '14:00', '17:00', '20:00']

    quick_reply_buttons = []

    for time in available_time:
        quick_reply_button = QuickReplyButton(action=PostbackAction(label=time,
                                                                    text=f'{time}',
                                                                    data=f'action=confirm&service_id={data["service_id"]}&date={data["date"]}&time={time}'))
        quick_reply_buttons.append(quick_reply_button)

    text_message = TextSendMessage(text='ご希望の時間帯',
                                   quick_reply=QuickReply(items=quick_reply_buttons))
    line_bot_api.reply_message(
        event.reply_token,
        [text_message])
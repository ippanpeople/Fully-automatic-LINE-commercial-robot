from urllib.parse import parse_qsl
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
                            "displayText": f"{service['title']}完了"
                            },
                            "color": "#E22222"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "個人鍋について",
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
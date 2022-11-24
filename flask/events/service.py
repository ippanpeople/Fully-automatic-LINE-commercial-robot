import sys 
sys.path.append("..") 
from api import *

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='予約したいカテゴリ',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://lh3.googleusercontent.com/p/AF1QipOhUotx8kwNK6Ojj1QYlce9LJ7Nk8B_CuLEhpI=w768-h768-n-o-v1',
                    action=PostbackAction(
                        label='台湾個人なべ',
                        display_text='個人鍋について',
                        data='action=service&itemid=台湾個人なべ'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fbook.asahi.com%2Farticle%2F12024484&psig=AOvVaw1Veh1eRjc-vKnL3McZofTS&ust=1669362877966000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNDOybyrxvsCFQAAAAAdAAAAABAP',
                    action=PostbackAction(
                        label='団体サービス',
                        display_text='団体サービスについて',
                        data='action=service&itemid=団体サービス'
                    )
                )
            ]
        )
    )

    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message]
    )

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage,  LocationSendMessage, ImagemapSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('LZMLw49U/JiAxFJKgPUtIScTt0KlTMKfJwmTNL7Ec6OBAZeWcVYCHBm0m9nDlrKm7iDGmLl6gZikuXYG5U+OcfBKiHqIFK8LGk89Lqv46dbko6H7JnO/CrV7pFuP035wulgV6MYrHPzbQPfj5te36QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('870b67c740b8012d0cc36ee0a116f925')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # 將從使用者側接收到的訊息, 進行自定義並加入表情符號（
    # lower() : 將字串主動變為小寫
    message_text = str(event.message.text).lower()
    
    if message_text == "@site":
        emoji = [
            {
                "index": 2,
                "productId": "5ac21c4e031a6752fb806d5b",
                "emojiId": "091"
            },
            {
                "index": 3,
                "productId": "5ac21c4e031a6752fb806d5b",
                "emojiId": "082"
            },
            {
                "index": 4,
                "productId": "5ac21c4e031a6752fb806d5b",
                "emojiId": "150"
            },
            {
                "index": 37,
                "productId": "5ac21184040ab15980c9b43a",
                "emojiId": "225"
            }
        ]
        text_message = TextSendMessage(text='''公式$$$はこちらです〜
- https://rakunabe.jp
- $お待ちしております〜''', emojis=emoji)
        sticker_message = StickerSendMessage(
            package_id='8522',
            sticker_id='16581271'
        )
        about_us_img = 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/296813604_577297440556390_2640681472271811157_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=110&_nc_ohc=HJ5J6srFtecAX_Cm3ZV&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=Mjg5NTc1ODI5MzY3OTkxNjM1OQ%3D%3D.2-ccb7-5&oh=00_AfCVXc9Qg4LF-KhIvjNTosYR1py7qhcFnj5hBFOt1iPgvw&oe=637AE86C&_nc_sid=30a2ef'

        image_message = ImageSendMessage(
            original_content_url=about_us_img,
            preview_image_url=about_us_img
        )
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, sticker_message, image_message])
    elif message_text == '@map':

        location_message = LocationSendMessage(
            title='台湾楽鍋',
            address='2F, ３丁目-２-1 高津 中央区 大阪市 大阪府 542-0072',
            latitude=34.6665307,
            longitude=135.5082797
        )

        line_bot_api.reply_message(
            event.reply_token,
            location_message)

    # imagemap_message = ImagemapSendMessage(
    #     base_url='https://i.imgur.com/fQDqArm.jpg',
    #     alt_text='this is an imagemap',
    #     base_size=BaseSize(height=1040, width=1040),
    #     video=Video(
    #         original_content_url='https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_480_1_5MG.mp4',
    #         preview_image_url='https://via.placeholder.com/1040x585',
    #         area=ImagemapArea(
    #             x=0, y=0, width=1040, height=585
    #         ),
    #         external_link=ExternalLink(
    #             link_uri='https://example.com/see_more.html',
    #             label='See More',
    #         ),
    #     ),
    #     actions=[
    #         URIImagemapAction(
    #             link_uri='https://google.com/',
    #             area=ImagemapArea(
    #                 x=0, y=0, width=520, height=1040
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='hello',
    #             area=ImagemapArea(
    #                 x=520, y=0, width=520, height=1040
    #             )
    #         )
    #     ]
    # )

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     imagemap_message)

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """ニーハウー, ようこそ台湾楽鍋！
僕はヘルパーのナベ君です！
- 予約する場合には
- 直接下のメニューから操作すればできますよう

- お待ちしております〜"""
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg)
    )
    

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)

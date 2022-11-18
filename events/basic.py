from line_bot_api import *

def about_us_event(event):

    # 將從使用者側接收到的訊息, 進行自定義並加入表情符號（
    # lower() : 將字串主動變為小寫
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

def location_event(event):
    location_message = LocationSendMessage(
        title='台湾楽鍋',
        address='2F, ３丁目-２-1 高津 中央区 大阪市 大阪府 542-0072',
        latitude=34.6665307,
        longitude=135.5082797
    )

    line_bot_api.reply_message(
        event.reply_token,
        location_message)


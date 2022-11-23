from flask.api import *

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
    about_us_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsgBsMhixWW72YbydGkuyjoUIGFeXhfwCZOYoDqsotJcTXT893S9SKJvgjCsib0P90bPs&usqp=CAU'

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


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage
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
        line_bot_api.reply_message(
            event.reply_token,
            text_message)
        sticker_message = StickerSendMessage(
            package_id='8522',
            sticker_id='16581271'
        )

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

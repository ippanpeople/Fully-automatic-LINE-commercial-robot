from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

@handler.add(FollowEvent)
def handle_follow(event):
    print(event)

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)

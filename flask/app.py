from flask import Flask, request, abort
from urllib.parse import parse_qsl

from api import *

from events.basic import *
from events.service import *

from extensions import db, migrate
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@10.0.1.201:5432/raku'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
migrate.init_app(app, db)

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
    
    # Determine if the user exists in the database
    user = User.query.filter(User.line_id == event.source.user_id).first()

    if not user :
        profile = line_bot_api.get_profile(event.source.user_id)
        # print(profile)
        # print(profile.display_name)
        # print(profile.user_id)
        # print(profile.picture_url)
        user = User(profile.user_id, profile.display_name, profile.picture_url)
        db.session.add(user)
        db.session.commit()
        
    # print(user.id)
    # print(user.line_id)
    # print(user.display_name)
    
    if message_text == "@site":
        about_us_event(event)
    elif message_text == '@map':
        location_event(event)
    elif message_text == '@reserve':
        service_category_event(event)

@handler.add(PostbackEvent)
def handle_postback(event):

    data = dict(parse_qsl(event.postback.data))
    print('action:', data.get('action'))
    print('category:', data.get('category'))
    print('service_id:', data.get('service_id'))


    if data.get('action') == 'service':
        print('action:', data.get('action'))
        print('category:', data.get('category'))
        print('service_id:', data.get('service_id'))
        service_event(event)
    elif data.get('action') == 'select_date':
        service_select_date_event(event)
        print('action:', data.get('action'))
        print('category:', data.get('category'))
        print('service_id:', data.get('service_id'))
        print('date:', data.get('date'))
    elif data.get('action') == 'select_time':
        service_select_time_event(event)
        print('action:', data.get('action'))
        print('category:', data.get('category'))
        print('service_id:', data.get('service_id'))
        print('date:', data.get('date'))
        print('time:', data.get('time'))



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

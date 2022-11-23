from flask import Flask, request, abort

from api import *
from events.basic import *

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
    
    profile = line_bot_api.get_profile(event.source.user_id)
    # user = User(profile.user_id, profile.display_name, profile.picture_url)
    # db.session(user)
    # db.session.commit()

    if message_text == "@site":
        about_us_event(event)
        # print(profile)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)
        user = User(profile.user_id, profile.display_name, profile.picture_url)
        print(user)
        db.session.add(user)
        db.session.commit()


    elif message_text == '@map':
        location_event(event)
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

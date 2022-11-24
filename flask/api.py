from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage,  LocationSendMessage, ImagemapSendMessage,
    TemplateSendMessage, ImageCarouselTemplate, PostbackAction, ImageCarouselColumn, FlexSendMessage,
    PostbackEvent
)
line_bot_api = LineBotApi('LZMLw49U/JiAxFJKgPUtIScTt0KlTMKfJwmTNL7Ec6OBAZeWcVYCHBm0m9nDlrKm7iDGmLl6gZikuXYG5U+OcfBKiHqIFK8LGk89Lqv46dbko6H7JnO/CrV7pFuP035wulgV6MYrHPzbQPfj5te36QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('870b67c740b8012d0cc36ee0a116f925')



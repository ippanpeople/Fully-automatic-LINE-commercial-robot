from extensions import db
import datetime

class User(db.Model):
    __table__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    line_id = db.Column(db.String(50), unique=True)
    display_name = db.Column(db.String(255))
    picture_url = db.Column(db.String(255))

    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    # init function : use for defind object initialization setting
    # when create User object ( given that new object ) -> line_id, display_name, picture_url
    def __init__(self, line_id, display_name, picture_url): # self => User(object)
        self.line_id = line_id  # self.line_id => User.line_id
        self.display_name = display_name  # self.display_name => User.display_name
        self.picture_url = picture_url  # self.picture_url => User.picture_url
from main import db

class QAentity(db.Model):
    __tanlename__='questionanswer'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String,nullable=False)
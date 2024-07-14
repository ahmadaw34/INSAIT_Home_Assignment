import os
from flask import Flask,request,jsonify
import openai
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# openai api key from .env 
openai.api_key = os.getenv('OPENAI_API_KEY')

# flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate = Migrate(app, db)

# database entity
class QAentity(db.Model):
    __tablename__='question_answer'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String,nullable=False)

# ask endpoint
@app.route('/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        data=request.get_json()
        question=data.get('question')
        
        response=openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "assistant", "content": question}])
        answer = response.choices[0].message.content

        q_a=QAentity(question=question,answer=answer)
        db.session.add(q_a)
        db.session.commit()

        return jsonify({'question': question, 'answer': answer})

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run()
from flask import Flask,request,redirect,jsonify
import openai
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

openai.api_key='sk-proj-nrtKQE5d4qraTP3dWxY0T3BlbkFJWuzNFZamZupWyZ7WVJUt'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@localhost:5432/question_answer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate = Migrate(app, db)

class QAentity(db.Model):
    __tablename__='question_answer'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String,nullable=False)

@app.route('/ask', methods=['GET','POST'])
def ask():
    if request.method == 'POST':
        # q_a=QAentity(question='postquestion',answer='postanswer')
        # db.session.add(q_a)
        # db.session.commit()
        # return jsonify({'question': 'post', 'answer': 'post'})
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
    # q_a=QAentity(question='getquestion',answer='getanswer')
    # db.session.add(q_a)
    # db.session.commit()
    
    # return jsonify({'question': "getquestion", 'answer': "getanswer"})

@app.route('/')
def home():
    return redirect("/ask")

# if __name__=='__main__':
#     with app.app_context():
#         db.create_all()
#     app.run()
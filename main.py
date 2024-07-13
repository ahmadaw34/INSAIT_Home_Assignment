from flask import Flask,request,redirect,jsonify
import openai
from flask_sqlalchemy import SQLAlchemy
from QAEntity import QAEntity


# openai.api_key='sk-proj-nrtKQE5d4qraTP3dWxY0T3BlbkFJWuzNFZamZupWyZ7WVJUt'
app = Flask(__name__)
db=SQLAlchemy()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:ahmadaw@localhost/Question_Answer'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/ask', methods=['GET','POST'])
def ask():
    if request.method == 'POST':
        data=request.get_json()
        question=data.get('question')
        
        response=openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "assistant", "content": "capital of israel"}])
        answer = response.choices[0].message.content

        q_a=QAEntity(question=question,answer=answer)
        db.session.add(q_a)
        db.session.commit()

        return jsonify({'question': question, 'answer': answer})
    
    return jsonify({'question': "question", 'answer': "answer"})

@app.route('/')
def home():
    return redirect("/ask")

if __name__=='__main__':
    app.run()
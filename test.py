import pytest
from app import app,QAentity,db
from flask_migrate import upgrade

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@db:5432/question_answer'

    with app.app_context():
        upgrade()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()

# post a question and check if the answer saved in the database
def test_ask(client):
    question='what is the capital of China?'
    response = client.post('/ask', json={'question': question})
    assert response.status_code == 200
    expected_answer = response.get_json()
    stored_qa = QAentity.query.filter_by(question=question).first()
    assert stored_qa!=None
    assert stored_qa.answer== expected_answer['answer']


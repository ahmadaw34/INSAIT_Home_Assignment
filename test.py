import pytest
from app import app,QAentity

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_ask(client):
    question='What is the capital of Egypt?'
    response = client.post('/ask', json={'question': question})
    assert response.status_code == 200
    expected_answer = response.get_json()
    stored_qa = QAentity.query.filter_by(question=question).first()
    assert stored_qa!=None
    assert stored_qa.answer== expected_answer


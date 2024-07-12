import requests

def ask_question(question):
    url = 'http://localhost:5000/ask' 

    data = {'question': question}

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print(f"Question: {question}")
            print(f"Answer: {response.json()['answer']}")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Example usage
if __name__ == '__main__':
    question = "What is the capital of France?"
    ask_question(question)

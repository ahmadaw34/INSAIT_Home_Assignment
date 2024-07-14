a simple Flask server that exposes an endpoint to ask a question. The server sends the
question to an OpenAI API, receives the answer, and saves both the question and the answer in
a PostgreSQL database. 
The server and the database are dockerized and run with
Docker Compose. 
test using pytest to ensure the endpoint works as expected.

to run the test open the terminal in the project directory and run:
  docker-compose build  
  docker-compose up

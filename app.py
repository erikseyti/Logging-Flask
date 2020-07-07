from flask import Flask
from logging import FileHandler, WARNING

app = Flask(__name__)

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

@app.route('/')
def index():
    return "<h1>O aplicativo esta rodando!</h1>"

if __name__ == '__main__':
    app.run()

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def guess_number():
    return render_template('index.html')


app.run()

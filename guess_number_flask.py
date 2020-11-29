from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def guess_number():
    if request.method == 'GET':
        init = True
        msg = "Imagine number between 1 to 1000"
        min_ = 0
        max_ = 1001
        guess = int((max_ - min_) / 2 + min_)
    else:
        init = False
        min_ = int(request.form['min_'])
        max_ = int(request.form['max_'])
        guess = int((max_ - min_) / 2 + min_)
        msg = ""
        if 'too_small' in request.form:
            min_ = guess
            if max_ == min_:
                msg = "Don't cheat!"
                init = True
                min_ = 0
                max_ = 1001
                guess = int((max_ - min_) / 2 + min_)
        elif 'you_guessed' in request.form:
            msg = "I win. Imagine a number between 1 and 1000"
            init = True
            min_ = 0
            max_ = 1001
            guess = int((max_ - min_) / 2 + min_)
        elif 'too_much' in request.form:
            max_ = guess
            if min_ == max_:
                msg = "Don't cheat!"
                init = True
                min_ = 0
                max_ = 1001
                guess = int((max_ - min_) / 2 + min_)

    return render_template('index.html', init=init, msg=msg, min_=min_, max_=max_, guess=int((max_ - min_) / 2 + min_))


app.run()

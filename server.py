from flask import Flask, render_template


app = Flask(__name__)

# initial page for FindMyJob
@app.route('/')
def index():
    return render_template("index.html")

# send user input with POST method
@app.route('/desc', methods=['POST'])
def desc():
    # todo: user input from form tag with POST method
    # You should solve this method
    # return response within result()
    # like this `return result(responses)`
    responses = "OK"
    return result(responses)

@app.route('/result')
def result(responses):
    return render_template("result.html", responses=responses)


if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080')

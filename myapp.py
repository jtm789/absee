from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = False



@app.route('/')
def hello():
    return "Hello, world! - Flask"

@app.route('/demo', methods=['GET', 'POST'])
def greeting():
    html = ''

    html += """
    <form action="" method="post">
        <div><textarea cols="40" name="text"></textarea></div>
        <div><input type="submit" /></div>
    </form>
    """

    return html

@app.route('/book')
def hello():
    return render_template('bookprice.html')
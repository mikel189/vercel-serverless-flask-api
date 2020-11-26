from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return 'hello world. This is index speaking'

@app.route('/bread', methods=["GET","POST"])
def get_bread():
    if request.method == "POST":
        data = request.get_json(force=True)
        quantity = data['date']
        size = data['size']

        result = {
            'bread-size': size,
            'bread-quantity': quantity
        }

        return result

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
from crawler import main


app = Flask(__name__)
@app.route('/anotai', methods=['GET', 'POST'])
def welcome():
    if request.method == "POST":
        url = request.get_json(force=True)["url"]
        breakpoint()
        item, local = main(url)
        json_item = item.to_json()
        # TODO: Wait the implementation in mobile to return this one!
        #local_item =local.to_json()
        return json_item
    else:
        return "The request method was unexpected!!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

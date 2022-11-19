from flask import Flask, request
from crawler import main


app = Flask(__name__)
@app.route('/anotai', methods=['GET', 'POST'])
def welcome():
    if request.method == "POST":
        url = request.get_json(force=True)["url"]
        item, local = main(url)
        list_items = item.values.tolist()
        # TODO: Wait the implementation in mobile to return this one!
        #local_item =local.to_json()
        return list_items
    else:
        return "The request method was unexpected!!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

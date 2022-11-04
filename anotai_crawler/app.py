from flask import Flask
from crawler import main


app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    mock = "https://sat.sef.sc.gov.br/nfce/consulta?p=42220805116621000310650070000025731331831472|2|1|1|FF9A732669D99F2CBC85F5D09E4F0E1EEBD3EA9B"
    item, local = main(mock)
    json_item = item.to_json()
    local_item =local.to_json()
    return json_item
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

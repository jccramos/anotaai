import os
import google.cloud.secretmanager  as secretmanager

from flask import Flask, request
from flask_mail import Mail, Message
from crawler import main

#secrets = secretmanager.SecretManagerServiceClient()
#PROJECT_ID = "anotaai-api"

#GMAIL_AUTH_LOGIN = secrets.access_secret_version(request={"name": "projects/"+PROJECT_ID+"/secrets/gmail-auth-login/versions/1"}).payload.data.decode("utf-8")


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'equipeanotaai@gmail.com'
app.config['MAIL_PASSWORD'] = "drjnpebfebrecobb"#GMAIL_AUTH_LOGIN.replace("[", "").replace("]","")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/anotai', methods=['GET', 'POST'])
def welcome():
    if request.method == "POST":
        post_request = request.get_json(force=True)
        url = post_request["url"]
        email = post_request["email"]

        item, local = main(url)

        item.to_excel("detalhes_compra.xlsx", index=False)

        msg_local = local["local"][0]
        msg_day = local["dt_emissao"][0].split(" ")[0]
        msg_when = local["dt_emissao"][0].split(" ")[1][:5].replace(":", "h")+"min"

        msg = Message(
            f"Gastos em {msg_local}",
            sender ='equipeanotaai@gmail.com',
            recipients=[email]
        )
        msg.html = f"""
        <div><span> Ol&aacute;, agora voc&ecirc; pode ver com o que gastou em </span><strong>{msg_local}.</strong><span><br /></span></div>
        <div>&nbsp;</div>
        <div><span> A sua compra foi realizada no dia </span><strong>{msg_day}</strong><span> &agrave;s </span><strong>{msg_when}</strong><span>,</span></div>
        <div><span> os detalhes desta compra est&atilde;o no anexo deste email.</span></div>
        <div>&nbsp;</div>
        <div>&nbsp;</div>
        <div><span> N&atilde;o &eacute; &oacute;timo poder enxergar com o que voc&ecirc; gastou de fato??</span></div>
        <div><strong> Compartilhe est&aacute; ideia com seus amigos #AnotaAi :))</strong></div>
        <div>&nbsp;</div>
        <div><span>&nbsp;</span></div>
        """

        with app.open_resource("detalhes_compra.xlsx") as fp:
            msg.attach("detalhes_compra.xlsx", "detalhes_compra/xlsx", fp.read())

        mail.send(msg)

        os.remove("detalhes_compra.xlsx")

        # TODO: Wait the implementation in mobile to return this one!
        #local_item =local.to_json()
        return item.values.tolist()
    else:
        return "The request method was unexpected!!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

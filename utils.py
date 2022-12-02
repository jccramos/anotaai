from config import logger


def get_subject_elements(df):
    try:
        msg_local = df["local"][0]
        msg_day = df["dt_emissao"][0].split(" ")[0]
        msg_when = df["dt_emissao"][0].split(" ")[1][:5].replace(":", "h")+"min"
    except Exception as e:
        logger.error(f"Error in get_subject_elements: {e}")
    return msg_local, msg_day, msg_when


def compose_msg(msg_local, msg_day, msg_when):
    return f"""
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


def parse_request(request):
    try:
        post_request = request.get_json(force=True)
        url = post_request["url"]
        email = post_request["email"]
        premium_user=post_request["premium"]
        if not url.startswith("https://sat.sef.sc.gov.br/nfce/"):
            raise ValueError(f"invalid url {url}")
    except Exception as e:
        logger.error(f"Error in parse_request function for {email}: {e}")
        return None, email, premium_user
    return url, email, premium_user


def mk_massage(Message, local, premium_user, email, app):
    msg_local, msg_day, msg_when = get_subject_elements(local)
    if premium_user:
        msg = Message(
            f"Gastos em {msg_local} {email}",
            sender ='equipeanotaai@gmail.com',
            recipients=['equipeanotaai@gmail.com']
        )
    else:
        msg = Message(
            f"Gastos em {msg_local}",
            sender ='equipeanotaai@gmail.com',
            recipients=[email]
        )

    msg.html = compose_msg(msg_local, msg_day, msg_when)

    try:    
        with app.open_resource("detalhes_compra.xlsx") as fp:
            if premium_user:
                msg.attach(f"detalhes_compra_{email}.xlsx", "detalhes_compra/xlsx", fp.read())
            else:
                msg.attach(f"detalhes_compra.xlsx", "detalhes_compra/xlsx", fp.read())
    except Exception as e:
        logger.error(f"Error in mk_massage function: {e}")
    return msg
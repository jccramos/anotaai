from datetime import datetime, timezone, timedelta


def  get_subject_elements(df):
    msg_local = df["local"][0]
    msg_day = df["dt_emissao"][0].split(" ")[0]
    msg_when = df["dt_emissao"][0].split(" ")[1][:5].replace(":", "h")+"min"
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

import re


def eliminar_comentarios(html):
    return re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)


def get(context, action=None, params=None):
    if action is None:
        context.resp = context.client.get(context.url, params=params, follow_redirects=True)
    else:
        context.resp = context.client.get(action, params=params, follow_redirects=True)
    assert context.resp.status_code == 200
    context.html = eliminar_comentarios(context.resp.text)


def post(context, action=None, data=None):
    if action is None:
        context.resp = context.client.post(context.url, data=data, follow_redirects=True)
    else:
        context.resp = context.client.post(action, data=data, follow_redirects=True)
    assert context.resp.status_code == 200
    context.html = eliminar_comentarios(context.resp.text)


def arriesgar(context, intento):
    post(context, data={"intento": intento})

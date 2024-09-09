import re

from behave import given, then, when

from app import app


def get(context, action, params=None):
    return context.client.get(action, params=params, follow_redirects=True)


def post(context, action, data=None):
    return context.client.post(action, data=data, follow_redirects=True)


@given('I have a valid word "{word}"')
def step_impl(context, word):
    context.client = app.test_client()
    context.resp = post(context, "/juego", {"palabra": word})


@when("I start the game")
def step_impl(context):
    pass


@then('I should see the masked word "{expected_progress}"')
def step_impl(context, expected_progress):
    assert context.resp.status_code == 200
    # eliminar comentarios
    html = re.sub('<!--.*?-->', '', context.resp.text)
    m = re.search(r"<p\b.*?>Progreso de la palabra: (.+)</p>", html, re.IGNORECASE)
    progress = m.group(1)
    assert progress == expected_progress


@when('I guess the letter "{letter}"')
def step_impl(context, letter):
    context.resp = post(context, "/juego", {"intento": letter})


@then('I should see "{expected_progress}"')
def step_impl(context, expected_progress):
    assert context.resp.status_code == 200
    html = re.sub('<!--.*?-->', '', context.resp.text)
    m = re.search(r"<p\b.*?>Progreso de la palabra: (.+)</p>", html, re.IGNORECASE)
    progress = m.group(1)
    assert progress == expected_progress


@when('I guess the word "{word}"')
def step_impl(context, word):
    context.resp = post(context, "/juego", {"intento": word})


@then("the remaining attempts should be {expected_attempts:d}")
def step_impl(context, expected_attempts):
    assert context.resp.status_code == 200
    html = re.sub('<!--.*?-->', '', context.resp.text)
    m = re.search(r"<p\b.*?>Intentos restantes: (\d+)</p>", html, re.IGNORECASE)
    intentos = int(m.group(1))
    assert intentos == expected_attempts

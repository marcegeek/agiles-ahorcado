import re

from behave import given, then, when
from environment import arriesgar, post

from app import app


@given('I have started the game with a valid word "{word}"')
def step_impl(context, word):
    context.client = app.test_client()
    context.url = "/juego"
    post(context, data={"palabra": word})


@then('I should see the progress "{expected_progress}"')
def step_impl(context, expected_progress):
    m = re.search(r"<p\b.*?>Progreso de la palabra: (.+)</p>", context.html, re.IGNORECASE)
    progress = m.group(1)
    assert progress == expected_progress


@when('I guess the letter "{letter}"')
def step_impl(context, letter):
    arriesgar(context, letter)


@when('I guess the word "{word}"')
def step_impl(context, word):
    arriesgar(context, word)


@then("the remaining attempts should be {expected_attempts:d}")
def step_impl(context, expected_attempts):
    m = re.search(r"<p\b.*?>Intentos restantes: (\d+)</p>", context.html, re.IGNORECASE)
    intentos = int(m.group(1))
    assert intentos == expected_attempts


@then('the game result should be "{result}"')
def step_impl(context, result):
    assert re.search(rf"\b{result}\b", context.html, re.IGNORECASE)

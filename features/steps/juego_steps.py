from behave import given, when, then
from juego import Juego


@given('I have a valid word "{word}"')
def step_impl(context, word):
    context.juego = Juego(palabra=word)


@when("I start the game")
def step_impl(context):
    pass


@then('I should see the masked word "{expected_progress}"')
def step_impl(context, expected_progress):
    assert context.juego.mostrarProgresoPalabra() == expected_progress


@when('I guess the letter "{letter}"')
def step_impl(context, letter):
    context.resultado = context.juego.arriesgarLetra(letter)


@then('I should see "{expected_progress}"')
def step_impl(context, expected_progress):
    assert context.juego.mostrarProgresoPalabra() == expected_progress


@when('I guess the word "{word}"')
def step_impl(context, word):
    context.resultado = context.juego.arriesgarPalabra(word)


@then("the remaining attempts should be {expected_attempts:d}")
def step_impl(context, expected_attempts):
    assert context.juego.intentosDisponibles() == expected_attempts

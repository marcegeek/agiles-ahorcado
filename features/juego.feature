Feature: Juego de Ahorcado

  Scenario: Iniciar un nuevo juego
    Given I have started the game with a valid word "python"
    Then I should see the progress "______"

  Scenario: Adivinar una letra correcta
    Given I have started the game with a valid word "python"
    When I guess the letter "p"
    Then I should see the progress "p_____"

  Scenario: Adivinar una letra incorrecta
    Given I have started the game with a valid word "python"
    When I guess the letter "z"
    Then the remaining attempts should be 5

  Scenario: Adivinar una palabra incorrecta
    Given I have started the game with a valid word "python"
    When I guess the word "java"
    Then the remaining attempts should be 4

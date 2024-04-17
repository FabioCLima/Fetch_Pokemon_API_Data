from src.api_interaction import fetch_pokemon_api


def test_fetch_pokemon_api_success():
    """
    Test case to verify successful fetching of Pokemon data.

    Given:
        A valid URL to the PokeAPI.

    When:
        Calling the fetch_pokemon_api function with the valid URL.

    Then:
        Verify that the result is a dictionary containing Pokemon data.
    """

    # Given
    url_pokemon = "https://pokeapi.co/api/v2/pokemon"

    # When
    result = fetch_pokemon_api(url_pokemon)

    # Then
    assert isinstance(result, dict), "Result should be a dictionary"


def test_fetch_pokemon_api_non_valid_url():
    """
    Test case to verify handling of non-valid URL.

    Given:
        A non-valid URL to the PokeAPI.

    When:
        Calling the fetch_pokemon_api function with the non-valid URL.

    Then:
        Verify that the result is an empty dictionary indicating failure to
        fetch data.
    """

    # Given
    url_non_valid = "https://pokeapi.co/api/v2/non_existing_endpoint"

    # When
    result = fetch_pokemon_api(url_non_valid)

    # Then
    assert result == {}, "Result is an empty dictionary for non-valid URL"

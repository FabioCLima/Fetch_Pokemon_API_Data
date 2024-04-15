from src.api_interaction import fetch_pokemon_api


def test_fetch_pokemon_api_success():
    # Given
    url_pokemon = "https://pokeapi.co/api/v2/pokemon"

    # When
    result = fetch_pokemon_api(url_pokemon)

    # Then
    assert isinstance(result, dict), "Result should be a dictionary"


def test_fetch_pokemon_api_non_valid_url():
    # Given
    url_non_valid = "https://pokeapi.co/api/v2/non_existing_endpoint"

    # When
    result = fetch_pokemon_api(url_non_valid)

    # Then
    assert result == {}, "Result is an empty dictionary for non-valid URL"

# tests/test_data_processing.py

import pytest
from src.data_processing import (process_pokemon_name,
                                 process_pokemon_info,
                                 display_pokemon_info
                                 )


def test_process_pokemon_name(monkeypatch):
    # Define a mock response for fetch_pokemon_api
    mock_response = {
        "results": [
            {"name": "bulbasaur"},
            {"name": "ivysaur"},
            {"name": "venusaur"},
            # Add more sample data as needed, but limit to 20 names
            {"name": "charmander"},
            {"name": "charmeleon"},
            {"name": "charizard"},
            {"name": "squirtle"},
            {"name": "wartortle"},
            {"name": "blastoise"},
            {"name": "caterpie"},
            {"name": "metapod"},
            {"name": "butterfree"},
            {"name": "weedle"},
            {"name": "kakuna"},
            {"name": "beedrill"},
            {"name": "pidgey"},
            {"name": "pidgeotto"},
            {"name": "pidgeot"},
            {"name": "rattata"},
            {"name": "raticate"}
        ]
    }

    # Define a mock implementation for fetch_pokemon_api
    def mock_fetch_pokemon_api(url):
        return mock_response

    # Apply the monkeypatch to replace fetch_pokemon_api with the mock implementation
    monkeypatch.setattr("src.api_interaction.fetch_pokemon_api", mock_fetch_pokemon_api)

    # Call the function under test
    result = process_pokemon_name()

    # Assert that the result matches the expected output (first 20 names)
    expected_result = [
        "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon",
        "charizard", "squirtle", "wartortle", "blastoise", "caterpie",
        "metapod", "butterfree", "weedle", "kakuna", "beedrill", "pidgey",
        "pidgeotto", "pidgeot", "rattata", "raticate"
    ]
    assert result == expected_result[:20]


def test_process_pokemon_info(monkeypatch):
    # Given
    pokemon_names = ["bulbasaur", "ivysaur"]

    # Define a mock implementation for fetch_pokemon_api
    def mock_fetch_pokemon_api(url):
        # Extract the pokemon name from the URL
        pokemon_name = url.split('/')[-1]
        # Define mock response based on the pokemon name
        mock_response = {
            "id": pokemon_names.index(pokemon_name) + 1,  # IDs start from 1
            "name": pokemon_name,
            "height": 5,  # Dummy values for height and weight
            "weight": 100,
            "base_experience": 21,
            "is_default": True
        }
        return mock_response

    # Apply the monkeypatch to replace fetch_pokemon_api with the mock implementation
    monkeypatch.setattr("src.api_interaction.fetch_pokemon_api", mock_fetch_pokemon_api)

    # When
    result = process_pokemon_info(pokemon_names)

    # Then
    assert isinstance(result, list)  # Ensure result is a list

    # Check that each item in the list is a dictionary
    for pokemon_info in result:
        assert isinstance(pokemon_info, dict)

        # Check if all expected keys are present in the dictionary
        expected_keys = ["id", "name", "height", "weight", "experience", "is_default"]
        for key in expected_keys:
            assert key in pokemon_info

    # Check if IDs start from 1 and increment correctly
    expected_ids = [1, 2]
    for idx, pokemon_info in enumerate(result):
        assert pokemon_info["id"] == expected_ids[idx]


@pytest.mark.parametrize("pokemon_info", [
    [
        {"id": 1, "name": "bulbasaur", "height": 7, "weight": 69, "experience": 64, "is_default": True},
        {"id": 2, "name": "ivysaur", "height": 10, "weight": 130, "experience": 142, "is_default": True},
        {"id": 3, "name": "venusaur", "height": 20, "weight": 1000, "experience": 263, "is_default": True}
    ]
])
def test_display_pokemon_info(capsys, monkeypatch, pokemon_info):
    # Mock the process_pokemon_name function to return a sample list of pokemon names
    monkeypatch.setattr("src.data_processing.process_pokemon_name", lambda: ["bulbasaur", "ivysaur", "venusaur"])

    # Mock the process_pokemon_info function to return the sample pokemon info
    monkeypatch.setattr("src.data_processing.process_pokemon_info", lambda _: pokemon_info)

    # Call the function under test
    display_pokemon_info()

    # Capture the printed output
    captured = capsys.readouterr()

    # Ensure that the displayed output contains the information of the first Pokemon in the list
    assert f'{pokemon_info[0]}' in captured.out

"""
This module will get the function fetch_pokemon_api, which fetch data from the
PokeAPI and process them.
"""

import logging
from typing import List, Dict, Any
from pathlib import Path
import pandas as pd
from api_interaction import fetch_pokemon_api

# Get the module name dynamically
module_name = __name__.rsplit(".", maxsplit=1)[-1]

# Configure logging
logs_dir = Path("./logs")
logs_dir.mkdir(exist_ok=True)
log_file = logs_dir / f"{module_name}.log"

logging.basicConfig(
    filename=str(log_file),  # Convert Path object to string
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Global variable for PokeAPI base URL
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def fetch_all_pokemon_names() -> List[str]:
    """
    Fetches all Pokemon names from the PokeAPI by handling pagination.

    Returns:
        List[str]: A list of all Pokemon names.
    """
    all_pokemon_names = []
    next_page = POKEAPI_BASE_URL

    while next_page:
        try:
            pokemon_data = fetch_pokemon_api(next_page)
            pokemon_names = [
                pokemon.get("name", None) for pokemon in
                pokemon_data.get("results", [])
            ]
            all_pokemon_names.extend(pokemon_names)
            next_page = pokemon_data.get("next")
        except Exception as error:
            logging.error("Failed to fetch Pokemon names: %s", error)
            return []

    return all_pokemon_names


def process_pokemon_name() -> List[str]:
    """
    Fetches the list of Pokemon names from the PokeAPI.

    Returns:
        List[str]: A list of Pokemon names.
    """
    try:
        pokemon_names = fetch_all_pokemon_names()
        logging.info("Total Pokemon names fetched: %d", len(pokemon_names))
        return pokemon_names
    except Exception as error:
        logging.error("Failed to fetch Pokemon names: %s", error)
        return []


def process_pokemon_info(pokemon_names: List[str]) -> List[Dict[str, Any]]:
    """
    Processes information for each Pokemon in the given list.

    Args:
        pokemon_names (List[str]): List of Pokemon names.

    Returns:
        List[Dict[str, any]]: Processed information for each Pokemon.
    """

    all_pokemon_info = []

    # Iterate over each pokemon name
    for pokemon_name in pokemon_names:
        pokemon_info_name_endpoint = f"{POKEAPI_BASE_URL}{pokemon_name}"
        try:
            pokemon_info_name = fetch_pokemon_api(pokemon_info_name_endpoint)
            if pokemon_info_name:
                pokemon_info = {
                    "id": pokemon_info_name.get("id"),
                    "name": pokemon_name,
                    "height": pokemon_info_name.get("height"),
                    "weight": pokemon_info_name.get("weight"),
                    "experience": pokemon_info_name.get("base_experience"),
                    "is_default": pokemon_info_name.get("is_default"),
                }
                all_pokemon_info.append(pokemon_info)

        except Exception as error:
            logging.error(
                "Failed to fetch info for %s: %s", pokemon_name, error
                )

    return all_pokemon_info


def save_to_pokemon_data(pokemon_info: List[Dict[str, Any]]) -> None:
    """
    Saves the Pokemon information to a CSV file.

    Args:
        pokemon_info (List[Dict[str, Any]]): List of dictionaries containing
        Pokemon information.
    """
    # Convert the list of dictionaries to a pandas DataFrame
    pokemon_df = pd.DataFrame(pokemon_info)

    # Define the path to save the CSV file
    data_dir = Path("./data")
    data_dir.mkdir(exist_ok=True)
    csv_file = data_dir / "pokemon_data.csv"

    # Save the DataFrame as a CSV file
    pokemon_df.to_csv(csv_file, index=False)


def display_pokemon_info() -> None:
    """
    Displays information for a sample list of Pokemon.
    """
    # Get a sample pokemon name
    pokemon_names = process_pokemon_name()

    # Process and display pokemon info
    pokemon_info = process_pokemon_info(pokemon_names)
    logging.info("Sample Pokemon info: %s", pokemon_info[0])

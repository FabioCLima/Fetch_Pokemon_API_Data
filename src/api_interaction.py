"""
api_interaction.py - Module for interacting with the PokeAPI

This module provides functionality to fetch Pokemon data from the PokeAPI.
It includes a function to fetch Pokemon data from a specified URL and log
any errors that occur during the process.

Usage examples:
1. Fetch Pokemon data from the default URL:
    data = fetch_pokemon_api()

2. Fetch Pokemon data from a custom URL:
    custom_url = "https://pokeapi.co/api/v2/pokemon/charizard"
    data = fetch_pokemon_api(custom_url)

3. Handle errors gracefully:
    data = fetch_pokemon_api("invalid_url")  # Invalid URL
    if not data:
        print("Failed to fetch Pokemon data. Check logs for details.")

"""

import logging
from pathlib import Path
from typing import Optional, Dict, Any
import requests
from requests import RequestException


# Dynamically get the module name
module_name = __name__.rsplit('.', maxsplit=1)[-1]

# Create logs directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=log_dir / f"{module_name}.log",
)


def fetch_pokemon_api(
    url_pokemon: Optional[str] = "https://pokeapi.co/api/v2/pokemon",
) -> Dict[str, Any]:
    """
    Fetches Pokemon data from the specified URL.

    Args:
        url_pokemon (str, optional): The URL of the Pokemon API. Defaults to
        "https://pokeapi.co/api/v2/pokemon".

    Returns:
        dict: A dictionary containing the Pokemon data.

    Raises:
        RequestException: If there is an error making the API request.
        ValueError: If there is an error parsing the JSON response.
    """
    try:
        with requests.Session() as session:
            with session.get(url=url_pokemon, timeout=10) as response:
                response.raise_for_status()
                data = response.json()
                logging.info("The data fetched from PokeAPI were %s", data)
                return data

    except RequestException as error:
        logging.error(
            "Error fetching information from the API %(cep)s: %(error)s",
            extra={"url": url_pokemon, "error": error},
            )
        return {}

    except ValueError as error:
        logging.error(
            "Invalid JSON: for %(url)s: %(error)s",
            extra={"url": url_pokemon, "error": error}
        )
        return {}

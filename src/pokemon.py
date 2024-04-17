"""
This module orchestrates the process of fetching data from the PokeAPI,
processing the data, and saving it to a CSV file.

It contains functions to fetch Pokemon data from the PokeAPI, process the
fetched data, and save the processed data to a CSV file.

Functions:
    - orchestrate_pokeapi: Orchestrates the process of fetching Pokemon data
    from the PokeAPI, processing it, and saving it to a CSV file.
"""

from pathlib import Path
import logging
from api_interaction import fetch_pokemon_api
from data_processing import (
    process_pokemon_name,
    process_pokemon_info,
    save_to_pokemon_data,
    display_pokemon_info
)
from utils import timer

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


@timer
def orchestrate_pokeapi():
    """
    Orchestrates the process of fetching Pokemon data from the PokeAPI,
    processing it, and saving it to a CSV file.
    """

    logging.info(
        "Starting fetch data from PokeAPI use this module in the AirFlow, "
        "to orchestrate the process for us, first on my machine and then in "
        "the AWS cloud service."
    )

    data = fetch_pokemon_api()
    total_number_pokemon = data.get("count", None)
    logging.info(
        "The total of pokemons will fetched are: %s", total_number_pokemon
        )

    # Process pokemon data
    pokemon_names = process_pokemon_name()
    pokemon_info = process_pokemon_info(pokemon_names)
    save_to_pokemon_data(pokemon_info)
    display_pokemon_info()


if __name__ == "__main__":
    orchestrate_pokeapi()

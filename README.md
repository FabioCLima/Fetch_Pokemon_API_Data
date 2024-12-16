# Fetch_Pokemon_API_Data

This project aims to demonstrate how to fetch data from a public API such as the Pokemon API (PokeAPI), orchestrate the data extraction process using Apache Airflow, and deploy the project to cloud services like AWS.

## Project Structure

```
Fetch_Pokemon_API_Data/
├── data/
├── figs/
├── logs/
├── src/
│   ├── api_interaction.py
│   ├── data_processing.py
│   ├── pokemon.py
│   └── utils.py
└── tests/
```

## Description

### api_interaction.py - Module

Module for interacting with the PokeAPI. This module provides functionality to fetch Pokemon data from the PokeAPI, including error logging.

### data_processing.py - Module

Module for processing Pokemon data fetched from the PokeAPI. It includes functions to fetch all Pokemon names, process Pokemon names, process Pokemon information, save Pokemon data to a CSV file, and display Pokemon information.

### utils.py - Module

Module containing utility functions, including a decorator to measure the execution time of a function.

### pokemon.py - Entry Point Module

This module orchestrates the process of fetching data from the PokeAPI, processing it, and saving it to a CSV file. It contains the `orchestrate_pokeapi` function, which is the entry point of the project.

## How to Run

### Using Apache Airflow

To run the orchestration of fetching data from the PokeAPI with Apache Airflow, follow these steps:

1. **Copy Files to Airflow Directory**: Copy all Python files related to `pokemon.py` (including `pokemon.py` itself) to the `dags` directory in your Airflow installation. Additionally, create a file named `pokemon_extraction_config.py` with the following content:

   ```python
   from datetime import datetime
   from airflow import DAG
   from airflow.operators.python_operator import PythonOperator
   from airflow.operators.dummy_operator import DummyOperator
   from pokemon import orchestrate_pokeapi

   default_args = {
       "owner": "Fabio Lima",
       "start_date": datetime(2023, 3, 10),  # A past date
   }

   dag = DAG(
       "extract_data_from_pokeapi",
       default_args=default_args,
       description="DAG to extract from PokeAPI",
       schedule_interval="0 10 * * *",  # Run daily at 10:00 AM UTC
       max_active_runs=1,
   )

   start_pipeline = DummyOperator(task_id="start_pipeline", dag=dag)

   extract_pokeapi_data = PythonOperator(
       task_id="extraction_pokemon_information_from_pokeapi",
       python_callable=orchestrate_pokeapi,
       op_args=[],  # No arguments needed for the function
       dag=dag,
   )

   done_pipeline = DummyOperator(task_id="done_pipeline", dag=dag)

   start_pipeline >> extract_pokeapi_data >> done_pipeline
   ```

2. **Start Airflow Services**:

   - Start the Airflow web server:
     ```bash
     airflow webserver --port 8080
     ```
   - Start the Airflow scheduler:
     ```bash
     airflow scheduler
     ```

3. **Open Airflow UI**: Open `http://localhost:8080/home` in your browser and start the orchestration.

## Conclusion

With Apache Airflow, you can easily orchestrate the process of fetching data from the PokeAPI and processing it. This project demonstrates a modular approach to data extraction, processing, and orchestration, making it easier to develop and maintain complex data pipelines.

---



"""         # Pretty print the JSON response
        print(json.dumps(data, indent=4))

    # Example: Print the count of available Pokemon
    print("\nTotal Pokemon: ", data.get("count"))

    # Print the limit of pagination
    total_pokemons_per_query = int(data.get('next').split("=")[-1])
    print(
        "Limit of data information will print out per requisition: "
        f"{total_pokemons_per_query}"
    ) """

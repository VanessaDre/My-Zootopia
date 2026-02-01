import json


def load_data(file_path):
    """Loads a JSON file and returns the parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    """Reads animals_data.json and prints name, diet, first location, and type if available."""
    animals_data = load_data("animals_data.json")

    for animal in animals_data:
        if not isinstance(animal, dict):
            continue

        name = animal.get("name")

        diet = animal.get("diet")
        if diet is None and isinstance(animal.get("characteristics"), dict):
            diet = animal["characteristics"].get("diet")

        locations = animal.get("locations")
        first_location = None
        if isinstance(locations, list) and len(locations) > 0:
            first_location = locations[0]

        animal_type = animal.get("type")
        if animal_type is None and isinstance(animal.get("characteristics"), dict):
            animal_type = animal["characteristics"].get("type")

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if first_location:
            print(f"Location: {first_location}")
        if animal_type:
            print(f"Type: {animal_type}")

        print()


if __name__ == "__main__":
    main()

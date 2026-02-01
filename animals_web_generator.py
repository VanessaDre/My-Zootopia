import json


def load_data(file_path):
    """Loads a JSON file and returns the parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    """Reads animals_data.json and prints name, diet, first location, and type if available."""
    animals_data = load_data("animals_data.json")

    output = ""

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

        output += '<li class="cards__item">\n'

        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if first_location:
            output += f"Location: {first_location}<br/>\n"
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"

        output += "</li>\n"

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template = handle.read()

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html)

if __name__ == "__main__":
    main()

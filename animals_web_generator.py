import json

TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
DATA_FILE = "animals_data.json"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    if not isinstance(animal, dict):
        return ""

    name = animal.get("name")

    diet = animal.get("diet")
    if diet is None and isinstance(animal.get("characteristics"), dict):
        diet = animal["characteristics"].get("diet")

    locations = animal.get("locations")
    first_location = None
    if isinstance(locations, list) and locations:
        first_location = locations[0]

    animal_type = animal.get("type")
    if animal_type is None and isinstance(animal.get("characteristics"), dict):
        animal_type = animal["characteristics"].get("type")

    output = '<li class="cards__item">\n'

    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if first_location:
        output += f'    <strong>Location:</strong> {first_location}<br/>\n'
    if animal_type:
        output += f'    <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def get_skins(animal_data_list):
    output = ""
    for animal in animal_data_list:
        output += serialize_animal(animal)
    return output


def write_html_to_file(html, file_path):
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(html)


def main():
    animals_data = load_data(DATA_FILE)
    output = get_skins(animals_data)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as handle:
        template = handle.read()

    new_html = template.replace(PLACEHOLDER, output)
    write_html_to_file(new_html, OUTPUT_FILE)


if __name__ == "__main__":
    main()

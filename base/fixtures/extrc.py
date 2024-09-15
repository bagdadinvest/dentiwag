import json
import re

# Placeholder template
PLACEHOLDER_TEMPLATE = "__TEXT_PLACEHOLDER_{}__"

def has_more_than_three_numbers(s):
    # Count the number of digits in the string
    return len(re.findall(r'\d', s)) > 3

def extract_and_replace_text(json_data):
    extracted_texts = {}
    placeholder_counter = 1

    def recursive_replace(obj):
        nonlocal placeholder_counter
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, (dict, list)):
                    obj[key] = recursive_replace(value)
                elif isinstance(value, str):
                    if not has_more_than_three_numbers(value):
                        placeholder = PLACEHOLDER_TEMPLATE.format(placeholder_counter)
                        extracted_texts[placeholder] = value
                        placeholder_counter += 1
                        obj[key] = placeholder
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = recursive_replace(item)
        return obj

    return recursive_replace(json_data), extracted_texts

# Load your JSON data
with open('/home/lofa/Downloads/xx/bakerydemo/bakerydemo/base/fixtures/bakerydemo.json', 'r') as file:
    data = json.load(file)

# Extract text and get placeholders
modified_data, extracted_texts = extract_and_replace_text(data)

# Save the modified JSON and extracted texts
with open('/home/lofa/Downloads/xx/bakerydemo/bakerydemo/base/fixtures/modified_bakerydemo.json', 'w') as file:
    json.dump(modified_data, file, indent=2)

with open('/home/lofa/Downloads/xx/bakerydemo/bakerydemo/base/fixtures/extracted_texts.json', 'w') as file:
    json.dump(extracted_texts, file, indent=2)

print("Extraction and replacement complete.")

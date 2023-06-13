import argparse
import string
import json
import yaml

parser = argparse.ArgumentParser(description='Konwersja plików XML, JSON i YAML.')

parser.add_argument('input_file', type=str, help='Nazwa pliku wejściowego.')
parser.add_argument('output_file', type=str, help='Nazwa pliku wyjściowego.')
parser.add_argument('format', type=str, help='Format pliku')

args = parser.parse_args()

input_file_extension = args.input_file.split('.')[-1].lower()

print("Plik wejściowy:", args.input_file)
print("Plik wyjściowy:", args.output_file)
print("Format:", args.format)
print("Rozszerzenie pliku wejściowego:", input_file_extension)

if input_file_extension == 'json':
    try:
        with open(args.input_file, 'r') as file:
            json_data = json.load(file)
        print("Składnia pliku jest poprawna.")

        with open(args.output_file, 'w') as file:
            json.dump(json_data, file)
        print("Dane zostały zapisane do pliku w formacie JSON.")

    except FileNotFoundError:
        print("Plik wejściowy nie został znaleziony.")
    except json.JSONDecodeError:
        print("Nieprawidłowa składnia JSON.")

elif input_file_extension == 'yml' or input_file_extension == 'yaml':
    try:
        with open(args.input_file, 'r') as file:
            yaml_data = yaml.safe_load(file)
        print("Składnia pliku jest poprawna.")

    except FileNotFoundError:
        print("Plik wejściowy nie został znaleziony.")
    except yaml.YAMLError as exc:
        print("Nieprawidłowa składnia YAML:", exc)

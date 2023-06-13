import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def convert_file(input_file, output_file):
    input_file_extension = input_file.split('.')[-1].lower()
    output_file_extension = output_file.split('.')[-1].lower()

    if input_file_extension == 'json':
        try:
            with open(input_file, 'r') as file:
                json_data = json.load(file)

            if output_file_extension == 'xml':
                root = ET.Element('root')
                for key, value in json_data.items():
                    child = ET.SubElement(root, key)
                    child.text = str(value)
                tree = ET.ElementTree(root)
                tree.write(output_file)
            elif output_file_extension in ('yml', 'yaml'):
                with open(output_file, 'w') as file:
                    yaml.dump(json_data, file)

            print("Konwersja zakończona sukcesem.")

        except FileNotFoundError:
            print("Plik wejściowy nie został znaleziony.")
        except json.JSONDecodeError:
            print("Nieprawidłowa składnia JSON.")

    elif input_file_extension in ('yml', 'yaml'):
        try:
            with open(input_file, 'r') as file:
                yaml_data = yaml.safe_load(file)

            if output_file_extension == 'xml':
                root = ET.Element('root')
                for key, value in yaml_data.items():
                    child = ET.SubElement(root, key)
                    child.text = str(value)
                tree = ET.ElementTree(root)
                tree.write(output_file)
            elif output_file_extension == 'json':
                with open(output_file, 'w') as file:
                    json.dump(yaml_data, file)

            print("Konwersja zakończona sukcesem.")

        except FileNotFoundError:
            print("Plik wejściowy nie został znaleziony.")
        except yaml.YAMLError as exc:
            print("Nieprawidłowa składnia YAML: {}".format(exc))

    elif input_file_extension == 'xml':
        try:
            tree = ET.parse(input_file)
            root = tree.getroot()

            if output_file_extension == 'json':
                data = {}
                for element in root:
                    data[element.tag] = element.text
                with open(output_file, 'w') as file:
                    json.dump(data, file)
            elif output_file_extension in ('yml', 'yaml'):
                data = {}
                for element in root:
                    data[element.tag] = element.text
                with open(output_file, 'w') as file:
                    yaml.dump(data, file)

            print("Konwersja zakończona sukcesem.")

        except FileNotFoundError:
            print("Plik wejściowy nie został znaleziony.")
        except ET.ParseError as exc:
            print("Nieprawidłowa składnia XML: {}".format(exc))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)')
    parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    convert_file(input_file, output_file)

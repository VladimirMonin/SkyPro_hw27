import csv
import json

JSON_FILE1 = r'./data/ads.json'
CSV_FILE1 = r'./raw_data/ads.csv'

JSON_FILE2 = r'./data/categories.json'
CSV_FILE2 = r'./raw_data/categories.csv'


def clean_csv_data(data_list: list[dict]) -> list[dict]:
    """
    Превращает строковые значения ID в целочисленные, так же приводит ключи Id и id к pk.
    Приводит строковые true false к булевым
    Приводит цены из строк к целочисленным
    :param data_list: Список данных из csv
    :return: list
    """
    for row in data_list:
        # Причесали ключи
        if 'Id' in row.keys():
            row['pk'] = int(row.pop('Id'))
        if 'id' in row.keys():
            row['pk'] = int(row.pop('id'))
        # Причесали булевы значения
        if 'is_published' in row.keys():
            if row['is_published'] == 'TRUE':
                row['is_published'] = True
            else:
                row['is_published'] = False
        # Причесали цены
        if 'price' in row.keys():
            row['price'] = int(row['price'])

    return data_list


def csv_to_json(csv_file, json_file):
    """
    Принимает адрес csv и отдает json файл. Использует функцию "очистки" данных
    :param csv_file: csv_file path
    :param json_file: json_file path
    :return: rewrite json_file
    """
    with open(csv_file, encoding='utf-8') as csvfile:
        csv_row = csv.DictReader(csvfile)
        data_list = [row for row in csv_row]
        data_list = clean_csv_data(data_list)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data_list, indent=4, ensure_ascii=False))


def read_json_file(json_file):
    with open(json_file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


csv_to_json(CSV_FILE1, JSON_FILE1)
csv_to_json(CSV_FILE2, JSON_FILE2)



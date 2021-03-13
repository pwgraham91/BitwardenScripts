import csv
import json


def get_essential_items(loaded_json):
    excluded_folder_ids = get_excluded_folder_ids(loaded_json['folders'])
    essential_items = []
    for item in loaded_json['items']:
        if (item.get('folderId') is None
                or item['folderId'] not in excluded_folder_ids) \
                and item['type'] == 1 \
                and item['login'].get('password') is not None \
                and '•' not in item['login']['password'] \
                and item['login'].get('username') is not None \
                and 'flosports' not in item['login']['username']:
            essential_item = [
                item['name'],
                item['login']['username'],
                item['login']['password'],
            ]
            if item['login'].get('uris') is not None:
                essential_item.append([uri['uri'] for uri in item['login']['uris']])

            essential_items.append(essential_item)
    return essential_items


def get_excluded_folder_ids(folders):
    excluded_folder_ids = set()
    excluded_folder_names = {'FloSports'}
    for folder in folders:
        if folder['name'] in excluded_folder_names:
            excluded_folder_ids.add(folder['id'])
    return excluded_folder_ids


def write_to_csv(essential_items):
    with open('bw_essential.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'username', 'password', 'urls'])
        for item in essential_items:
            writer.writerow(item)


def run():
    with open('bw.json') as f:
        essential_items = get_essential_items(json.load(f))
    write_to_csv(essential_items)


if __name__ == "__main__":
    run()

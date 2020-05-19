import csv
import orjson
import json

def json_to_md_table(file_to_convert: str, filename: str, num_to_convert=-1):
    """
    :param file_to_convert: str path or filename. Must be json file
    :param filename: str -> Pass the filename without the extension
    :param num_to_convert: leave empty to convert everything or choose a number to convert that amount of elements.
    :return: An md file with the json data converted to an md table.
    """
    with open(f'{filename}.md', 'w+') as file:
        file.write(f'Job Title | Category | Location | Date Posted | Application Url \n'
                   f'------------ | ------------- | ------------ | ------------ | ------------\n')

    with open(f'{file_to_convert}', encoding='utf_8') as f:
        elements = json.load(f)

    for item in elements[:num_to_convert]:
        with open(f'{filename}.md', 'a+', encoding='utf_8') as jobs:
            jobs.write(f"{item['Title']} | {item['Category']} | {item['Location']} | {item['Date Posted']} | [Apply]({item['Url']})\n")


json_to_md_table('appl.json', 'apple_jobs', 10)
import csv
import pandas as pd

def csv_to_md(file_to_convert: str, filename: str):
    """
    :param file_to_convert: str path or filename. Must be csv file
    :param filename: str -> Pass the filename without the extension
    :return: An md file with the csv data converted to an md table.
    """
    with open(f'{filename}.md', 'w+') as file:
        file.write(f'Job Title | Company | Location | Description | Skills | Application Url \n'
                   f'------------ | ------------- | ------------ | ------------ | ------------ | -----\n')

    with open(file_to_convert, "r", encoding="utf8")as job_details:
        reader = csv.reader(job_details)
        for idx, row in enumerate(reader):
            if idx >= 0:
                # print(idx, row)
                with open(f'{filename}.md', 'a+') as jobs:
                    jobs.write(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | [Apply]({row[5]})\n")


def add_to_csv(job_dict, file_name: str):
    """
    Uses pandas to convert a dictionary to a csv file.
    :param job_dict: Dictionary
    :param file_name: name of the csv to be created
    :return:
    """
    # data = job_dict
    df = pd.DataFrame([job_dict], columns=['Job Title', 'Company', 'Location', 'Description', 'Skills', "Application Url"])
    df.to_csv(f'{file_name}.csv', mode='a+', header=False, index=False)


def remove_duplicate_rows(csv_file: str):
    """
    Removes the duplicates from a csv file
    :param csv_file: csv file with extension
    :return:
    """
    df = pd.read_csv(csv_file)
    remove_dups_df = df.drop_duplicates(keep="first")
    return remove_dups_df.to_csv(csv_file, index=False)


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


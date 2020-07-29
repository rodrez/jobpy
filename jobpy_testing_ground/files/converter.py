import csv
import json
import pandas as pd


def csv_to_md(file_to_convert: str, filename: str):
    """ Converts csv file to md table

        Parameters
        ----------
        file_to_convert: str
            Path or filename of the file name to convert. It does not require the extension. MUST be a csv file.

        filename: str
            Output filename desired. Does not need the extension. 

        Returns
        -------
            Md file with a table based on the csv data provided and named after your chosen filename.

        """

    with open(f'{filename}.md', 'w+') as file:
        file.write(f'Job Title | Company | Location | Description | Skills | Application Url \n'
                   f'------------ | ------------- | ------------ | ------------ | ------------ | -----\n')

    with open(f'{file_to_convert}.csv', "r", encoding="utf8")as job_details:
        reader = csv.reader(job_details)
        for idx, row in enumerate(reader):
            if idx >= 0:
                # print(idx, row)
                with open(f'{filename}.md', 'a+') as jobs:
                    jobs.write(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | [Apply]({row[5]})\n")


def add_to_csv(dictionary, filename):
    """ Uses pandas to convert a dictionary to a csv file.

            Parameters
            ----------
            dictionary: dict
                Any dictionary
                

            filename: str
                Output filename desired. Does not need the extension. 

            Returns
            -------
             File
                csv file based on the dictionary data provided and named after your chosen filename.

            """

    df = pd.DataFrame([dictionary],
                      columns=['Job Title', 'Company', 'Location', 'Description', 'Skills', "Application Url"])
    df.to_csv(f'{filename}.csv', mode='a+', header=False, index=False)


def remove_duplicate_rows(csv_file):
    """ Removes the duplicates from a csv file

                Parameters
                ----------
                csv_file: str
                    Any csv file without the extension

                Returns
                -------
                 File
                    The same file given with the duplicate rows removed.

                """
    df = pd.read_csv(f'{csv_file}.csv')
    remove_dups_df = df.drop_duplicates(keep="first")
    return remove_dups_df.to_csv(f'{csv_file}.csv', index=False)


def json_to_md_table(file_to_convert, filename, num_to_convert=-1):
    """ Removes the duplicates from a csv file

                    Parameters
                    ----------
                    file_to_convert : str
                        Any json file without the extension. MUST be json file.
                    
                    filename : str
                        Desired output name without the extension
                    
                    num_to_convert : int, optional
                        Values are index based. Default value is -1 and converts all the data.
                        The number represents the amount of rows to convert.
                    
                    Returns
                    -------
                     File : Md
                        A file with the given output name and data converted to MD table.

                    """

    with open(f'{filename}.md', 'w+') as file:
        file.write(f'Job Title | Category | Location | Date Posted | Application Url \n'
                   f'------------ | ------------- | ------------ | ------------ | ------------\n')

    with open(f'{file_to_convert}', encoding='utf_8') as f:
        elements = json.load(f)

    for item in elements[:num_to_convert]:
        with open(f'{filename}.md', 'a+', encoding='utf_8') as jobs:
            jobs.write(
                f"{item['Title']} | {item['Category']} | {item['Location']} | {item['Date Posted']} | [Apply]({item['Url']})\n")

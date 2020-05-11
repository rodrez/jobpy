from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import datetime

job = 'software engineer'
location = 'Mechanicsburg, PA'


def add_to_csv(job_dict):
    """
    Uses pandas to convert a dictionary to a csv file.
    :param job_dict: Dictionary
    :return:
    """
    # data = job_dict
    df = pd.DataFrame([job_dict])
    df.to_csv('panda_job_data.csv', mode='a+', header=False, index=False)


def grab_jobs(job_title, job_location):
    """
    Grabs the link for each job container and saves it to saved_jobs
    Removes the sign in link to avoid signing in to the CB page.
    :param job_title: str -> desired job to be searched
    :param job_location: str -> desired location to be searched
    :return:
    """
    web = requests.get(
        f"https://www.careerbuilder.com/jobs?keywords={job_title}&location={job_location}&sort=date_desc").text
    soup = BeautifulSoup(web, 'html.parser')

    # Career Builder sign in url. Used later to avoid signing in to grab the data.
    sign_in_url = "https://www.careerbuilder.com/user/sign-in?next="
    job_containers = soup.select('.data-results-content-parent')

    # Empty list used to store the values of the for loop below
    saved_jobs = []

    for idx, jobs in enumerate(job_containers):
        # CB has a required signing link and we use the replace method to bypass it.
        saved_jobs.append(f'{job_containers[idx].a.get("href", None).replace(sign_in_url, "")}')

    return saved_jobs


def job_information(url):
    """
    Uses bs4 to grab the information from each job container based on the url.
    :param url: career builder url of any job
    :return: A dictionary containing Job Name, Company Name, Job Location and apply link.
    """
    website = requests.get(url).text
    job_soup = BeautifulSoup(website, 'html.parser')

    # application_type = 'regular'
    job_name = job_soup.select('.dib-m > h1')[0].getText()
    company_name = job_soup.select('.data-details > span:nth-child(1)')[0].getText()
    job_location = job_soup.select('.data-details > span:nth-child(2)')[0].getText()
    # apply_url = job_soup.select('.external-apply-link')[0].get('href', None)
    # company_url = soup.select(".icl-u-lg-mr--sm > a")[0].get("href", None)

    job_data = {'Job Title': job_name, 'Company': company_name, 'Location': job_location, 'Application Url': url}

    return job_data


# Loops through each link in saved_jobs and use the job_information function to add
# the data to a csv file. Counter is to create an id for the items in the csv file.
def start_search(job, location):
    for jobs in grab_jobs(job, location):
        add_to_csv(job_information(jobs))


def csv_to_md(file_to_convert, filename):
    """
    :param file_to_convert: str -> path or filename. Must be csv file
    :param filename: str -> Pass the filename without the extension
    :return: An md file with the csv data converted to an md table.
    """
    with open(f'{filename}.md', 'w+') as file:
        file.write(f'Job Title | Company | Location | Application Url \n'
                   f'------------ | ------------- | ------------ | -----\n')

    with open(file_to_convert, "r")as job_details:
        reader = csv.reader(job_details)
        for idx, row in enumerate(reader):
            if idx >= 0:
                # print(idx, row)
                with open(f'{filename}.md', 'a+') as jobs:
                    jobs.write(f"{row[0]} | {row[1]} | {row[2]} | [Apply]({row[3]})\n")


def remove_duplicate(csv_file):
    """
    Removes the duplicates from a csv file
    :param csv_file: csv file with extension
    :return:
    """
    df = pd.read_csv(csv_file)
    remove_dups_df = df.drop_duplicates(keep="first")
    return remove_dups_df.to_csv(csv_file, index=False)

start_time = datetime.datetime.now()
print("Collecting jobs...")
start_search(job, location)

print("Removing duplicates")
remove_duplicate("panda_job_data.csv")

print("Converting data...")
csv_to_md("panda_job_data.csv", "tech jobs")

print("Job collection completed")
end_time = datetime.datetime.now()
print(f"Time elapsed: {end_time - start_time}")
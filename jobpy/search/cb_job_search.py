from bs4 import BeautifulSoup


import csv
import requests
import datetime


def grab_jobs_links(job_title: str, job_location: str):
    """Return a list of job links

       Parameters
       ----------
       job_title : str
           Desired job title.

       job_location : str
           Desired job location

       Returns
       -------
       saved_jobs : list
            Collection of link from Career Builder equal or similar to the parameters given.:

       """
    web = requests.get(
        f"https://www.careerbuilder.com/jobs?utf8=%E2%9C%93&keywords={job_title}&location={job_location}").text
    soup = BeautifulSoup(web, 'html.parser')

    # Career Builder sign in url. Used later to avoid signing in to grab the data.
    sign_in_url = "https://www.careerbuilder.com/user/sign-in?next="
    job_containers = soup.select('.data-results-content-parent')

    # Empty list used to store the values of the for loop below
    saved_jobs = [ ]

    for idx, jobs in enumerate(job_containers):
        # CB requires the user to be signed in to see jobs. We use the replace method to bypass it.
        saved_jobs.append(f'{job_containers[idx].a.get("href", None).replace(sign_in_url, "")}')

    return saved_jobs


def get_job_information(url):
    """ Uses bs4 to grab the information from each job container based on the url.

    Parameters
    ----------
    url : str
        Career builder url of any job

    Returns
    ------
    job_data : dict
        Contains Job Name, Company Name, Job Location, Description, Skills and apply link.
    """

    website = requests.get(url).text
    job_soup = BeautifulSoup(website, 'html.parser')

    job_name = job_soup.select('h2.h3')[0].getText() 
    company_name = job_soup.select('.data-details > span:nth-child(1)')[0].getText()
    job_location = job_soup.select('.data-details > span:nth-child(2)')[0].getText()

    job_description = job_soup.select('#jdp_description > div.col-2 > div.col.big.col-mobile-full > p')
    job_description_2 = job_soup.select('#jdp_description > div:nth-child(1) > div:nth-child(1)')

    desc = [ ]
    for idx, paragraph in enumerate(job_description):
        desc.append(job_description[idx].text)

    if len(desc) == 0:
        for idx, paragraph in enumerate(job_description_2):
            desc.append(job_description_2[idx].text)

    job_skills = [ ]
    skills_container = job_soup.findAll("div", {"class": "check-bubble"})

    for idx, skill in enumerate(skills_container):
        job_skills.append(skills_container[idx].text)

    job_data = {'Job Title': job_name,
                'Company': company_name,
                'Location': job_location,
                'Description': desc,
                'Skills': job_skills,
                'Application Url': url}

    return job_data


# Loops through each link in saved_jobs and use the job_information function to add
# the data to a csv file. Counter is to create an id for the items in the csv file.
def start_search(job: str, location: str):
    """ Initiate the job search

    Parameters
    ----------
    job: str
        Desired job title ("software engineer")
    location: str
        Desired job location ("Silicon Valley")

    Returns
    -------
    File
        csv file with the name of the job title and position.

    """
    job_info = []
    for jobs in grab_jobs_links(job, location):
        job_info.append(get_job_information(jobs))
    
    return job_info

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    print("Collecting jobs...")
    print(start_search("software engineer", 'Silicon Valley'))

    print("Removing duplicates...")
    # remove_duplicate_rows("software_dev_jobs.csv")

    print("Converting data...")
    # csv_to_md("software_dev_jobs", "tech jobs")

    print("Job collection completed")
    end_time = datetime.datetime.now()
    print(f"Time elapsed: {end_time - start_time}")


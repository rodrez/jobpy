Welcome to jobpy's documentation!
=================================
Jobpy
========

What is Jobpy?
--------------

Jobpy is a library built with Python to pull job posting from all over the internet.
The idea behind is was to analyze the different characteristics of the job posting, like
skills required, experience, etc. It can also be used to apply to the search jobs although
the fetaure has not been released yet.

![GitHub version](https://badge.fury.io/gh/rodrez%2FJobs-and-Skills.svg)
![GitHub issues](https://img.shields.io/github/issues/rodrez/jobpy)
![License MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/pypi/pyversions/jobpy)

Look how easy it is to use:
`
   [In]: from jobpy.search import cb_job_search as cb
   [In]: jobs_in_la = cb.start_search('software developer', 'Los Angeles')
   [In]: print(jobs_la)
   [Out]: 'software_developer_job_los_angeles.csv
`
>>>>

Table of Contents
-----------------

- [Installation](#Installation)
- [Features](#Features)
- [Contributing](#Contributing)
- [FAQ](#FAQ)
- [Support](#Support)



Features
--------

- Easy Job Search
- Great Performance
- Export to CSV or MD Table
- Organized data
- File converter support
- Apply to jobs easily

>>>>

Installation
------------

At the command line::

    pip install jobpy

>>>>

FAQS
----

1. How do we performed the search.

   - I used Scrapy, Beutiful Soup to perform the search.

2. How often does jopby gets updated?

   - I am currently releasing weekly updates.
   - NOTE: I'm currently a full time employee and part time student so I spend the rest ofvmy free time coding to expand my knowledge. Help is always appreciated.

3. Will this become something more?

   - I would like this to become an Open Source website that could help developers like me find their dream job.

>>>>

Contributing
------------

   To get started...

**Step 1**

- **Option 1**
    - 🍴 Fork this repo!
- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/rodrez/Jobs-and-Skills.git`

**Step 2**

- **HACK AWAY!** 🔨🔨🔨

**Step 3**

- 🔃 Create a new pull request using `[https://github.com/rodrez/Jobs-and-Skills/compare/](https://github.com/rodrez/Jobs-and-Skills/compare/)`.

>>>>

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: fabian.rodrez@gmail.com

It's easier to reach me on Twitter @Rodrez_

License
-------

The project is licensed under the MIT license.

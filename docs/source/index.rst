Welcome to Jobpy's documentation!
=================================

Jobpy Overview
*************************************

What is Jobpy?
==============

Jobpy is a library built with Python to pull job posting from all over the internet.
The idea behind is was to analyze the different characteristics of the job posting, like
skills required, experience, etc. It can also be used to apply to the search jobs although
the fetaure has not been released yet.


Look how easy it is to use:

from jobpy.files import converter as con
from jobpy.search import cb_job_search as cb
 
job_data = cb.start_search("python developer", "washington")
for item in job_data:
    con.add_to_csv(item,"py jobs")


Features
========

- Easy Job Search
- Great Performance
- Export to CSV or MD Table
- Organized data
- File converter support
- Apply to jobs easily

>>>>

Installation
============

At the command line::

    pip install jobpy

>>>>

FAQS
====

1. How do we performed the search.

   - I used Scrapy, Beutiful Soup to perform the search.

2. How often does jopby gets updated?

   - I am currently releasing weekly updates.
   - NOTE: I'm currently a full time employee and part time student so I spend the rest ofvmy free time coding to expand my knowledge. Help is always appreciated.

3. Will this become something more?

   - I would like this to become an Open Source website that could help developers like me find their dream job.

>>>>

Contributing
============

   To get started...

- Issue Tracker: ![Issues](github.com/rodrez/jobpy/issues)

- Source Code: ![Source](github.com/rodrez/jobpy)

**Step 1**

- **Option 1**
    - 🍴 Fork this repo!
- **Option 2**
    - 👯 Clone this repo to your local machine using ![https://github.com/rodrez/jobpy.git](https://github.com/rodrez/jobpy.git)

**Step 2**

- **HACK AWAY!** 🔨🔨🔨

**Step 3**

- 🔃 Create a new pull request using ![https://github.com/rodrez/jobpy/compare/](https://github.com/rodrez/jobpy/compare/).

Support
=======

If you are having issues, please let us know.
We have a mailing list located at: fabian.rodrez@gmail.com

It's easier to reach me on Twitter @Rodrez_

License
=======

The project is licensed under the MIT license.

Documentation
=============

.. automodule:: jobpy.search.cb_job_search
    :members:

.. automodule:: jobpy.files.converter
    :members:

.. toctree::
   :maxdepth: 2
   :titlesonly: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

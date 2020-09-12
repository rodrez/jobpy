[![PyPI version](https://badge.fury.io/py/jobpy.svg)](https://badge.fury.io/py/jobpy)
![Issues](https://img.shields.io/github/issues/rodrez/jobpy)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python3.8-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](http://ansicolortags.readthedocs.io/?badge=latest)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/rodrez/jobpy">
    <img src="images/jobpy.png" alt="Logo" width="250px" height="180px">
  </a>
  <h3 align="center">Jobpy</h3>
<br />
  
  <p align="center">
    Welcome to jobpy!
    <br />
    <a href="https://jobpy.readthedocs.io/en/latest/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/rodrez/jobpy/issues">Report Bug</a>
    ·
    <a href="https://github.com/rodrez/jobpy/issues">Request Feature</a>
  </p>
  
  
</p>





Jobpy
========

What is Jobpy?
--------------

Jobpy is a library built with Python to pull job postings from all over the internet.
The idea behind is was to analyze the different characteristics of the job posting, like
skills required, experience, etc. It can also be used to apply to the search jobs although
the fetaure has not been released yet.


Look how easy it is to use:

```
from jobpy.files import converter as con
from jobpy.search import cb_job_search as cb
 
job_data = cb.start_search("python developer", "washington")
for item in job_data:
    con.add_to_csv(item,"py jobs")
```
>>>>

Table of Contents
-----------------

- [Features](#Features)
- [Installation](#Installation)
- [FAQS](#FAQS)
- [Contributing](#Contributing)
- [Support](#Support)
- [Docs](#Documentation)
- [License](#License)

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

At the command line:

    pip install jobpy

>>>>

FAQS
----

1. How do we performed the search.

   - I used Scrapy, BeautifulSoup to perform the search.

2. How often does jopby gets updated?

   - I am currently releasing weekly updates.
   - NOTE: I'm currently a full time employee and part time student so I spend the rest ofvmy free time coding to expand my knowledge. Help is always appreciated.

3. Will this become something more?

   - I would like this to become an Open Source website that could help developers like me find their dream job.

>>>>

Contributing
------------

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

>>>>



<span id="documentation"></span><h1>Documentation<a class="headerlink" href="#module-jobpy.search.cb_job_search" title="Permalink to this headline">¶</a></h1>
- Read the documentation at https://jobpy.readthedocs.io/en/latest/
<dl class="py function">
<dt id="jobpy.search.cb_job_search.get_job_information">
<code class="sig-prename descclassname">jobpy.search.cb_job_search.</code><code class="sig-name descname">get_job_information</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">url</span></em><span class="sig-paren">)</span><a class="headerlink" href="#jobpy.search.cb_job_search.get_job_information" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses bs4 to grab the information from each job container based on the url.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>url</strong> (<em>str</em>) – Career builder url of any job</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>job_data</strong> – Contains Job Name, Company Name, Job Location, Description, Skills and apply link.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>dict</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="jobpy.search.cb_job_search.grab_jobs_links">
<code class="sig-prename descclassname">jobpy.search.cb_job_search.</code><code class="sig-name descname">grab_jobs_links</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">job_title</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">job_location</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span><a class="headerlink" href="#jobpy.search.cb_job_search.grab_jobs_links" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of job links</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>job_title</strong> (<em>str</em>) – Desired job title.</p></li>
<li><p><strong>job_location</strong> (<em>str</em>) – Desired job location</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>saved_jobs</strong> – Collection of link from Career Builder equal or similar to the parameters given.:</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>list</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="jobpy.search.cb_job_search.start_search">
<code class="sig-prename descclassname">jobpy.search.cb_job_search.</code><code class="sig-name descname">start_search</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">job</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span><a class="headerlink" href="#jobpy.search.cb_job_search.start_search" title="Permalink to this definition">¶</a></dt>
<dd><p>Initiate the job search</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>job</strong> (<em>str</em>) – Desired job title (“software engineer”)</p></li>
<li><p><strong>location</strong> (<em>str</em>) – Desired job location (“Silicon Valley”)</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>csv file with the name of the job title and position.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>File</p>
</dd>
</dl>
</dd></dl>

<span class="target" id="module-jobpy.files.converter"></span><dl class="py function">
<dt id="jobpy.files.converter.add_to_csv">
<code class="sig-prename descclassname">jobpy.files.converter.</code><code class="sig-name descname">add_to_csv</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dictionary</span></em>, <em class="sig-param"><span class="n">filename</span></em><span class="sig-paren">)</span><a class="headerlink" href="#jobpy.files.converter.add_to_csv" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses pandas to convert a dictionary to a csv file.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>dictionary</strong> (<em>dict</em>) – Any dictionary</p>
</dd>
</dl>
<dl class="simple">
<dt>filename: str</dt><dd><p>Output filename desired. Does not need the extension.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>csv file based on the dictionary data provided and named after your chosen filename.</p>
</dd>
<dt class="field-even">Return type</dt>
<dd class="field-even"><p>File</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="jobpy.files.converter.csv_to_md">
<code class="sig-prename descclassname">jobpy.files.converter.</code><code class="sig-name descname">csv_to_md</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">file_to_convert</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">filename</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span><a class="headerlink" href="#jobpy.files.converter.csv_to_md" title="Permalink to this definition">¶</a></dt>
<dd><p>Converts csv file to md table</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>file_to_convert</strong> (<em>str</em>) – Path or filename of the file name to convert. It does not require the extension. MUST be a csv file.</p></li>
<li><p><strong>filename</strong> (<em>str</em>) – Output filename desired. Does not need the extension.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p></p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Md file with a table based on the csv data provided and named after your chosen filename.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="jobpy.files.converter.json_to_md_table">
<code class="sig-prename descclassname">jobpy.files.converter.</code><code class="sig-name descname">json_to_md_table</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">file_to_convert</span></em>, <em class="sig-param"><span class="n">filename</span></em>, <em class="sig-param"><span class="n">num_to_convert</span><span class="o">=</span><span class="default_value">- 1</span></em><span class="sig-paren">)</span><a class="headerlink" href="#jobpy.files.converter.json_to_md_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Removes the duplicates from a csv file</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>file_to_convert</strong> (<em>str</em>) – Any json file without the extension. MUST be json file.</p></li>
<li><p><strong>filename</strong> (<em>str</em>) – Desired output name without the extension</p></li>
<li><p><strong>num_to_convert</strong> (<em>int</em><em>, </em><em>optional</em>) – Values are index based. Default value is -1 and converts all the data.
The number represents the amount of rows to convert.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>File</strong> – A file with the given output name and data converted to MD table.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Md</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="jobpy.files.converter.remove_duplicate_rows">
<code class="sig-prename descclassname">jobpy.files.converter.</code><code class="sig-name descname">remove_duplicate_rows</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">csv_file</span></em><span class="sig-paren">)</span><a class="headerlink" href="#jobpy.files.converter.remove_duplicate_rows" title="Permalink to this definition">¶</a></dt>
<dd><p>Removes the duplicates from a csv file</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>csv_file</strong> (<em>str</em>) – Any csv file without the extension</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The same file given with the duplicate rows removed.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>File</p>
</dd>
</dl>
</dd></dl>

>>>>
Support
-------

If you are having issues, please let us know.
We have a mailing list located at: fabian.rodrez@gmail.com

It's easier to reach me on Twitter @Rodrez_

License
-------

The project is licensed under the MIT license.

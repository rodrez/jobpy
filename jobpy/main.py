###  Main Functionality - Export CSV file names py jobs with 25 jobs

from files import converter as con
from search import cb_job_search as cb
from util import states
 
def main(job, location, filename):

    for state in states.get_us_states():
        job_data = cb.start_search(job, location)

        for item in job_data:
            con.add_to_csv(item, filename)

    con.remove_duplicate_rows(filename)

# main("data science", "test")



def html_generator(filename, jobs):
     
    job_info = ""
    index = ["""  <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

    <title>Jobpy Job Board</title>
  </head>
  <body>
    <!-- Image and text -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">
    <img src="/docs/4.0/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">
    Jopby Job Board
  </a>
</nav>
<div style="height: 50px;"></div>
    <div style="margin-top: 25;">
    <div class="row">
      <div style="height: 24px;"></div>
      <!-- Block to add info --> """,
      
      """ 
      <!-- Block ends -->
      
      
    </div>
  </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </body>
</html>
      """]

    count = 0
    for job in jobs:

        job_info = f"""
        <div class="col-sm-6 mt-8">
            <div class="card text-white bg-secondary mb-3" style="max-width: 25rem;">
            <div class="card-header">{job["Job Title"]}</div>
            <div class="card-body">
                <h5 class="card-title">{job["Company"]}</h5>
                <p class="card-text">{job["Location"]} </p>
                <p class="card-text">{job["Description"][0][:200].strip()}.</p>
                <a class="btn btn-primary" href="{job["Application Url"]}" role="button">Read More</a>            </div>
            </div>
        </div>

        
        """
        index.insert(1, job_info)
        count += 1

      
        if count == 5:
              break
    with open(f"{filename}.html", "w") as f:
        f.write("".join(index))
      

    # return job_info
html_generator("test")
###  Main Functionality - Export CSV file names py jobs with 25 jobs

from files import converter as con
from search import cb_job_search as cb
from util import states
 


for state in states.get_us_states():
    job_data = cb.start_search("data science", state)

    for item in job_data:
        con.add_to_csv(item, "test")

con.remove_duplicate_rows("test")


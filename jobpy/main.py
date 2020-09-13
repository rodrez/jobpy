###  Main Functionality - Export CSV file names py jobs with 25 jobs

from files import converter as con
from search import cb_job_search as cb
from util import states
 


# # for state in states.get_us_states()[10:]:
# #     job_data = cb.start_search("python developer", state)

# #     for item in job_data:
# #         con.add_to_csv(item, "py jobs")

# con.remove_duplicate_rows("py jobs")

# job_name = job_soup.select('h2.h3')[0].getText() 
# IndexError: list index out of range

job_name = []

for i in range(5):
    try:
        job_name.append(job_name[i] / i)
    except:
        print(f"{i}  failed to do math")
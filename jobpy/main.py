from files import converter as con
from search import cb_job_search as cb

job_data = cb.start_search("python developer", "washington")

for item in job_data:
    con.add_to_csv(item,"py jobs")

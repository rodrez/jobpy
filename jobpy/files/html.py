from files import converter as con
from search import cb_job_search as cb
from util import states

def html_generator():
 
    jobs = cb.start_search("data science", "california")
    job_info = ""

    for job in jobs[0]:
        

        job_info = f"""
        <div class="col-sm-6 mt-8">
            <div class="card text-white bg-primary mb-3" style="max-width: 25rem;">
            <div class="card-header">{job["Title"]}</div>
            <div class="card-body">
                <h5 class="card-title">{job["Company"]}</h5>
                <p class="card-text">{job["Location"]} </p>
                <p class="card-text">{job["Description"][:50]}.</p>
                <a class="btn btn-primary" href="{job["Url"]}" role="button">Read More</a>            </div>
            </div>
        </div>
        
        """
print(html_generator())
c_list = ['Apple', 'Microsoft', 'Samsung Electronics', 'Alphabet', 'AT&T', 'Amazon',' Verizon Communications',
	'Walt Disney', 'Facebook', 'Alibaba', 'Intel', 'Softbank', 'IBM','Cisco Systems', 'Oracle',
	'SAP', 'Dell Technologies', 'Broadcom', 'Micron Technology', 'Qualcomm', 'PayPal', 'HP',
	'Automatic Data Processing', 'Booking Holdings', 'Texas Instruments', 'Netflix',
	'Salesforce', 'Adobe', 'VMware', 'Cognizant', 'NVIDIA', 'eBay', 'Fidelity National Information',
    'DISH Network', 'Activision', 'Blizzard', 'DXC Technology', 'Fiserv', 'Hewlett Packard Enterprise']

try:
	from googlesearch import search
except ImportError:
	print('No module named "google"')


def get_company_job_url(company_list):
	""" Uses a list of company names to get their career url.

	    Parameters
	    ----------
	    company_list : list
	        A list of companies

	    Returns
	    ------
	    company_urls : list
	        Contains the career urls for each company pass on the list
	    """
	for i, company in enumerate(company_list):
		for _ in search(f"{company} careers", tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
			c_url = _
			print(c_url)
		
get_company_job_url(c_list)

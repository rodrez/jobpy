c_list = ['Apple', 'Microsoft', 'Samsung Electronics', 'Alphabet', 'AT&T', 'Amazon',' Verizon Communications',
	'Walt Disney', 'Facebook', 'Alibaba', 'Intel', 'Softbank', 'IBM','Cisco Systems', 'Oracle',
	'SAP', 'Dell Technologies', 'Broadcom', 'Micron Technology', 'Qualcomm', 'PayPal', 'HP',
	'Automatic Data Processing', 'Booking Holdings', 'Texas Instruments', 'Netflix',
	'Salesforce.com', 'Adobe', 'VMware', 'Cognizant', 'NVIDIA', 'eBay', 'Corning', 'Fidelity National Information',
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
	company_urls = []

	for idx, company in enumerate(c_list):
		query = f'{c_list[idx]} careers'

		for i in search(query, tld="com", num=1, stop=1, pause=.25):
			company_urls.append(i)

	return company_urls

for url in get_company_job_url(c_list):
	print(url)

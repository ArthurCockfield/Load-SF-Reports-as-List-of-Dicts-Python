import requests
import pandas as pd
from simple_salesforce import SalesforceAPI
from io import StringIO
username = 'enter_here'
password = 'enter_here'
security_token = 'enter_here'
sf = SalesforceAPI(username, password, security_token)

report_id = 'enter_here'

def Load_SF_Reports(sf, report_id, export_params = '?isdtp=p1&export=1&enc=UTF-8&xf=csv') :
    """ ARG: SF_org (default OneLocal), report ID from Salesforce, export parameters
        Returns: list of dictionaries of the report
    """
    

    sf_report_url = sf_org + report_id + export_params
    print(sf_report_url)
    response = requests.get(sf_report_url, headers=sf.headers, cookies={'sid': sf.session_id})
    new_report = response.content.decode('utf-8')
    report_df = pd.read_csv(StringIO(new_report))
    datadict = report_df.to_dict('records')
    
    return datadict



data_sample =  Load_SF_Reports(sf, report_id)
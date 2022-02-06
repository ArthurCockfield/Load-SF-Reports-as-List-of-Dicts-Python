# Load-SF-Reports-As-List-of-Dicts-Python
**Summary**

Loads a Salesforce Report as a list of dictionaries in Python. The program takes any Salesforce report and loads the data as a list of dictionaries, where the key is the field and the value is the value in the row. Think of each dictionary in the the list as a single row of the original report.
 
 
 **Windows Installation**
 You will need to install the following packages:
 - Pandas
 - Simple_Salesforce

If you are using Anaconda on Windows, go to the Anaconda prompt on your computer and type in "pip install Pandas", and press enter to install Pandas. Do the same with Simple Salesforce.

**How to use with your own packages**

The easiest way to use this package is to copy the Load_SF_Reports file into whatever program you are running. Then insert the following code into any .py file where you want to use it:
From Load_SF_Reports import Load_SF_Reports

**Instructions to use**

You will need to change lines 5-10 in the Load_SF_Reports.py file so that so that you can log into Salesforce. 

Report_id is the report ID Salesforce specifies (it looks like this format "00O3u000007A1d2GHK" in the report url").

SF_Org is your Salesforce org url.

The security token is attached to your username and password in Salesforce. It's given to you whenever you change your password in Salesforce.

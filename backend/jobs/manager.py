import json
import datetime as dt
from .model import Job

def is_company_name_valid(company_name):
    '''
    args: company_name:str
    checks if company_name is empty string. if yes, returns false
    we do not check if company_name is not of type String as this validation will be done by API
    returns: Bool
    '''
    if company_name=="":
        return False
    return True

def generate_datetime():
    '''
    returns current datetime
    used to populate job datetime parameter if empty
    '''
    return dt.datetime.now()

def create_job(job_item):
    print(job_item)
    '''
    paramters: job_item = {
            "id": item,
            "company": "",
            "job_title": "sample job title",
            "location": "Bangalore",
        }
    received a job JSON from API, enforces business rules by checking for empty company name, 
        '''
    if not is_company_name_valid(job_item["company"]):
        return {"message":"Company name cannot be invalid"}
    timestamp = generate_datetime()
    status = "Applied"
    job = Job(
        id=job_item["id"],
        company=job_item["company"],
        job_title=job_item["job_title"],
        date_applied=timestamp,
        location=job_item["location"],
        status=status,
        notes=""
    )
    return job
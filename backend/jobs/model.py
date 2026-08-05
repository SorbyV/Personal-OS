import datetime as dt
class Job:
    id: int
    created_at: str
    updated_at: str
    company: str
    job_title: str
    date_applied: dt.datetime
    location: str
    status: str
    notes: str
    def __init__(self, id, company, job_title, date_applied, location, status, notes) -> None:
        self.id = id
        self.company = company
        self.job_title = job_title
        self.date_applied = date_applied
        self.location = location
        self.status = status
        self.notes = notes
        self.created_at = ""
        self.updated_at = ""

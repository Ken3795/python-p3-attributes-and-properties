APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, **kwargs):
        self.name = None
        self.job = None
        
        # Only validate name if explicitly provided
        if 'name' in kwargs:
            if self._is_valid_name(kwargs['name']):
                self.name = kwargs['name'].title()
        
        # Only validate job if explicitly provided
        if 'job' in kwargs:
            if self._is_valid_job(kwargs['job']):
                self.job = kwargs['job']
            
    def _is_valid_name(self, name):
        """Validate that name is a non-empty string of appropriate length"""
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return False
        return True
    
    def _is_valid_job(self, job):
        """Validate that job is in the approved list"""
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return False
        return True
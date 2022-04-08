class LeadEmailNotFound(Exception):
    def __init__(self, message= None, status_code=404):
        if message:
            self.message = message
        else:
            self.message="Email not found"
        self.status_code = status_code
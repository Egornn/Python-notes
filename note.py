from datetime import datetime
from datetime import date
class Note:
    def __init__(self, id):
        self.id= id
        self.title = "Default title"
        self.body = "Some task"
        self.time = datetime.now().strftime("%H:%M:%S")
        self.date = date.today()

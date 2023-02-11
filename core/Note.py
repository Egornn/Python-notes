from datetime import datetime
from datetime import date
import json
class Note:
    def __init__(self, id):
        self.id= id
        self.title = "Default title"
        self.body = "Some task"
        self.time = datetime.now().strftime("%H:%M:%S")
        self.date = date.today()
    def __str__(self) -> str:
        return f"{self.id}: {self.title}"
    
    def __repr__(self) -> str:
        keys = ["ID", "Title", 'Text', 'Time of creation', 'Creation date']
        values = [self.id, self.title, self.body, self.time, self.date]
        return json.dumps(dict(zip(keys, values)))
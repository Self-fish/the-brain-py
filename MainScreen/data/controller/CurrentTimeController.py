from datetime import datetime
from pytz import timezone


def get_current_hour():
    print("Get Hour")
    return "Test hour"
    #return datetime.now(timezone('Europe/Madrid')).strftime("%H:%M  %d %b %Y")

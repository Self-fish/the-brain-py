from datetime import datetime, timezone


def get_current_hour():
    return datetime.now(timezone('Europe/Madrid')).strftime("%H:%M  %d %b %Y")
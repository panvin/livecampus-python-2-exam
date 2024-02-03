from datetime import datetime, timezone, timedelta
import random
import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def isDateBeforeNow(date):
    return date < (datetime.now(timezone.utc) - timedelta(minutes=5) )

def isFirstDateOlderThanSecond(firstDate, secondDate):
    return firstDate < secondDate
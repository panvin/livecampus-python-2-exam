from datetime import datetime, timezone
import random
import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def isDateBeforeNow(date):
    return date < date
def isFirstDateOlderThanSecond(firstDate, secondDate):
    return firstDate < secondDate
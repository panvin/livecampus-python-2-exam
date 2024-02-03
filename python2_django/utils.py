from datetime import datetime, timezone, timedelta
import locale
import random
import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def isDateBeforeNow(date):
    return date < (datetime.now(timezone.utc) - timedelta(minutes=5) )

def isFirstDateOlderThanSecond(firstDate, secondDate):
    return firstDate < secondDate

def getFormattedDateForHomePage():
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    date = datetime.now(timezone.utc)
    formattedDate = date.strftime('%A %d %B')
    return formattedDate
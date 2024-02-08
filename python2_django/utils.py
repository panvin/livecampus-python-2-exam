from datetime import datetime, timezone, timedelta
from django.conf import settings
import locale
import random
import string
import jwt

def generateRandomString(length: int) -> str:
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

def generateJwt(userId, username, sessionId):
    payload = {
        'userId': userId,
        'username': username,
        'sessionId' : sessionId
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
    return token
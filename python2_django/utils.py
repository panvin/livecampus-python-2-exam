from datetime import datetime, timezone, timedelta
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

def getPercentageAsStr(value, total):
  percentage = 100 * float(value)/float(total)
  return f"{percentage} %"

def generateJwt(username, sessionId):
    payload = {
        'username': username,
        'sessionId' : sessionId
    }
    token = jwt.encode(payload, "test_12345", algorithm='HS256')
    return token
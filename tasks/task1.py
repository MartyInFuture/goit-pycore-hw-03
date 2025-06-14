from datetime import datetime

BASE_FORMAT = '%Y-%m-%d'

def get_days_from_today(date, format = BASE_FORMAT):
  if is_valid_date_format(date, format): 
    return (datetime.today().date() - get_date(date, format)).days
  else:
    return f"You've provided wrong date, or date format"


def is_valid_date_format(date, format = BASE_FORMAT):
  try: 
    get_date(date, format)
    return True
  except ValueError:
    return False
  
def get_date(date, format = BASE_FORMAT):
  return datetime.strptime(date, format).date()


print(get_days_from_today('2025-06-110'))
print(get_days_from_today('2025-06-10'))
print(get_days_from_today('2025-06-20'))
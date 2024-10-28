from datetime import datetime 

def get_days_from_today(date): 
    try: 
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - date_obj
        return delta.days
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'"
    
print(get_days_from_today("2021-10-09"))
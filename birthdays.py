from datetime import datetime, timedelta

def users(path):
    """Зчитуєм файл із іменами та датами, та переносимо все в словник"""
    current_datetime = datetime.now()
    with open(path, 'r', encoding='UTF-8') as files:
        rezult = []
        for line_file in files:
            rezult_line = {}
            line_rezult = line_file.split(',')
            rezult_line["name"] = line_rezult[0]
            birthdays_date = line_rezult[1].removesuffix('\n')
            birthdays_date = birthdays_date.split('-')
            birthdays_date = str(current_datetime.year) + '-' + birthdays_date[1] + '-' + birthdays_date[2]
            rezult_line["birthday"] = birthdays_date
            rezult.append(rezult_line)
    return rezult
          
def get_birthdays_per_week(n=7):
    """Обробляємо словник відносно поточної дати на тиждень вперед і групуємо"""
    i = 0
    rezult = {'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday': ''} 
    while i < 7:
        current_datetime = (datetime.now() +  timedelta(days=i)).date()
        for data_list in users(patch):
            if current_datetime == (datetime.strptime(str(data_list["birthday"]), '%Y-%m-%d')).date():
                if current_datetime.weekday() == 0:
                    rezult['Monday'] += data_list["name"] + ", "
                elif current_datetime.weekday() == 1:
                    rezult['Tuesday'] += data_list["name"] + ", "
                elif current_datetime.weekday() == 2:
                    rezult['Wednesday'] += data_list["name"] + ", "
                elif current_datetime.weekday() == 3:
                    rezult['Thursday'] += data_list["name"] + ", "
                elif current_datetime.weekday() == 4:
                    rezult['Friday'] += data_list["name"] + ", "
                else: 
                    if (current_datetime.weekday() == 5 or current_datetime.weekday() == 4) and (datetime.now().weekday() != 0):
                     rezult['Monday'] += data_list["name"] + ", "        
        i += 1
    for week, name in rezult.items():
        if rezult[week] != '':
            print(f"{week}: {name.removesuffix(', ')}")
patch = 'C:/Work Python/home-work-8/birthdays/users.txt'

get_birthdays_per_week()

seventh_day_2022 = datetime(year=2022, month=12, day=14)

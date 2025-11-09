import datetime, bday_messages
today = datetime.date.today()
next_birthday = datetime.date(2026, 8, 23)

if today == next_birthday:
    print(bday_messages.random_message)
else:
    daysaway = next_birthday - today
    print(f'My next Birthday is {daysaway} days away!' )


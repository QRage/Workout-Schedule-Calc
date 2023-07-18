import datetime
import calendar


def determine_workout_days(year, month, planning_day):
    days_in_month = calendar.monthrange(year, month)[1]
    workout_days = []

    for day in range(1, days_in_month + 1):
        if (day - planning_day) % 4 < 2:
            if datetime.datetime(year, month, day).weekday() in [0, 2, 4]:
                workout_days.append(f"День {day} - вільний для тренування")
            else:
                workout_days.append(f"День {day} - день відпочинку")
        else:
            workout_days.append(f"День {day} - на роботі")

    return workout_days


current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

planning_day_input = int(input("Введіть день для планування: "))

workout_days = determine_workout_days(2023, 7, planning_day_input)

print("Розклад тренувань:")
for day in workout_days:
    print(day)

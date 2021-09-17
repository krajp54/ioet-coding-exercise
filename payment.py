import datetime


def readFile(path):
    try:
        with open(path) as file:
            lines = file.readlines()

            employees = {}

            for line in lines:
                line = line.rstrip('\n')
                aux = line.split('=')

                employees[aux[0]] = aux[1].split(',')

            return employees
    except FileNotFoundError:
        print('File not found')
        exit(1)


def processHours(hours):

    aux = hours.split('-')

    beggin_hour = aux[0].split(':')[0]
    beggin_minute = aux[0].split(':')[1]

    end_hour = aux[1].split(':')[0]
    end_minute = aux[1].split(':')[1]

    beggin = datetime.datetime(100, 1, 1, int(
        beggin_hour), int(beggin_minute), 0)
    end = datetime.datetime(100, 1, 1, int(end_hour), int(end_minute), 0)

    return beggin, end


def processPayment(beggin, end, weekend):
    first_schedule = datetime.datetime(100, 1, 1, 0, 1, 0)
    second_schedule = datetime.datetime(100, 1, 1, 9, 1, 0)
    third_schedule = datetime.datetime(100, 1, 1, 18, 1, 0)

    if first_schedule <= beggin < second_schedule:

        if first_schedule < end < second_schedule:
            hours = (end - beggin).seconds // 3600

            if weekend:
                return (30 * hours)
            else:
                return (25 * hours)

        elif second_schedule <= end < third_schedule:
            first_hours = (second_schedule - beggin).seconds // 3600
            second_hours = (end - second_schedule).seconds // 3600

            if weekend:
                return ((30 * first_hours) + (20 * second_hours))
            else:
                return ((25 * first_hours) + (15 * second_hours))

        else:
            first_hours = (second_schedule - beggin).seconds // 3600
            second_hours = (third_schedule - second_schedule).seconds // 3600
            third_hours = (end - third_schedule).seconds // 3600

            if weekend:
                return ((30 * first_hours) + (20 * second_hours) +
                        (25 * third_hours))
            else:
                return ((25 * first_hours) + (15 * second_hours) +
                        (20 * third_hours))

    elif second_schedule <= beggin < third_schedule:

        if second_schedule < end < third_schedule:
            hours = (end - beggin).seconds // 3600

            if weekend:
                return (20 * hours)
            else:
                return (15 * hours)
        else:
            first_hours = (third_schedule - beggin).seconds // 3600
            second_hours = (end - third_schedule).seconds // 3600

            if weekend:
                return (20 * first_hours) + (25 * second_hours)
            else:
                return (15 * first_hours) + (20 * second_hours)

    else:
        hours = (end - beggin).seconds // 3600

        if weekend:
            return (25 * hours)
        else:
            return (20 * hours)


def processDay(day, hours):
    beggin, end = processHours(hours)

    dayCases = {
        'MO': False,
        'TU': False,
        'WE': False,
        'TH': False,
        'FR': False,
        'SA': True,
        'SU': True
    }

    return processPayment(beggin, end, dayCases.get(
        day, lambda: print("Invalid day")))


def processSchedules(schedules):
    payment = 0

    for schedule in schedules:
        day = schedule[:2]
        hours = schedule[2:]

        payment += processDay(day, hours)

    return payment


if __name__ == '__main__':
    employees = readFile('./employees.txt')

    for employee, schedules in employees.items():
        payment = processSchedules(schedules)
        print('The amount to pay', employee, 'is:', payment, 'USD')

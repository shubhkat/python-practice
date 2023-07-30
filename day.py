import argparse

# Weekdays
weekdays = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

# Find day for the given date
def find_day(date: int, starting_day: str) -> str:
    """ This function will return the day of the given date according to the starting day of a month

    Args:
        date (int): date
        starting_day (str): starting day of a month

    Raises:
        Exception: Unable to determine the day for given date if input is invalid

    Returns:
        str: day of the given date
    """
    if 1 <= date <= 31 and starting_day in weekdays:
        starting_day_index = weekdays.get(starting_day)
        day_index = (starting_day_index + date - 1) % 7
        return list(weekdays.keys())[day_index]
    else:
        raise Exception("Unable to determine the day for given date")

# Input arguments passed
def main():
    """ This function is main function which is responsible for parsing arguments

    Returns:
        date (int): date
        starting_day (str): starting day of a month
    """
    parser = argparse.ArgumentParser(description = "Input 2 arguments as follows:\n\tdate - Date, day - Starting day of that month")
    parser.add_argument("--date", type = int, default = 0, help = "Date")
    parser.add_argument("--day", type = str, default = None, help = "Starting day of that month")
    args = parser.parse_args()
    return args.date, args.day

# Main entry point for the program
if __name__ == '__main__':
    """
    This is the main entry point
    """
    date, day = main()
    day_of_date = find_day(date, day.casefold())
    print(f"Day for date '{date}' is '{day_of_date} with regards to given input arguments")

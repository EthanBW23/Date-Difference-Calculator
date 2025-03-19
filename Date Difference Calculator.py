class DateDifferenceCalculator:

    @classmethod
    def __parseDateTime(self, dateString): # Method to parse the date times inputted by the user (removes '/' and ':')
        # The double underscore makes this method private, so only methods inside the class can use it
        try: # The program will attempt to do all that's indented in the try
            date, time = dateString.split() # Splits the inputted date time into two separate strings, date and time
            day, month, year = map(int, date.split('/')) # Splits the date string into it's respective parts: day, month, year
            hour, minute, second = map(int, time.split(':')) # Splits the time string into it's respective parts: hour, minutes, seconds

            # Validates that all the values inputted are in the correct format
            if not (1 <= month <= 12): # Checks if month is between 1 and 12
                raise ValueError("Invalid month.")
            if not (1 <= day <= 31): # Checks if day is between 1 and 31
                raise ValueError("Invalid day.")
            if not (0 <= hour <= 23): # Checks if hour is between 0 and 23
                raise ValueError("Invalid hour.")
            if not (0 <= minute <= 59): # Checks if minute is between 0 and 59
                raise ValueError("Invalid minute.")
            if not (0 <= second <= 59): # Checks if second is between 0 and 59
                raise ValueError("Invalid second.")
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30: # Checks if the inputted month is a 30 day month and then verifies that the day inputted is also less than 31
                raise ValueError("Invalid day for the month.")
            if month == 2: # If the month selected if February
                isLeap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) # Calculation to check if the year inputted is a leap year
                if day > (29 if isLeap else 28): # If the year is a leap year, checks if day is greater than 29, if not a leap year it checks if it's greater than 28 days
                    raise ValueError("Invalid day for February.")
            # If any of these checks return false then a specific error message is returned
            return day, month, year, hour, minute, second
            # Returns all the values back through the method
        except Exception: # If the code in the try fails, then the error is caught by the program instead of crashing it
            raise ValueError("Invalid date format. Use DD/MM/YYYY HH:MM:SS.") # Returns the error that occurred back to the user, notifying them of the issue (they didn't input the data correctly)

    @classmethod
    def __daysInMonth(self, month, year): # Method that returns the specific number of days in a given month for a specific year
        # The double underscore makes this method private, so only methods inside the class can use it
        daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # An array of each number of days in a month in chronological order
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):  # If the specific year is a leap year...
            return 29 # Return the number of days as 29 not 28 for February
        return daysInMonths[month - 1] # Returns the number of days in that specific month

    @classmethod
    def __calculateExactDifference(self, dateTime1, dateTime2): # Method that calculates the exact difference between two date times
        # The double underscore makes this method private, so only methods inside the class can use it
        day1, month1, year1, hour1, minute1, second1 = dateTime1
        day2, month2, year2, hour2, minute2, second2 = dateTime2
        # Extrapolates each dateTime for their specific values

        # Ensures dateTime1 <= dateTime2 so the calculation isn't negative (swaps their values if necessary)
        if (year1, month1, day1, hour1, minute1, second1) > (year2, month2, day2, hour2, minute2, second2):
            dateTime1, dateTime2 = dateTime2, dateTime1
            day1, month1, year1, hour1, minute1, second1 = dateTime1
            day2, month2, year2, hour2, minute2, second2 = dateTime2
            # Updates the values from the start of the method

        # Calculate differences in each unit
        seconds = second2 - second1 # Calculates second difference
        if seconds < 0: # If the difference is negative...
            seconds += 60 # Add 60 to the second difference
            minute2 -= 1 # Take away 1 from the second minutes value
            # This ensures the difference remains positive and accurate for the next calculation

        minutes = minute2 - minute1 # Calculates minute difference
        if minutes < 0: # If the difference is negative...
            minutes += 60 # Add 60 to the minute difference
            hour2 -= 1 # Take away 1 from the second hour value

        hours = hour2 - hour1 # Calculates hour difference
        if hours < 0: # If the difference is negative...
            hours += 24 # Add 24 to the hour difference
            day2 -= 1 # Take away 1 from the second days value

        days = day2 - day1 # Calculates day difference
        if days < 0: # If the difference is negative...
            month2 -= 1 # Take away 1 from the second month value
            if month2 < 1: # If the second month value is now less than 0...
                month2 = 12 # Change the second month value to 12
                year2 -= 1 # Take away 1 from the second year value
            days += self.__daysInMonth(month2, year2) # Adds the number of days in the specific month to the day difference value

        months = month2 - month1 # Calculates month difference
        if months < 0: # If the difference is negative...
            months += 12 # Add 12 to the month difference
            year2 -= 1 # Take away 1 from the second year value

        years = year2 - year1 # Calculates year difference

        return years, months, days, hours, minutes, seconds
        # Returns the calculated differences

    @classmethod # Means the method can be used outside the class
    def run(self): # Main method
        print("Exact Date Difference Calculator")
        print("Enter date times in the format DD/MM/YYYY HH:MM:SS")

        while True: # loops until a full calculation has been made
            try:
                # Asks for date times from user
                dateTime1 = self.__parseDateTime(input("Enter the first date time: "))
                dateTime2 = self.__parseDateTime(input("Enter the second date time: "))
                break # breaks out the while loop
            except ValueError as e: # If an error occurs...
                print(f"Error: {e}. Please try again.") # Returns the error message to the user

        years, months, days, hours, minutes, seconds = self.__calculateExactDifference(dateTime1, dateTime2) # Calculates the difference between the two date times
        print("\nExact Difference:")
        print(f"{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.") # Returns the difference to the user

DateDifferenceCalculator.run() # Starts the program

# Reference: W3Schools (2024). Python Try Except. [online] www.w3schools.com. Available at: https://www.w3schools.com/python/python_try_except.asp.
# Reference: W3Schools (2024). Python - String Methods. [online] www.w3schools.com. Available at: https://www.w3schools.com/python/python_strings_methods.asp.
# Reference: W3Schools (2024). Python Classes and Objects. [online] www.w3schools.com. Available at: https://www.w3schools.com/python/python_classes.asp.
# Reference: GeeksforGeeks (2024). Class Method vs Static Method vs Instance Method in Python. [online] www.geeksforgeeks.org. Available at: https://www.geeksforgeeks.org/class-method-vs-static-method-vs-instance-method-in-python/.
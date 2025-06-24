def add_time(start, duration, weekday=None):
    """
    Calculates the new time after adding a duration to a starting time.

    Parameters:
        start (str): A start time in 12-hour format (e.g., '3:00 PM')
        duration (str): A time duration in hours and minutes (e.g., '3:10')
        weekday (str, optional): Day of the week (e.g., 'Monday'); case-insensitive

    Returns:
        str: The resulting time in 12-hour format, possibly with day information
    """

    # ── Meridiem Explanation ─────────────────────────────────────────────
    # "Meridiem" is from Latin:
    # - AM = ante meridiem ("before midday")
    # - PM = post meridiem ("after midday")
    # ─────────────────────────────────────────────────────────────────────

    # List of week days for optional day tracking
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse starting time and meridiem (AM/PM)
    start_time, meridiem = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert 12-hour format to 24-hour format for easier arithmetic
    if meridiem == "PM" and start_hour != 12:
        start_hour += 12
    elif meridiem == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate total minutes and handle any overflow into hours
    final_minute = start_minute + duration_minute
    extra_hour = final_minute // 60
    final_minute %= 60

    # Calculate total hours and determine how many days later
    final_hour = start_hour + duration_hour + extra_hour
    days_later = final_hour // 24
    final_hour %= 24

    # Convert back to 12-hour format and determine new meridiem
    if final_hour == 0:
        hour_12 = 12
        new_meridiem = "AM"
    elif final_hour < 12:
        hour_12 = final_hour
        new_meridiem = "AM"
    elif final_hour == 12:
        hour_12 = 12
        new_meridiem = "PM"
    else:
        hour_12 = final_hour - 12
        new_meridiem = "PM"

    # Format the basic time string (e.g., "3:03 PM")
    final_time = f"{hour_12}:{final_minute:02d} {new_meridiem}"

    # If weekday provided, calculate the new day after adding duration
    if weekday:
        start_index = days_of_week.index(weekday.capitalize())
        end_index = (start_index + days_later) % 7
        final_time += f", {days_of_week[end_index]}"

    # Append (next day) or (n days later) if needed
    if days_later == 1:
        final_time += " (next day)"
    elif days_later > 1:
        final_time += f" ({days_later} days later)"

    return final_time

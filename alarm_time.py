def calculate_alarm_time():
    # Prompt user for current time in HH:MM format
    current_time_str = input("Enter the current time (in HH:MM format): ")

    # Extract the hour value from the string
    current_time = int(current_time_str[:2])

    # Get the wait time
    wait_time = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the alarm time
    alarm_time = (current_time + wait_time) % 24

    # Print the alarm time
    print(f"The alarm will go off at {alarm_time:02d}:00")

# Call the function
calculate_alarm_time()

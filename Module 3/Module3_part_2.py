def main():
    # Get current time and wait time from user
    current_time = int(input("Enter the current time in hours (24 hour time format: 0-23 hours): "))
    wait_time = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate alarm time based on a 24-hour clock
    alarm_time = (current_time + wait_time) % 24

    # Display result
    print(f"The alarm will go off at: {alarm_time}:00 hours")

if __name__ == "__main__":
    main()

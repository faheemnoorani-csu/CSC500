def calculate_rainfall():
    years = int(input("Enter the number of years to enter rain data for: "))
    total_months = years * 12
    total_rainfall = 0

    # Loop through each year and month to collect rainfall data
    for year in range(1, years + 1):
        print(f"Year {year}:")
        for month in range(1, 13):
            monthly_rainfall = float(input(f"  Enter rainfall for month {month} (in inches): "))
            total_rainfall += monthly_rainfall

    # Calculate average monthly rainfall
    average_rainfall = total_rainfall / total_months

    # Display results
    print(f"\nTotal months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall for entire period: {average_rainfall:.2f} inches")

if __name__ == "__main__":
    calculate_rainfall()

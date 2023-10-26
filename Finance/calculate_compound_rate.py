
    def calculate_annual_interest(principal_per_year, total_value, years):
        # Initialize a guess for the annual interest rate
        annual_interest_rate = 0.05  # Start with a 5% annual interest rate

        # Define the number of times interest is compounded per year (usually 1 for annual)
        compounding_frequency = 1

        # Define a tolerance level for the difference between total_value and the target value (150万)
        tolerance = 1

        while True:
            # Calculate the future value using the current guess for annual interest rate
            future_value = 0
            for year in range(years):
                future_value += principal_per_year * (1 + annual_interest_rate / compounding_frequency) ** (compounding_frequency * year)

            # Check if the future value is within the tolerance of the target value
            if abs(future_value - total_value) < tolerance:
                break

            # Adjust the guess for annual interest rate based on the difference between future and target values
            if future_value < total_value:
                annual_interest_rate += 0.001  # Increase the guess by 0.1%
            else:
                annual_interest_rate -= 0.001  # Decrease the guess by 0.1%

        return annual_interest_rate

    # Input values
    principal_per_year = 1.5  # 1.5万，每年定期投入
    total_value = 150  # 150万
    years = 30

    # Calculate the annual interest rate
    annual_interest_rate = calculate_annual_interest(principal_per_year, total_value, years)

    # Display the result
    print(f"每年的复利年利率为: {annual_interest_rate * 100:.2f}%")

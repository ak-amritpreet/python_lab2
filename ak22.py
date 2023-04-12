def float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Error: Enter a positive value.")


def organism_data():
   # Function for recording daily data of organisms and species
    Starting_count = float_input("Enter the initial number of organisms / species: ")
    Daily_Percentage_Increase = float_input("Enter the average daily percentage increase (in decimal form, e.g. 0.1 for 10%): ")
    num_days = int(float_input("Enter the number of days' worth of data to be printed: "))

    counts = [Starting_count]  # list for storing daily count
    for i in range(1, num_days):
        Count = counts[-1] + counts[-1] * Daily_Percentage_Increase  
        counts.append(Count) 
        print(f"Day {i+1:02d}: Count =", Count)

# calling fxn
organism_data()
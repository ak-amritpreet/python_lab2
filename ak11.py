def calculatingyearlyrainfall():
    
    Num_Years = int(input("Enter the number of years -  "))

    YearlyRainfall = []
    Avg_MonthlyRainfall = []

    
    for i in range(Num_Years):
        YearlyRainfall.append([])
        TotalRainfall = 0
        for j in range(12):
            Rainfall = float(input(f"Enter rainfall for month {j+1} of year {i+1} (in centimeters) - "))
            YearlyRainfall[i].append(Rainfall)
            TotalRainfall += Rainfall
        Avg_MonthlyRainfall.append(TotalRainfall / 12)

   
    print("\nYearly rainfall and average monthly rainfall:")
    for i in range(Num_Years):
        print(f"Year {i+1}: Total Rainfall = {sum(YearlyRainfall[i])} cm, Average Monthly Rainfall = {Avg_MonthlyRainfall[i]} cm")

calculatingyearlyrainfall()
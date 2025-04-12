import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel(r"C:\Users\Ayush Punia\OneDrive\Documents\newdatasetpy.xlsx")

# Convert date to datetime and set as index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)


# Objective 1: Analyze the overall vaccination progress over time



# Plot total vaccinations over time
plt.figure(figsize=(12,6))
df['total_vaccinations'].plot(title='Total COVID-19 Vaccinations in India Over Time')
plt.ylabel('Total Vaccinations')
plt.xlabel('Date')
plt.grid(True)
plt.show()

# Plot daily vaccinations
plt.figure(figsize=(12,6))
df['daily_vaccinations'].plot(title='Daily COVID-19 Vaccinations in India')
plt.ylabel('Daily Vaccinations')
plt.xlabel('Date')
plt.grid(True)
plt.show()

# Print key statistics
print("Vaccination Progress Statistics:")
print(f"First vaccination date: {df.index.min()}")
print(f"Last vaccination date: {df.index.max()}")
print(f"Total vaccinations: {df['total_vaccinations'].max():,}")
print(f"Highest daily vaccinations: {df['daily_vaccinations'].max():,}")
print(f"Average daily vaccinations: {df['daily_vaccinations'].mean():,.0f}")

# Conclusion

print("\nConclusion for Objective 1:")
print("The vaccination program in India started in January 2021 and showed steady growth.")
print("There were several peaks in daily vaccinations, with the highest around mid-2021.")
print("The program maintained a relatively high average daily vaccination rate throughout.")


# Objective 2: Compare first dose vs. second dose vaccination rates


# Calculate vaccination ratios
df['first_dose_ratio'] = df['people_vaccinated'] / df['total_vaccinations']
df['second_dose_ratio'] = df['people_fully_vaccinated'] / df['total_vaccinations']

# Plot the comparison
plt.figure(figsize=(12,6))
df[['first_dose_ratio', 'second_dose_ratio']].plot(title='First Dose vs Second Dose Vaccination Ratios')
plt.ylabel('Ratio of Total Vaccinations')
plt.xlabel('Date')
plt.grid(True)
plt.show()

# Plot absolute numbers
plt.figure(figsize=(12,6))
df[['people_vaccinated', 'people_fully_vaccinated']].plot(title='First Dose vs Second Dose Vaccinations')
plt.ylabel('Number of People')
plt.xlabel('Date')
plt.grid(True)
plt.show()

# Print key statistics
print("\nFirst vs Second Dose Statistics:")
print(f"Maximum first dose ratio: {df['first_dose_ratio'].max():.2%}")
print(f"Maximum second dose ratio: {df['second_dose_ratio'].max():.2%}")
print(f"Final first dose count: {df['people_vaccinated'].max():,}")
print(f"Final second dose count: {df['people_fully_vaccinated'].max():,}")

# Conclusion
print("\nConclusion for Objective 2:")
print("Initially, the first dose ratio was nearly 100% as the program started.")
print("Over time, the second dose ratio increased as people completed their vaccination schedules.")
print("The gap between first and second doses narrowed significantly by the end of the dataset.")

# Objective 3: Analyze vaccination rates per hundred population


# Plot vaccination rates per hundred
plt.figure(figsize=(12,6))
df[['total_vaccinations_per_hundred', 
    'people_vaccinated_per_hundred', 
    'people_fully_vaccinated_per_hundred']].plot(title='Vaccination Rates per Hundred Population')
plt.ylabel('Vaccinations per Hundred People')
plt.xlabel('Date')
plt.grid(True)
plt.show()

# Print key statistics
print("\nVaccination Rates per Hundred Statistics:")
print(f"Final total vaccinations per hundred: {df['total_vaccinations_per_hundred'].max():.2f}")
print(f"Final people vaccinated per hundred: {df['people_vaccinated_per_hundred'].max():.2f}")
print(f"Final fully vaccinated per hundred: {df['people_fully_vaccinated_per_hundred'].max():.2f}")

# Conclusion
print("\nConclusion for Objective 3:")
print("The vaccination rates per hundred population show the penetration of the vaccination program.")
print("The total vaccinations per hundred exceeded 150, indicating many people received boosters.")
print("The fully vaccinated rate reached about 66.7%, showing significant population coverage.")

# Objective 4: Examine the booster dose rollout and impact

# Plot booster doses
plt.figure(figsize=(12,6))
df['total_boosters'].plot(title='Total Booster Doses Administered')
plt.ylabel('Number of Booster Doses')
plt.xlabel('Date')
plt.grid(True)
plt.show()

# Plot booster rate per hundred
plt.figure(figsize=(12,6))
df['total_boosters_per_hundred'].plot(title='Booster Doses per Hundred Population')
plt.ylabel('Boosters per Hundred People')
plt.xlabel('Date')
plt.grid(True)
plt.show()

# Print key statistics
print("\nBooster Dose Statistics:")
print(f"Total booster doses administered: {df['total_boosters'].max():,}")
print(f"Booster doses per hundred population: {df['total_boosters_per_hundred'].max():.2f}")
print(f"Percentage of fully vaccinated who received boosters: {(df['total_boosters'].max()/df['people_fully_vaccinated'].max())*100:.1f}%")

# Conclusion
print("\nConclusion for Objective 4:")
print("Booster doses were introduced later in the vaccination campaign.")
print("The booster program achieved significant uptake, with about 13.3 boosters per hundred population.")
print("Approximately 20% of fully vaccinated individuals received a booster dose by the end of the dataset.")


# Objective 5: Analyze vaccination trends by month


# Resample data by month
monthly = df.resample('M').agg({
    'daily_vaccinations': 'mean',
    'total_vaccinations': 'max',
    'people_vaccinated': 'max',
    'people_fully_vaccinated': 'max'
})

# Plot monthly trends
plt.figure(figsize=(12,6))
monthly[['daily_vaccinations']].plot(kind='bar', title='Average Daily Vaccinations by Month')
plt.ylabel('Average Daily Vaccinations')
plt.xlabel('Month')
plt.grid(True)
plt.show()

# Plot cumulative monthly
plt.figure(figsize=(12,6))
monthly[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']].plot(title='Cumulative Vaccinations by Month')
plt.ylabel('Number of Vaccinations')
plt.xlabel('Month')
plt.grid(True)
plt.show()

# Print key monthly statistics
print("\nMonthly Vaccination Statistics:")
print(f"Month with highest average daily vaccinations: {monthly['daily_vaccinations'].idxmax().strftime('%B %Y')}")
print(f"Highest average daily vaccinations: {monthly['daily_vaccinations'].max():,.0f}")

# Conclusion
print("\nConclusion for Objective 5:")
print("Vaccination rates varied significantly by month, with peaks in mid-2021.")
print("The program maintained high vaccination rates for several consecutive months.")
print("Monthly trends show the program's ability to scale up and sustain vaccination efforts.")
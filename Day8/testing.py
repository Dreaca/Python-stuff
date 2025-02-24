# import pandas as pd

# df = pd.read_csv("Day8/my_csv_file.csv")

# filtered = df['Temperature']

# filteredList = [i for i,temp in enumerate(list(filtered)) if type(temp) != float  or pd.isna(i)]

# print(filteredList)

# Question 3 
# import pandas as pd
# import numpy as np

# # (a) Load the dataset and display the first five rows
# df = pd.read_csv("employee_data.csv")
# print("First 5 rows of the dataset:")
# print(df.head())

# # (b) Compute the mean, median, and standard deviation of the Salary column using NumPy
# salary_mean = np.mean(df["Salary"])
# salary_median = np.median(df["Salary"])
# salary_std = np.std(df["Salary"])

# print("\nSalary Statistics:")
# print(f"Mean Salary: {salary_mean}")
# print(f"Median Salary: {salary_median}")
# print(f"Standard Deviation of Salary: {salary_std}")

# # (c) Find the total number of employees with ExperienceYears > 10
# experienced_employees = df[df["ExperienceYears"] > 10].shape[0]
# print(f"\nTotal number of employees with more than 10 years of experience: {experienced_employees}")

# # (d) Identify and display the five highest-paid employees, sorted in descending order of Salary
# top_paid_employees = df.nlargest(5, "Salary")
# print("\nFive highest-paid employees:")
# print(top_paid_employees)

# # (e) Determine the percentage of employees aged above 50
# total_employees = df.shape[0]
# employees_above_50 = df[df["Age"] > 50].shape[0]
# percentage_above_50 = (employees_above_50 / total_employees) * 100

# print(f"\nPercentage of employees aged above 50: {percentage_above_50:.2f}%")

# # (f) Add a new column "ExperienceLevel"
# def categorize_experience(exp):
#     if exp >= 15:
#         return "Senior"
#     elif 5 <= exp <= 14:
#         return "Mid-Level"
#     else:
#         return "Junior"

# df["ExperienceLevel"] = df["ExperienceYears"].apply(categorize_experience)

# # (g) Sort the dataset by ExperienceLevel (Senior first), then by Salary in descending order
# experience_order = {"Senior": 0, "Mid-Level": 1, "Junior": 2}
# df["ExperienceOrder"] = df["ExperienceLevel"].map(experience_order)

# sorted_df = df.sort_values(by=["ExperienceOrder", "Salary"], ascending=[True, False]).drop(columns=["ExperienceOrder"])

# print("\nDataset sorted by ExperienceLevel and Salary:")
# print(sorted_df.head())

# # Save the modified dataset to a new CSV file
# sorted_df.to_csv("modified_employee_data.csv", index=False)

#Question 3

#A
# import requests
# from bs4 import BeautifulSoup

# # URL of the financial market page
# url = "https://example.com/market"

# try:
#     # Send an HTTP GET request
#     response = requests.get(url, timeout=10)
    
#     # Check if request was successful (HTTP status 200)
#     if response.status_code == 200:
#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, "html.parser")

#         # Extract data using class names
#         company_name = soup.find("h2", class_="company-name")
#         ticker = soup.find("p", class_="ticker")
#         price = soup.find("span", class_="current-price")

#         # Validate extracted data
#         if company_name and ticker and price:
#             print(f"Company: {company_name.text.strip()}")
#             print(f"Ticker: {ticker.text.strip()}")
#             print(f"Current Price: {price.text.strip()}")
#         else:
#             print("Error: Expected HTML elements not found.")

#     else:
#         print(f"HTTP Error: {response.status_code}")

# except requests.exceptions.RequestException as e:
#     print(f"Network Error: {e}")

# #B

# import requests

# # API endpoint
# api_url = "https://api.example.com/market"

# try:
#     # Send GET request
#     response = requests.get(api_url, timeout=10)

#     # Check if request was successful (HTTP status 200)
#     if response.status_code == 200:
#         stock_data = response.json()  # Convert JSON response to Python dictionary

#         print("Stock Market Data:")
#         for stock in stock_data:
#             print(f"Company: {stock['company']}")
#             print(f"Ticker: {stock['ticker']}")
#             print(f"Current Price: ${stock['price']:.2f}\n")

#     else:
#         print(f"HTTP Error: {response.status_code}")

# except requests.exceptions.RequestException as e:
#     print(f"Network Error: {e}")

import random
import csv

def generate_random_data(num_samples):
    data = []
    for _ in range(num_samples):
        weight = random.uniform(40, 100)  # Generating random weight between 40 and 100 kg
        height = random.uniform(1.5, 2)   # Generating random height between 1.5 and 2 meters
        gender = random.choice(['male', 'female'])  # Randomly choosing gender
        data.append({'Weight': weight, 'Height': height, 'Gender': gender})
    return data

def calculate_bmi(weight, height, system='metric'):
    if system.lower() == 'metric':
        bmi = weight / (height ** 2)
    elif system.lower() == 'imperial':
        bmi = (weight / (height ** 2)) * 703
    else:
        raise ValueError("Invalid system. Choose 'metric' or 'imperial'.")
    return bmi

def save_to_csv(data, filename='bmi_data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Weight', 'Height', 'Gender', 'BMI']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            row['BMI'] = calculate_bmi(row['Weight'], row['Height'])
            writer.writerow(row)

# Generate random data
num_samples = 100
random_data = generate_random_data(num_samples)

# Save data to CSV file
save_to_csv(random_data)

print(f"Random data with BMI calculated has been saved to 'bmi_data.csv'.")

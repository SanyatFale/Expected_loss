import csv

def calculate_bmi(weight, height, system='metric'):
    if system.lower() == 'metric':
        bmi = weight / (height ** 2)
    elif system.lower() == 'imperial':
        bmi = (weight / (height ** 2)) * 703
    else:
        raise ValueError("Invalid system. Choose 'metric' or 'imperial'.")
    return bmi

def predict_gender(bmi, threshold=23):
    return 'male' if bmi > threshold else 'female'

def update_csv_with_prediction(input_filename='bmi_data.csv', output_filename='bmi_data_with_prediction.csv'):
    with open(input_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        fieldnames = reader.fieldnames + ['Prediction']
        
        with open(output_filename, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                bmi = calculate_bmi(float(row['Weight']), float(row['Height']))
                prediction = predict_gender(bmi)
                row['Prediction'] = prediction
                writer.writerow(row)

# Update CSV file with gender predictions
update_csv_with_prediction()

print("Gender predictions added to the CSV file (bmi_data_with_prediction.csv).")

import csv

def calculate_conditional_risk(input_filename='bmi_data_with_prediction.csv'):
    total_samples = 0
    incorrect_predictions_female = 0
    incorrect_predictions_male = 0
    total_female = 0
    total_male = 0

    with open(input_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            total_samples += 1 
            if row['Gender'] != row['Prediction']:
                if row['Gender'] == 'female':
                    incorrect_predictions_female += 1
                elif row['Gender'] == 'male':
                    incorrect_predictions_male += 1

            if row['Gender'] == 'female':
                total_female += 1
            elif row['Gender'] == 'male':
                total_male += 1

    conditional_risk_female = incorrect_predictions_female / total_female
    conditional_risk_male = incorrect_predictions_male / total_male

    return conditional_risk_female, conditional_risk_male

# Calculate conditional risk for females and males
risk_female, risk_male = calculate_conditional_risk()
print(f"Conditional risk (loss = 1 | female, weight, height): {risk_female:.4f}")
print(f"Conditional risk (loss = 1 | male, weight, height): {risk_male:.4f}")

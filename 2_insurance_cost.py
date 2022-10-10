#You are curious about how certain factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.

#You will apply your new knowledge of Python functions to write a useful function that calculates medical insurance costs.


# Create calculate_insurance_cost() function below:

def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name = "this person"):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + str(name) + " is " + str(estimated_cost) + " dollars.")

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")

# Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")

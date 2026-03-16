# Heart Disease Detection without Dataset

print("Enter Patient Details")

age = int(input("Age: "))
sex = int(input("Sex (1 = Male, 0 = Female): "))
cp = int(input("Chest Pain Type (0-3): "))
bp = int(input("Blood Pressure: "))
chol = int(input("Cholesterol Level: "))

# Risk counter
risk = 0

if age > 50:
    risk += 1
if bp > 140:
    risk += 1
if chol > 240:
    risk += 1
if cp >= 1:
    risk += 1

print("\n--- Heart Disease Prediction Result ---")

if risk >= 2:
    print("⚠️ Heart Disease Risk Detected")
else:
    print("✅ No Heart Disease Risk Detected")

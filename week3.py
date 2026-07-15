import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("healthcare_dataset.csv")

print("First 5 Records")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInformation")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

df = df.drop_duplicates()

df["Name"] = df["Name"].str.title()

df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

df["Length of Stay"] = (
    df["Discharge Date"] - df["Date of Admission"]
).dt.days

print("\nSummary Statistics")
print(df.describe())

print("\nAverage Age")
print(df["Age"].mean())

print("\nAverage Billing Amount")
print(df["Billing Amount"].mean())

print("\nAverage Length of Stay")
print(df["Length of Stay"].mean())

print("\nGender Distribution")
print(df["Gender"].value_counts())

print("\nBlood Group Distribution")
print(df["Blood Type"].value_counts())

print("\nAdmission Types")
print(df["Admission Type"].value_counts())

print("\nMedical Conditions")
print(df["Medical Condition"].value_counts())

print("\nInsurance Providers")
print(df["Insurance Provider"].value_counts().head(10))

print("\nTop Hospitals")
print(df["Hospital"].value_counts().head(10))

print("\nTop Doctors")
print(df["Doctor"].value_counts().head(10))

condition_bill = df.groupby("Medical Condition")["Billing Amount"].mean()

print("\nAverage Billing by Medical Condition")
print(condition_bill)

gender_bill = df.groupby("Gender")["Billing Amount"].mean()

print("\nAverage Billing by Gender")
print(gender_bill)

stay = df.groupby("Admission Type")["Length of Stay"].mean()

print("\nAverage Stay by Admission Type")
print(stay)

def age_group(age):
    if age < 18:
        return "Child"
    elif age < 40:
        return "Adult"
    elif age < 60:
        return "Middle Age"
    else:
        return "Senior"

df["Age Group"] = df["Age"].apply(age_group)

print("\nAge Groups")
print(df["Age Group"].value_counts())

df["Month"] = df["Date of Admission"].dt.month_name()

print("\nAdmissions by Month")
print(df["Month"].value_counts())

plt.figure(figsize=(8,5))
df["Medical Condition"].value_counts().plot(kind="bar")
plt.title("Patients by Medical Condition")
plt.xlabel("Condition")
plt.ylabel("Patients")
plt.tight_layout()
plt.show()

plt.figure(figsize=(5,5))
df["Gender"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.title("Gender Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
condition_bill.sort_values().plot(kind="bar")
plt.title("Average Billing Amount")
plt.xlabel("Medical Condition")
plt.ylabel("Billing")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
stay.plot(kind="bar",color="orange")
plt.title("Average Stay")
plt.xlabel("Admission Type")
plt.ylabel("Days")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
df["Age"].plot(kind="hist",bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
df["Blood Type"].value_counts().plot(kind="bar")
plt.title("Blood Group Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df["Insurance Provider"].value_counts().head(10).plot(kind="bar")
plt.title("Top Insurance Providers")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df["Hospital"].value_counts().head(10).plot(kind="bar")
plt.title("Top Hospitals")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df["Month"].value_counts().plot(kind="line",marker="o")
plt.title("Monthly Admissions")
plt.xlabel("Month")
plt.ylabel("Patients")
plt.tight_layout()
plt.show()

summary = pd.DataFrame({
    "Total Patients":[len(df)],
    "Average Age":[round(df["Age"].mean(),2)],
    "Average Billing":[round(df["Billing Amount"].mean(),2)],
    "Average Stay":[round(df["Length of Stay"].mean(),2)],
    "Hospitals":[df["Hospital"].nunique()],
    "Doctors":[df["Doctor"].nunique()]
})

summary.to_csv("hospital_summary.csv",index=False)

df.to_csv("cleaned_healthcare_dataset.csv",index=False)

print("\nSummary")
print(summary)

print("\nProject Completed Successfully")
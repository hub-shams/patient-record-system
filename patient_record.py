import pickle
import os

class Patient:
    def __init__(self, patient_id, name, age, gender, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.ailment = ailment


    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Ailment: {self.ailment}")


class PatientRecordSystem:
    def __init__(self, filename = "patients.pkl"):
        self.filename = filename
        self.patients = self.load_data()


    def add_patient(self, patient):
        self.patients.append(patient)
        self.save_data()
        print("✅ Patient added and saved successfully!")


    def view_all_patients(self):
        if not self.patients:
            print("⚠️ No patients in the record.")
        for patient in self.patients:
            patient.display_info()

    def search_patient(self, name):
        found = False
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                patient.display_info()
                found = True
        if not found:
            print("❌ No patient found with that name.")

    def save_data(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.patients, f)


    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        else:
            return []

def run_system():
    system = PatientRecordSystem()
    while True:
        print("\n====== Patient Record System ======")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by Name")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pid = input("Enter patient ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            gender = input("Enter Gender(Male or Female): ")
            ailment = input("Enter ailment: ")
            patient = Patient(pid, name, age, gender, ailment)
            system.add_patient(patient)

        elif choice == '2':
            system.view_all_patients()

        elif choice == '3':
            name = input("Enter patient name to search: ")
            system.search_patient(name)

        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    run_system()

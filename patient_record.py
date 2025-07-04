import pickle
import os 

class Patient:
    def __init__(self, patient_id, name, age, ailment):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.ailment = ailment

    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Ailment: {self.ailment}")

class PatientRecordSystem:
    def __init__(self, filename="patients.pkl"):
        self.filename = filename
        self.patients = self.load_data()     #why is it that this part of the code was initilized and not the rest?

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

    def del_patient(self, patient_id):
        """Delete a patient by patientID with confirmation."""
        for index, patient in enumerate(self.patients):
            if patient.patient_id == patient_id:
                print("\n⚠️ Patient found:")
                print(f"🆔 ID: {patient.patient_id}")
                print(f"🧑 Name: {patient.name}")
                print(f"🎂 Age: {patient.age}")
            
                confirm = input("\nAre you sure you want to delete this patient? (yes/no): ").strip().lower()
                if confirm == "yes":
                    del self.patients[index]
                    self.save_data()
                    print("✅ Patient record deleted successfully.")
                else:
                    print("❎ Deletion cancelled.")
                return
        print("❌ Patient ID not found in the records.")

                      
        
            


def run_system():
    system = PatientRecordSystem()
    while True:
        print("\n====== Patient Record System ======")
        print("1. Add Patient")
        print("2. to delete a patient-record")
        print("3. View All Patients")
        print("4. Search patient by name")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pid = input("Enter patient ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            ailment = input("Enter ailment: ")
            patient = Patient(pid, name, age, ailment)
            system.add_patient(patient)

        elif choice == "2":
            patientID = input("Enter the patient Id you want to delete: ")
            system.del_patient(patientID)

        elif choice == '3':
            system.view_all_patients()

        elif choice == '4':
            name = input("Enter patient name to search: ")
            system.search_patient(name)

        elif choice == '5':
            print("Exiting system. Goodbye!")
            break

            
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    run_system()

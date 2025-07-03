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
            
    """ #this block of code was replaced by another load_data() function.
    def load_data(self):
        if os.path.exist(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        else:
            return []
    """

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                data = pickle.load(f)
                # Patch older patient objects
                for patient in data:
                    if not hasattr(patient, "gender"):
                        patient.gender = "Unknown"
                    if not hasattr(patient, "ailment"):
                        patient.ailment = "N/A"
                return data
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
                print(f"🆔 Gender: {patient.gender}")
            
                confirm = input("\nAre you sure you want to delete this patient? (yes/no): ").strip().lower()
                if confirm == "yes":
                    del self.patients[index]
                    self.save_data()
                    print("✅ Patient record deleted successfully.")
                else:
                    print("❎ Deletion cancelled.")
                return
        print("❌ Patient ID not found in the records.")

    def update_patient(self, patient_id):
        """update patient record by patient_id"""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print("\n📝 Patient found:")
                patient.display_info()

                print("\nEnter new values (press Enter to keep current):")
                name = input(f"Name [{patient.name}]: ") or patient.name
                age = input(f"Age [{patient.age}]: ") or patient.age
                gender = input(f"Gender [{patient.gender}]: ") or patient.gender
                ailment = input(f"Ailment [{patient.ailment}]: ") or patient.ailment
                            # Apply updates
                patient.name = name
                patient.age = age
                patient.gender = gender
                patient.ailment = ailment

                self.save_data()
                print("✅ Patient record updated successfully.")
                return

        print("❌ Patient ID not found.")
            


        
            


def run_system():
    system = PatientRecordSystem()
    while True:
        print("\n====== Patient Record System ======")
        print("1. Add Patient")
        print("2. to delete a patient record")
        print("3. to update/Edit a patient record")
        print("4. View All Patients")
        print("5. Search patient by name")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pid = input("Enter patient ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            gender = input("Enter gender: ")
            ailment = input("Enter ailment: ")
            patient = Patient(pid, name, age, gender, ailment)
            system.add_patient(patient)

        elif choice == "2":
            patientID = input("Enter the patient Id you want to delete: ")
            system.del_patient(patientID)

        elif choice =="3":
            pid = input("Enter patient ID to update: ")
            system.update_patient(pid)


        elif choice == '4':
            system.view_all_patients()

        elif choice == '5':
            name = input("Enter patient name to search: ")
            system.search_patient(name)

        elif choice == '6':
            print("Exiting system. Goodbye!")
            break

            
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    run_system()

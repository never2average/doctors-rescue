import json
from models import Appointment, Medicines

def listOnePatient(doctorName, hospitalName, patientName):
    return Appointment.objects(hospitalName=hospitalName, doctorName=doctorName, patientName=patientName).order_by("startDateTime-").limit(1).to_json()

def listAllPatient(doctorName, hospitalName):
    return Appointment.objects(hospitalName=hospitalName, doctorName=doctorName).to_json()

def updatePatientReports(doctorName, hospitalName, patientName, appointmentReport, prescription):
    prescription = json.loads(prescription)
    pList = []
    for i in prescription:
        pList.append(Medicines(
            medicineName=i["name"],
            medicineDosage=i["dose"],
            medicineSchedule=i["sched"],
            medicineNumDays=i["numDays"]
        ))
    Appointment.objects(hospitalName=hospitalName, doctorName=doctorName, patientName=patientName).update(set__appointmentReport=appointmentReport, set__prescription=pList)

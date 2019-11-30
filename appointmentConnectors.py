import datetime
from mongoengine import Appointment, Symptoms

def listDoctors(symptomList):
    pass

def pre_appointment_report(symptomList):
    pass

def makeAppointments(doctorName, hospitalName, patientName, symptomList, appointmentDateTime):
    app = Appointment(doctorName=doctorName, hospitalName=hospitalName, patientName=patientName)
    app.save()
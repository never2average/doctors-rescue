from mongoengine import Document, StringField, DateTimeField, IntField, ListField, PointField
from mongoengine import EmbeddedDocument, EmbeddedDocumentListField, EmailField, URLField

class Doctor(EmbeddedDocument):
    doctorName = StringField(required=True)
    doctorEmail = EmailField(required=True)
    doctorSpecialization = EmailField(required=True)

class Hospital(Document):
    hospitalName = StringField(required=True)
    hospitalLocation = PointField(required=True)
    doctorsList = EmbeddedDocumentListField(Doctor)

class Symptom(Document):
    patientName = StringField(required=True)
    symptomName = StringField(required=True)
    symptomSeverity = StringField(required=True, choices=["None","Mild","Moderate","Severe"])
    date = DateTimeField(required=True)

class Patient(Document):
    patientName = StringField(required=True, unique=True)
    patientProfileURL = StringField(required=True)

class Medicines(EmbeddedDocument):
    medicineName = StringField(required=True)
    medicineDosage = IntField(required=True)
    medicineSchedule = StringField(required=True)
    medicineNumDays = IntField(required=True)

class Appointment(Document):
    startDateTime = DateTimeField(required=True)
    endDateTime = DateTimeField(required=True)
    patientName = StringField(required=True)
    hospitalName = StringField(required=True)
    doctorName = StringField(required=True)
    preAppointmentReport = URLField(required=True)
    appointmentReport = StringField(required=True)
    prescription = EmbeddedDocumentListField(Medicines)

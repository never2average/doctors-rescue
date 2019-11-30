from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource, request
import mongoengine
from flask_cors import CORS
from appointmentConnectors import listDoctors, makeAppointments
from doctorConnectors import listOnePatient, listAllPatient, updatePatientReports


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
mongoengine.connect()


class Appointments(Resource):
    def get(self):
        symptomList = request.headers.get('symptomList')
        try:
            return make_response(listDoctors(symptomList), 200)
        except Exception:
            return make_response(jsonify({"data": "Invalid Data"}), 300)
    def post(self):
        doctorName = request.headers.get("doctor")
        hospitalName = request.headers.get("hospital")
        patientName = request.headers.get("patient")
        symptomList = request.headers.get("symptoms")
        try:
            return make_response(makeAppointments(doctorName, hospitalName, patientName, symptomList), 200)
        except Exception:
            return make_response(jsonify({"data": "Invalid Data"}), 300)


class DoctorUtlities(Resource):
    def get(self):
        doctorName = request.headers.get("doctor")
        hospitalName = request.headers.get("hospital")
        patientName = request.headers.get("patient")
        if patientName is not None:
            try:
                return make_response(listOnePatient(doctorName, hospitalName, patientName), 200)
            except Exception:
                return make_response(jsonify({"data": "Invalid Data"}), 300)
        else:
            try:
                return make_response(listAllPatient(doctorName, hospitalName), 200)
            except Exception:
                return make_response(jsonify({"data": "Invalid Data"}), 300)
    
    def put(self):
        doctorName = request.headers.get("doctor")
        hospitalName = request.headers.get("hospital")
        patientName = request.headers.get("patient")
        appointmentReport = request.headers.get("appointment")
        prescription = request.headers.get("prescription")
        try:
            return make_response(updatePatientReports(doctorName, hospitalName, patientName, appointmentReport, prescription), 200)
        except Exception:
            return make_response(jsonify({"data": "Invalid Data"}), 300)


api.add_resource(Appointments, "/appointment")
api.add_resource(DoctorUtlities, "/utilities")


if __name__ == "__main__":
    app.run(debug=True)
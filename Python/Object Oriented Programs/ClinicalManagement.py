# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:33:58 2020

@author: Niraj
"""

import json
import os


class ClinicManagement:


    def __init__(self):
        pass

    def doctorInformation(self):
        with open('doctor.json', 'r+') as doctorFile:
            doctorfilereader = doctorFile.read()
            jsonDoctor = json.loads(doctorfilereader)
            doctorFile.close()
        return jsonDoctor

    def patientInformation(self):
        with open('patient.json', 'r+') as patientFile:
            patientFileReader = patientFile.read()
            jsonPatientfile = json.loads(patientFileReader)
            patientFile.close()
        return jsonPatientfile
    
    def addPatients(self,patientDict):
        try:
            if os.path.exists("patient.json") == False:
                print("File Created")
                open("patient.json", "w").close
            with open("patient.json","r") as outputFile:
                sizeOfFile = os.stat("patient.json").st_size
                if(sizeOfFile == 0):
                    data = {}
                else:
                    data = json.load(outputFile)
                if "Patients" not in data:
                    data["Patients"] = []
                    data["Patients"].append(patientDict)
                else:
                    temp = data["Patients"]
                    temp.append(patientDict)
            
            with open('patient.json', 'w') as f: 
                json.dump(data,f,indent = 4)
                print(data["Patients"])
                
        except(IOError):
            print("File can't be found")



    def appointment(self):
        if os.path.exists("appointments.json") == False:
                print("File Created")
                open("appointments.json", "w").close
#        
        with open("appointments.json","r") as outputFile:
                sizeOfFile = os.stat("appointments.json").st_size
                if(sizeOfFile == 0):
                    jsonappointmentsFile = {}
                else:
                    jsonappointmentsFile = json.load(outputFile)
        return jsonappointmentsFile

    def addDoct(self):
        docName = input(" Enter doctor Name: \n")
        dId = input(" Enter Doctor ID: \n")
        dSpcl = input(" Enter specialization: \n")
        dAvil = input(" Enter availability in (AM/PM/BOTH): \n")
        try:
            if os.path.exists("doctor.json") == False:
                print("File Created")
                open("doctor.json", "w").close
            with open("doctor.json","r") as outputFile:
                sizeOfFile = os.stat("doctor.json").st_size
                if(sizeOfFile == 0):
                    data = {}
                else:
                    data = json.load(outputFile)
                dictionaryData ={}
                dictionaryData["name"] = docName.upper()
                dictionaryData["idDoctor"] = dId
                dictionaryData["specialization"] = dSpcl.upper()
                dictionaryData["availability"] = dAvil.upper()
                                                                                         
                
                if "doctors" not in data:
                    data["doctors"] = []
                    data["doctors"].append(dictionaryData)
                else:
                    temp = data["doctors"]
                    temp.append(dictionaryData)
            
            with open('doctor.json', 'w') as f: 
                json.dump(data,f,indent = 4)
                print(data["doctors"])
                
        except(IOError):
            print("File can't be found")
  


    def displayDoct(self):
        doct = self.doctorInformation()
        doctors = doct['doctors']
        print("\nID,Name,Specialization")
        for i in range(len(doctors)):
            name = doctors[i]['name']
            spcl = doctors[i]['speciliaztion']
            doctorID = doctors[i]['idDoctor']
            print("{},{},{}".format(doctorID,name,spcl))


    def addAppointment(self):
        
        doct = self.doctorInformation()
        doctors = doct['doctors']
        for i in range(len(doctors)):
            name = doctors[i]['name']
            doctorId = doctors[i]['idDoctor']
            spclzn = doctors[i]['specialization']
            available = doctors[i]['availability']
            print("Doctor having id {} and name {} with {} is available at {}".format(doctorId,name,spclzn,available))
        doctName = input("Enter the Doctor Name")
        time = input(" Availability (AM/PM/BOTH)")
        appointmentDict = self.appointment()  # read appointment json.
        if doctorId not in appointmentDict:
            appointmentList =[]
        else:
            appointmentList = appointmentDict[doctorId]  # store all patients of 1 doctor in list.
        print("Appointment list is ", appointmentList)
        if len(appointmentList) <= 5:
            for i in range(len(doctors)):
                if doctors[i]["name"] == doctName.upper():
                    if time.upper() == doctors[i]["availability"]:
                        print("Doctor is Available..!! Please Enter the patient details:")
                        name = input(" Enter pName:")
                        patientID = input(" Enter patient Id:")
                        age = int(input(" Enter patient age:"))
                        mob_no = input(" Enter patient's pMobNumber:")       
                        jsonAppointFile = self.appointment()
                        new_dict = {"pName": name.upper(), "Id": patientID, "pAge": age, "pMobNumber": mob_no, "Time": time.upper()}
                        self.addPatients(new_dict)
                        with open('appointments.json', 'a+') as f:
                            if doctorId not in jsonAppointFile:
                                jsonAppointFile[doctorId] = [new_dict]
                            else:
                                 jsonAppointFile[doctorId].append([new_dict])
                            f.write(json.dumps(jsonAppointFile, indent=4))
                        print("Your appointment is fixed. Thank You !")
                    else:
                        print("Sorry. Doctor is not available at the Moment !! ")



    def doctorSearchById(self):
        doct = self.doctorInformation()
        doctors = doct['doctors']
        doctorID = input("Enter doctor Id :")
        print(doct)
        for i in range(len(doct)):
            if doctors[i]["idDoctor"] == doctorID:
                print("Congrats Doctor is available..!!")
                break
            else:
                print("Sorry Doctor is not available..!!")
                break



    def doctorSearchBySpclzn(self):
        doct = self.doctorInformation()
        doctors = doct['doctors']
        spec = input("Enter doctor specilization you want to search:")
        for i in range(len(doct)):
            if spec.upper() == doctors[i]["specialization"]:
                print("Congratulations Doctor is available..!!")
                break
            else:
                print("Sorry Doctor is not available..!!")
                break



    def doctorSearchByName(self):
        doct = self.doctorInformation()
        doctors = doct['doctors']
        name = input("Enter the Doctor name that you want to Search:")
        for i in range(len(doct)):
            if name.upper() == doctors[i]["name"]:
                print("Doctor is available..!!")
                break
            else:
                print("Doctor is not available..!!")
                break
    
    def patientSearchByName(self):
        patientInfo = self.patientInformation()
        patients = patientInfo['Patients']
        name = input("Enter Patients name :")
        for i in range(len(patientInfo)):
            if patients[i]["pName"] == name.upper():
                print("A patients with above name is available")
                break
            else:
                print("A patients with above name is not available")
                break



    def patientSearchById(self):
        patientInfo = self.patientInformation()
        patients = patientInfo['Patients']
        patientID = input("Enter Patients id :")
        for i in range(len(patientInfo)):
            if patients[i]["Id"] == patientID:
                print("A patients with above Id is available")
                break
            else:
                print("A patients with above Id is not available")
                break



    def patientSearchByMobileNo(self):
        patientInfo = self.patientInformation()
        patients = patientInfo['Patients']
        patientMobileNo = input("Enter Patients mobile number :")
        for i in range(len(patientInfo)):
            if patients[i]["pMobNumber"] == patientMobileNo:
                print("A patients with above mobile number is available")
                break
            else:
                print("A patients with above mobile number is not available")
                break



    def Users(self):
        print("------------------- Hospital Management -------------------\n")
        yn = input("Do you Want to Continue? (Y/N)")
        while (yn == 'y') or (yn == 'Y') or (yn == 'Yes') or (yn == 'yes'):
            choice = int(input("Press \n 1. Doctor options \n 2. Patient options \n 3.Search patients \n  4. Exit "))
            if choice == 1:
                ch = int(input("Press \n 1. Add doctor \n 2. View doctor \n 3. Go back\n "))
                if ch == 1:
                    self.addDoct()
                    
                if ch == 2:
                    self.displayDoct()
                    
                if ch == 3:
                    yn == 3
            if choice == 2:
                ch = int(input("Press \n 1. Add appointment \n 2. search doctor \n 3. Go back "))
                if ch == 1:
                    self.addAppointment()
                    
                if ch == 2:
                    op = int(input("Press \n 1. Seach by ID \n 2. Search by Specalization \n 3. Seach by Name\n "))
                    if op == 1:
                        self.doctorSearchById()
                        
                    if op == 2:
                        self.doctorSearchBySpclzn()
                        
                    if op == 3:
                        self.doctorSearchByName()
                        
                if ch == 3:
                    (yn == 'n') or (yn == 'N') or (yn == 'No') or (yn == 'no')
            
            if choice == 3:
                ch = int(input("Press \n 1. Seach by Name \n 2. Search by MobileNumber \n 3. Seach by ID\n 4.Exit  "))
                if ch == 1:
                    self.patientSearchByName()
                    
                if ch == 2:
                    self.patientSearchByMobileNo()
                    
                if ch == 3:
                    self.patientSearchById()
                    
                if ch == 4:
                    (yn == 'n') or (yn == 'N') or (yn == 'No') or (yn == 'no')
                
            
            if choice == 4:
                exit()

objClinicManagement = ClinicManagement()
objClinicManagement.Users()

import pandas as pd
import numpy as np



data = pd.read_csv("E:\PDAC study\diagnosis.csv")

print('data.shape', data.shape)
#(662195, 10)

print('data.size', data.size)
#6621950

print('data.columns', data.columns)
#Index(['patient_id', 'encounter_id', 'code_system', 'code',
#       'principal_diagnosis_indicator', 'admitting_diagnosis',
#       'reason_for_visit', 'date', 'derived_by_TriNetX', 'source_id'],
#      dtype='object')


data.drop_duplicates(inplace=True) # remove duplicate rows based on all columns
#>>> data.shape
#(615828, 22)


datafiltered1 = data[(data["code"]=='C25')|(data["code"]=='C25.0')|(data["code"]=='C25.1')|(data["code"]=='C25.7')]

np.unique(data[(data["code"]=='C25')|(data["code"]=='C25.0')|(data["code"]=='C25.1')|(data["code"]=='C25.7')]['patient_id']).shape
#(1124,)


patients = np.unique(datafiltered1["patient_id"])


conditions1 = ['C25', 'C25.0', 'C25.1', 'C25.7']
conditions2 = ['C24', 'C24.1', 'C24.8', 'C17', 'K83', 'K83.31', 'K83.3','K80.30',
               'K80.32', 'K80.33', 'K80.35', 'K80.36', 'K80.34', 'C22.1', 'C22']
conditions3 = ['4492', '12574', '2555', '32592', '51499', '56946', '0M0P5042943', '40048', '4179',
               '1597876', '72965', '84857', '224905', '0M0P5051437', '1298944', '3002', '3639']
conditions4 = ['CPT48154', 'CPT48152', 'CPT48153', 'CPT1007926', 'CPT48150', 'SNOMED116031009', 'ICD-10-PCS0FTG02Z', 'CPT1007923']
conditions5 =['CPT43262', 'CPT1007283', 'CPT43274', 'CPT1021432', 'CPT43260', 'CPT43261', 'SNOMED174653005',
              'SNOMED174654004', 'CPT43277', 'SNOMED709467007', 'SNOMED425503000', 'SNOMED432876003', 'SNOMED43211004',
              'SNOMED433134004', 'CPT43276', 'HCPCSC7543', 'HCPCSC7542', 'CPT43274']
conditions6 = ['SNOMED16747000', 'SNOMED42917003', 'ICD-10-PCS0F793DZ', 'ICD-10-PCS0F793ZZ', 'ICD-10-PCS0F993ZZ', 'ICD-10-PCS0F994ZZ',
               'SNOMED315031003', 'CPT43264', 'CPT43265', 'SNOMED174630009', 'CPT74363', 'CPT47532', 'SNOMED174636003']
conditions7 = conditions5 + conditions6


bile_leakage = ['ICD-10-CMK31', 'ICD-10-CMR18.8', 'ICD-10-CMK91.89', 'ICD-10-CMK91.3']
Duodenal_anstomosis_stricture = ['ICD-10-CMK91.89', 'ICD-10-CMK91.3', 'ICD-10-CMK31.5']
intra_abdominal_abscess_hematoms  = ['ICD-10-CMK61.11', 'ICD-10-CMT81.43', 'ICD-10K66.8']
Wound_dehiscence = ['ICD-10-CMT81.30XA', 'ICD-10-CMT81.31XA', 'ICD-10-CMT81.31', 'ICD-10-CMT81.32',
                    'ICD-10-CMT-81.32XA', 'ICD-10-CMT81.32XD', 'ICD-10-CMT81.89XA', 'SNOMED29629000',
                    'SNOMED80173001', 'CPT1003325', 'CPT13160', 'CPT12020', 'CPT12021', 'CPT49900', 'SNOMED442460002']
pancreatic_fistula = ['ICD-10-CMK86.8', 'ICD-10-CMK86.1']
bile_duct_stricture = ['ICD-10-CMK83.1']
Cjolangitis = ['ICD-10-CMK83.0', 'ICD-10-CMK83.09']
acute_pancreatitis = ['ICD-10-CMK85', 'ICD-10-CMK85.9', 'ICD-10-CMK85.8', 'ICD-10-CMK85.91',
                      'ICD-10-CMK85.92', 'ICD-10-CMK85.82', 'ICD-10-CMK85.90', 'CPT48105']
sepsis = ['ICD-10-CMA41.9', 'ICD-10-CMR65.20', 'ICD-10-CMR65.21']
emergency_department_visit = ['CPT99281', 'CPT99282', 'CPT99283', 'CPT99284', 'CPT99285', 'CPT1013711']
All_hospitalization =['CPT1013659', 'CPT1013660', 'CPT1013699', 'CPT1013729', 'CPT99221', 'CPT99223',
                      'CPT99232', 'CPT99233', 'CPT99231', 'CPT99234', 'CPT99235', 'CPT99236', 'CPT99251',
                      'CPT99252', 'CPT99253', 'CPT99255', 'CPT99254']
obstructive_jaundice = ['ICD-10-CMK83.1']
acute_pancreatitis = ['ICD-10-CMK85']
liver_cirrhosis = ['ICD-10-CMK74', 'ICD-10-CMK73']
Hypertension = ['ICD-10-CMI10', 'ICD-10-CMI11', 'ICD-10-CMI12', 'ICD-10-CMI13', 'ICD-10-CMI14', 'ICD-10-CMI15']
Ischemic_heart_disease = ['ICD-10-CMI20', 'ICD-10-CMI21', 'ICD-10-CMI22', 'ICD-10-CMI23', 'ICD-10-CMI24', 'ICD-10-CMI25']
Diabetic_mellitus = ['ICD-10-CME08', 'ICD-10-CME09', 'ICD-10-CME10', 'ICD-10-CME11', 'ICD-10-CME12', 'ICD-10-CME13']
ASthma = ['ICD-10-CMJ45']
COPD = ['ICD-10-CMJ44']
CKD = ['ICD-10-CMN18']


filtered1 = []
for i in range(len(patients)):
	for j in range(len(conditions2)):
		if conditions2[j] in list(data[data["patient_id"]==patients[i]]["code"]):
			filtered1.append(patients[i])
len(filtered1)
#95
len(np.unique(filtered1))
#81
filtered1 = np.unique(filtered1)
			
patients_filtered1 = np.setdiff1d(patients, filtered1, assume_unique=False)

len(patients_filtered1)
#1043


data2 = pd.read_csv("E:\PDAC study\medication_ingredient.csv")
#data2 = pd.read_csv("/Users/Hsu-Kai/Downloads/PDAC study/medication_ingredient.csv")
data2.drop_duplicates(inplace=True)
filtered2 = []
for i in range(len(patients_filtered1)):
	for j in range(len(conditions3)):
		if conditions3[j] in list(data2[data2["patient_id"]==patients_filtered1[i]]["code"]):
			filtered2.append(patients_filtered1[i])
len(filtered2)
#694
len(np.unique(filtered2))
#252
filtered2 = np.unique(filtered2)
patients_filtered2 = np.setdiff1d(patients_filtered1, filtered2, assume_unique=False)


data3 = pd.read_csv("E:\PDAC study\procedure.csv")
data3.drop_duplicates(inplace=True)
data3["operation"]=data3["code_system"]+data3["code"]
patients_filtered3 = []
for i in range(len(patients_filtered2)):
	for j in range(len(conditions4)):
		if conditions4[j] in list(data3[data3["patient_id"]==patients_filtered2[i]]["operation"]):
			patients_filtered3.append(patients_filtered2[i])

len(patients_filtered3)
#661
patients_filtered3 = np.unique(patients_filtered3)
len(np.unique(patients_filtered3))
#658

patients_filtered4 = []
for i in range(len(patients_filtered3)):
	for j in range(len(conditions5)):
		if conditions5[j] in list(data3[data3["patient_id"]==patients_filtered3[i]]["operation"]):
			patients_filtered4.append(patients_filtered3[i])
len(patients_filtered4)
#555
patients_filtered4 = np.unique(patients_filtered4)
len(patients_filtered4)
#269

filtered5 = []
for i in range(len(patients_filtered4)):
	for j in range(len(conditions6)):
		if conditions6[j] in list(data3[data3["patient_id"]==patients_filtered4[i]]["operation"]):
			filtered5.append(patients_filtered4[i])
#len(filtered5)
69
len(np.unique(filtered5))
#69
filtered5 = np.unique(filtered5)

patients_filtered5 = np.setdiff1d(patients_filtered4, filtered5, assume_unique=False)
patients_filtered5 = np.unique(patients_filtered5)

len(patients_filtered5)
#200


############
filtered7 = []
for i in range(len(patients_filtered3)):
	for j in range(len(conditions7)):
		if conditions7[j] in list(data3[data3["patient_id"]==patients_filtered3[i]]["operation"]):
			filtered7.append(patients_filtered3[i])

len(filtered7)
#637
len(np.unique(filtered7))
#282
filtered7 = np.unique(filtered7)
patients_filtered7 = np.setdiff1d(patients_filtered3, filtered7, assume_unique=False)
len(patients_filtered7)
#376
len(np.unique(patients_filtered7))
#376
patients_filtered7 = np.unique(patients_filtered7)

############

#>>> len(np.setdiff1d(patients_filtered5, patients_filtered7, assume_unique=False))
#200



data["operation"]=data["code_system"]+data["code"]
data_patients_filtered5 = data[data['patient_id'].isin(patients_filtered5)]
data_patients_filtered7 = data[data['patient_id'].isin(patients_filtered7)]

       
##############
data_patients_filtered5_conditions1 = data_patients_filtered5[data_patients_filtered5['code'].isin(conditions1)]
# data_patients_filtered5_conditions1.shape
# (7479, 11)


procedure = []
procedure_date = []
procedure_patients_filtered5 = data3[data3['patient_id'].isin(patients_filtered5)]
procedure_patients_filtered5_conditions4 = procedure_patients_filtered5[procedure_patients_filtered5['operation'].isin(conditions4)]


#>>> procedure_patients_filtered5_conditions4[procedure_patients_filtered5_conditions4['patient_id']=='owG'][procedure_patients_filtered5_conditions4[procedure_patients_filtered5_conditions4['patient_id']=='owG']['date']==procedure_patients_filtered5_conditions4[procedure_patients_filtered5_conditions4['patient_id']=='owG']['date'].min()]['operation']
#3412    CPT48150
#3413    CPT48153
#Name: operation, dtype: object

for i in range(len(data_patients_filtered5_conditions1)):
        patient_id = data_patients_filtered5_conditions1['patient_id'].iloc[i]
        procedure_date.append(procedure_patients_filtered5_conditions4[procedure_patients_filtered5_conditions4['patient_id']== patient_id]['date'].min())
        procedure.append(list(procedure_patients_filtered5_conditions4[procedure_patients_filtered5_conditions4['patient_id']
                        ==patient_id][procedure_patients_filtered5_conditions4[procedure_patients_filtered5_conditions4['patient_id']
                        ==patient_id]['date']==procedure_patients_filtered5_conditions4[procedure_patients_filtered5_conditions4['patient_id']
                        ==patient_id]['date'].min()]['operation']))
for i in range(len(procedure)):
	procedure[i]='+'.join(np.unique(procedure[i]))
data_patients_filtered5_conditions1['procedure'] = procedure
data_patients_filtered5_conditions1['procedure_date'] = procedure_date



biliary_drainage = []
biliary_drainage_date = []
procedure_patients_filtered5_conditions5 = procedure_patients_filtered5[procedure_patients_filtered5['operation'].isin(conditions5)]

for i in range(len(data_patients_filtered5_conditions1)):
        patient_id = data_patients_filtered5_conditions1['patient_id'].iloc[i]
        biliary_drainage_date.append(procedure_patients_filtered5_conditions5[procedure_patients_filtered5_conditions5['patient_id']== patient_id]['date'].min())
        biliary_drainage.append(list(procedure_patients_filtered5_conditions5[procedure_patients_filtered5_conditions5['patient_id']
                        ==patient_id][procedure_patients_filtered5_conditions5[procedure_patients_filtered5_conditions5['patient_id']
                        ==patient_id]['date']==procedure_patients_filtered5_conditions5[procedure_patients_filtered5_conditions5['patient_id']
                        ==patient_id]['date'].min()]['operation']))
for i in range(len(biliary_drainage)):
	biliary_drainage[i]='+'.join(np.unique(biliary_drainage[i]))
data_patients_filtered5_conditions1['biliary_drainage'] = biliary_drainage
data_patients_filtered5_conditions1['biliary_drainage_date'] = biliary_drainage_date




data4 = pd.read_csv("E:\PDAC study\patient.csv")
data4.drop_duplicates(inplace=True)
sex = []
race = []
data4_patients_filtered5 = data4[data4['patient_id'].isin(patients_filtered5)]
#>>> np.unique(data4_patients_filtered5['patient_id']).shape
#(200,)

for i in range(len(data_patients_filtered5_conditions1)):
        patient_id = data_patients_filtered5_conditions1['patient_id'].iloc[i]
        sex.append(data4_patients_filtered5[data4_patients_filtered5['patient_id']== patient_id]['sex'].iloc[0])
        race.append(data4_patients_filtered5[data4_patients_filtered5['patient_id']== patient_id]['race'].iloc[0])
data_patients_filtered5_conditions1['sex'] = sex
data_patients_filtered5_conditions1['race'] = race



bile_leakage_boolean = []
bile_leakage_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(bile_leakage)]['patient_id']):
		bile_leakage_boolean.append(1)
		bile_leakage_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(bile_leakage))]['date'].min())
	else:
            bile_leakage_boolean.append(0)
            bile_leakage_date.append(0)

data_patients_filtered5_conditions1['bile_leakage'] = pd.to_numeric(bile_leakage_boolean)
data_patients_filtered5_conditions1['bile_leakage_date'] = pd.to_numeric(bile_leakage_date)


Duodenal_anstomosis_stricture_boolean = []
Duodenal_anstomosis_stricture_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(Duodenal_anstomosis_stricture)]['patient_id']):
		Duodenal_anstomosis_stricture_boolean.append(1)
		Duodenal_anstomosis_stricture_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(Duodenal_anstomosis_stricture))]['date'].min())
	else:
            Duodenal_anstomosis_stricture_boolean.append(0)
            Duodenal_anstomosis_stricture_date.append(0)

data_patients_filtered5_conditions1['Duodenal_anstomosis_stricture'] = pd.to_numeric(Duodenal_anstomosis_stricture_boolean)
data_patients_filtered5_conditions1['Duodenal_anstomosis_stricture_date'] = pd.to_numeric(Duodenal_anstomosis_stricture_date)


intra_abdominal_abscess_hematoms_boolean = []
intra_abdominal_abscess_hematoms_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(intra_abdominal_abscess_hematoms)]['patient_id']):
		intra_abdominal_abscess_hematoms_boolean.append(1)
		intra_abdominal_abscess_hematoms_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(intra_abdominal_abscess_hematoms))]['date'].min())
	else:
            intra_abdominal_abscess_hematoms_boolean.append(0)
            intra_abdominal_abscess_hematoms_date.append(0)

data_patients_filtered5_conditions1['intra_abdominal_abscess_hematoms'] = pd.to_numeric(intra_abdominal_abscess_hematoms_boolean)
data_patients_filtered5_conditions1['intra_abdominal_abscess_hematoms_date'] = pd.to_numeric(intra_abdominal_abscess_hematoms_date)



Wound_dehiscence_boolean = []
Wound_dehiscence_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(Wound_dehiscence)]['patient_id']):
		Wound_dehiscence_boolean.append(1)
		Wound_dehiscence_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(Wound_dehiscence))]['date'].min())
	else:
            Wound_dehiscence_boolean.append(0)
            Wound_dehiscence_date.append(0)

data_patients_filtered5_conditions1['Wound_dehiscence'] = pd.to_numeric(Wound_dehiscence_boolean)
data_patients_filtered5_conditions1['Wound_dehiscence_date'] = pd.to_numeric(Wound_dehiscence_date)



pancreatic_fistula_boolean = []
pancreatic_fistula_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(pancreatic_fistula)]['patient_id']):
		pancreatic_fistula_boolean.append(1)
		pancreatic_fistula_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(pancreatic_fistula))]['date'].min())
	else:
            pancreatic_fistula_boolean.append(0)
            pancreatic_fistula_date.append(0)

data_patients_filtered5_conditions1['pancreatic_fistula'] = pd.to_numeric(pancreatic_fistula_boolean)
data_patients_filtered5_conditions1['pancreatic_fistula_date'] = pd.to_numeric(pancreatic_fistula_date)



bile_duct_stricture_boolean = []
bile_duct_stricture_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(bile_duct_stricture)]['patient_id']):
		bile_duct_stricture_boolean.append(1)
		bile_duct_stricture_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(bile_duct_stricture))]['date'].min())
	else:
            bile_duct_stricture_boolean.append(0)
            bile_duct_stricture_date.append(0)

data_patients_filtered5_conditions1['bile_duct_stricture'] = pd.to_numeric(bile_duct_stricture_boolean)
data_patients_filtered5_conditions1['bile_duct_stricture_date'] = pd.to_numeric(bile_duct_stricture_date)



Cjolangitis_boolean = []
Cjolangitis_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(Cjolangitis)]['patient_id']):
		Cjolangitis_boolean.append(1)
		Cjolangitis_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(Cjolangitis))]['date'].min())
	else:
            Cjolangitis_boolean.append(0)
            Cjolangitis_date.append(0)

data_patients_filtered5_conditions1['Cjolangitis'] = pd.to_numeric(Cjolangitis_boolean)
data_patients_filtered5_conditions1['Cjolangitis_date'] = pd.to_numeric(Cjolangitis_date)



acute_pancreatitis_boolean = []
acute_pancreatitis_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(acute_pancreatitis)]['patient_id']):
		acute_pancreatitis_boolean.append(1)
		acute_pancreatitis_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(acute_pancreatitis))]['date'].min())
	else:
            acute_pancreatitis_boolean.append(0)
            acute_pancreatitis_date.append(0)

data_patients_filtered5_conditions1['acute_pancreatitis'] = pd.to_numeric(acute_pancreatitis_boolean)
data_patients_filtered5_conditions1['acute_pancreatitis_date'] = pd.to_numeric(acute_pancreatitis_date)



sepsis_boolean = []
sepsis_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(sepsis)]['patient_id']):
		sepsis_boolean.append(1)
		sepsis_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(sepsis))]['date'].min())
	else:
            sepsis_boolean.append(0)
            sepsis_date.append(0)

data_patients_filtered5_conditions1['sepsis'] = pd.to_numeric(sepsis_boolean)
data_patients_filtered5_conditions1['sepsis_date'] = pd.to_numeric(sepsis_date)




emergency_department_visit_boolean = []
emergency_department_visit_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(emergency_department_visit)]['patient_id']):
		emergency_department_visit_boolean.append(1)
		emergency_department_visit_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(emergency_department_visit))]['date'].min())
	else:
            emergency_department_visit_boolean.append(0)
            emergency_department_visit_date.append(0)

data_patients_filtered5_conditions1['emergency_department_visit'] = pd.to_numeric(emergency_department_visit_boolean)
data_patients_filtered5_conditions1['emergency_department_visit_date'] = pd.to_numeric(emergency_department_visit_date)




All_hospitalization_boolean =[]
All_hospitalization_date =[]
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(All_hospitalization)]['patient_id']):
		All_hospitalization_boolean.append(1)
		All_hospitalization_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(All_hospitalization))]['date'].min())
	else:
            All_hospitalization_boolean.append(0)
            All_hospitalization_date.append(0)

data_patients_filtered5_conditions1['All_hospitalization'] = pd.to_numeric(All_hospitalization_boolean)
data_patients_filtered5_conditions1['All_hospitalization_date'] = pd.to_numeric(All_hospitalization_date)



obstructive_jaundice_boolean = []
obstructive_jaundice_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(obstructive_jaundice)]['patient_id']):
		obstructive_jaundice_boolean.append(1)
		obstructive_jaundice_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(obstructive_jaundice))]['date'].min())
	else:
            obstructive_jaundice_boolean.append(0)
            obstructive_jaundice_date.append(0)

data_patients_filtered5_conditions1['obstructive_jaundice'] = pd.to_numeric(obstructive_jaundice_boolean)
data_patients_filtered5_conditions1['obstructive_jaundice_date'] = pd.to_numeric(obstructive_jaundice_date)




acute_pancreatitis_boolean = []
acute_pancreatitis_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(acute_pancreatitis)]['patient_id']):
		acute_pancreatitis_boolean.append(1)
		acute_pancreatitis_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(acute_pancreatitis))]['date'].min())
	else:
            acute_pancreatitis_boolean.append(0)
            acute_pancreatitis_date.append(0)

data_patients_filtered5_conditions1['acute_pancreatitis'] = pd.to_numeric(acute_pancreatitis_boolean)
data_patients_filtered5_conditions1['acute_pancreatitis_date'] = pd.to_numeric(acute_pancreatitis_date)



liver_cirrhosis_boolean = []
liver_cirrhosis_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(liver_cirrhosis)]['patient_id']):
		liver_cirrhosis_boolean.append(1)
		liver_cirrhosis_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(liver_cirrhosis))]['date'].min())
	else:
            liver_cirrhosis_boolean.append(0)
            liver_cirrhosis_date.append(0)

data_patients_filtered5_conditions1['liver_cirrhosis'] = pd.to_numeric(liver_cirrhosis_boolean)
data_patients_filtered5_conditions1['liver_cirrhosis_date'] = pd.to_numeric(liver_cirrhosis_date)



Hypertension_boolean = []
Hypertension_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(Hypertension)]['patient_id']):
		Hypertension_boolean.append(1)
		Hypertension_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(Hypertension))]['date'].min())
	else:
            Hypertension_boolean.append(0)
            Hypertension_date.append(0)

data_patients_filtered5_conditions1['Hypertension'] = pd.to_numeric(Hypertension_boolean)
data_patients_filtered5_conditions1['Hypertension_date'] = pd.to_numeric(Hypertension_date)



Ischemic_heart_disease_boolean = []
Ischemic_heart_disease_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(Ischemic_heart_disease)]['patient_id']):
		Ischemic_heart_disease_boolean.append(1)
		Ischemic_heart_disease_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(Ischemic_heart_disease))]['date'].min())
	else:
            Ischemic_heart_disease_boolean.append(0)
            Ischemic_heart_disease_date.append(0)

data_patients_filtered5_conditions1['Ischemic_heart_disease'] = pd.to_numeric(Ischemic_heart_disease_boolean)
data_patients_filtered5_conditions1['Ischemic_heart_disease_date'] = pd.to_numeric(Ischemic_heart_disease_date)



Diabetic_mellitus_boolean = []
Diabetic_mellitus_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(Diabetic_mellitus)]['patient_id']):
		Diabetic_mellitus_boolean.append(1)
		Diabetic_mellitus_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(Diabetic_mellitus))]['date'].min())
	else:
            Diabetic_mellitus_boolean.append(0)
            Diabetic_mellitus_date.append(0)

data_patients_filtered5_conditions1['Diabetic_mellitus'] = pd.to_numeric(Diabetic_mellitus_boolean)
data_patients_filtered5_conditions1['Diabetic_mellitus_date'] = pd.to_numeric(Diabetic_mellitus_date)



ASthma_boolean = []
ASthma_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(ASthma)]['patient_id']):
		ASthma_boolean.append(1)
		ASthma_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(ASthma))]['date'].min())
	else:
            ASthma_boolean.append(0)
            ASthma_date.append(0)

data_patients_filtered5_conditions1['ASthma'] = pd.to_numeric(ASthma_boolean)
data_patients_filtered5_conditions1['ASthma_date'] = pd.to_numeric(ASthma_date)



COPD_boolean = []
COPD_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(COPD)]['patient_id']):
		COPD_boolean.append(1)
		COPD_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(COPD))]['date'].min())
	else:
            COPD_boolean.append(0)
            COPD_date.append(0)

data_patients_filtered5_conditions1['COPD'] = pd.to_numeric(COPD_boolean)
data_patients_filtered5_conditions1['COPD_date'] = pd.to_numeric(COPD_date)



CKD_boolean = []
CKD_date = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered5[data_patients_filtered5['operation'].isin(CKD)]['patient_id']):
		CKD_boolean.append(1)
		CKD_date.append(data_patients_filtered5[(data_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i])&(data_patients_filtered5['operation'].isin(CKD))]['date'].min())
	else:
            CKD_boolean.append(0)
            CKD_date.append(0)

data_patients_filtered5_conditions1['CKD'] = pd.to_numeric(CKD_boolean)
data_patients_filtered5_conditions1['CKD_date'] = pd.to_numeric(CKD_date)


###
data5 = pd.read_csv("F:\PDAC study\tumor.csv")
#data5 = pd.read_csv(r"C:\Users\Hsu-Kai\Downloads\PDAC study\tumor.csv")        #https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3
data5.drop_duplicates(inplace=True)
#>>> data5.shape
#(1844, 14)


stage_code = []
tumor_size = []
number_of_lymph_nodes = []
metastatic = []

data5['stage_code'] = data5['stage_code'].fillna('0')
data5['tumor_size'] = data5['tumor_size'].fillna('0')
data5['number_of_lymph_nodes'] = data5['number_of_lymph_nodes'].fillna('0')
data5['metastatic'] = data5['metastatic'].fillna('0')


tumor_patients_filtered5 = data5[data5['patient_id'].isin(patients_filtered5)]
#>>> tumor_patients_filtered5.shape
#(243, 14)

for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered5['patient_id']):
                stage_code.append(list(tumor_patients_filtered5[tumor_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i]]['stage_code']))
	else:
            stage_code.append(str(0))
            
for i in range(len(stage_code)):
	stage_code[i]='/'.join(np.unique(stage_code[i]))
data_patients_filtered5_conditions1['stage_code'] = stage_code



for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered5['patient_id']):
                tumor_size.append(list(tumor_patients_filtered5[tumor_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i]]['tumor_size']))
	else:
            tumor_size.append(str(0))
            
for i in range(len(tumor_size)):
	tumor_size[i]='/'.join(np.unique(tumor_size[i]))
data_patients_filtered5_conditions1['tumor_size'] = tumor_size



for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered5['patient_id']):
                number_of_lymph_nodes.append(list(tumor_patients_filtered5[tumor_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i]]['number_of_lymph_nodes']))
	else:
            number_of_lymph_nodes.append(str(0))
            
for i in range(len(number_of_lymph_nodes)):
	number_of_lymph_nodes[i]='/'.join(np.unique(number_of_lymph_nodes[i]))
data_patients_filtered5_conditions1['number_of_lymph_nodes'] = number_of_lymph_nodes



for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered5['patient_id']):
                metastatic.append(list(tumor_patients_filtered5[tumor_patients_filtered5['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i]]['metastatic']))
	else:
            metastatic.append(str(0))
            
for i in range(len(metastatic)):
	metastatic[i]='/'.join(np.unique(metastatic[i]))
data_patients_filtered5_conditions1['metastatic'] = metastatic





###

month_year_death = []
for i in range(len(data_patients_filtered5_conditions1)):
	if data_patients_filtered5_conditions1['patient_id'].iloc[i] in np.unique(data4['patient_id']):
		try:
			month_year_death.append(int(data4[data4['patient_id']== data_patients_filtered5_conditions1['patient_id'].iloc[i]]['month_year_death']))
		except:
			month_year_death.append(0)

	else:
            month_year_death.append(0)
data_patients_filtered5_conditions1['month_year_death'] = pd.to_numeric(month_year_death)





##############################
data_patients_filtered7_conditions1 = data_patients_filtered7[data_patients_filtered7['code'].isin(conditions1)]
# >>> data_patients_filtered7_conditions1.shape
#(5993, 11)


procedure = []
procedure_date = []
procedure_patients_filtered7 = data3[data3['patient_id'].isin(patients_filtered7)]
procedure_patients_filtered7_conditions4 = procedure_patients_filtered7[procedure_patients_filtered7['operation'].isin(conditions4)]


for i in range(len(data_patients_filtered7_conditions1)):
        patient_id = data_patients_filtered7_conditions1['patient_id'].iloc[i]
        procedure_date.append(procedure_patients_filtered7_conditions4[procedure_patients_filtered7_conditions4['patient_id']== patient_id]['date'].min())
        procedure.append(list(procedure_patients_filtered7_conditions4[procedure_patients_filtered7_conditions4['patient_id']
                        ==patient_id][procedure_patients_filtered7_conditions4[procedure_patients_filtered7_conditions4['patient_id']
                        ==patient_id]['date']==procedure_patients_filtered7_conditions4[procedure_patients_filtered7_conditions4['patient_id']
                        ==patient_id]['date'].min()]['operation']))
for i in range(len(procedure)):
	procedure[i]='+'.join(np.unique(procedure[i]))
data_patients_filtered7_conditions1['procedure'] = procedure
data_patients_filtered7_conditions1['procedure_date'] = procedure_date



sex = []
race = []
data4_patients_filtered7 = data4[data4['patient_id'].isin(patients_filtered7)]

for i in range(len(data_patients_filtered7_conditions1)):
        patient_id = data_patients_filtered7_conditions1['patient_id'].iloc[i]
        sex.append(data4_patients_filtered7[data4_patients_filtered7['patient_id']== patient_id]['sex'].iloc[0])
        race.append(data4_patients_filtered7[data4_patients_filtered7['patient_id']== patient_id]['race'].iloc[0])
data_patients_filtered7_conditions1['sex'] = sex
data_patients_filtered7_conditions1['race'] = race




bile_leakage_boolean = []
bile_leakage_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(bile_leakage)]['patient_id']):
		bile_leakage_boolean.append(1)
		bile_leakage_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(bile_leakage))]['date'].min())
	else:
            bile_leakage_boolean.append(0)
            bile_leakage_date.append(0)

data_patients_filtered7_conditions1['bile_leakage'] = pd.to_numeric(bile_leakage_boolean)
data_patients_filtered7_conditions1['bile_leakage_date'] = pd.to_numeric(bile_leakage_date)


Duodenal_anstomosis_stricture_boolean = []
Duodenal_anstomosis_stricture_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(Duodenal_anstomosis_stricture)]['patient_id']):
		Duodenal_anstomosis_stricture_boolean.append(1)
		Duodenal_anstomosis_stricture_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(Duodenal_anstomosis_stricture))]['date'].min())
	else:
            Duodenal_anstomosis_stricture_boolean.append(0)
            Duodenal_anstomosis_stricture_date.append(0)

data_patients_filtered7_conditions1['Duodenal_anstomosis_stricture'] = pd.to_numeric(Duodenal_anstomosis_stricture_boolean)
data_patients_filtered7_conditions1['Duodenal_anstomosis_stricture_date'] = pd.to_numeric(Duodenal_anstomosis_stricture_date)


intra_abdominal_abscess_hematoms_boolean = []
intra_abdominal_abscess_hematoms_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(intra_abdominal_abscess_hematoms)]['patient_id']):
		intra_abdominal_abscess_hematoms_boolean.append(1)
		intra_abdominal_abscess_hematoms_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(intra_abdominal_abscess_hematoms))]['date'].min())
	else:
            intra_abdominal_abscess_hematoms_boolean.append(0)
            intra_abdominal_abscess_hematoms_date.append(0)

data_patients_filtered7_conditions1['intra_abdominal_abscess_hematoms'] = pd.to_numeric(intra_abdominal_abscess_hematoms_boolean)
data_patients_filtered7_conditions1['intra_abdominal_abscess_hematoms_date'] = pd.to_numeric(intra_abdominal_abscess_hematoms_date)



Wound_dehiscence_boolean = []
Wound_dehiscence_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(Wound_dehiscence)]['patient_id']):
		Wound_dehiscence_boolean.append(1)
		Wound_dehiscence_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(Wound_dehiscence))]['date'].min())
	else:
            Wound_dehiscence_boolean.append(0)
            Wound_dehiscence_date.append(0)

data_patients_filtered7_conditions1['Wound_dehiscence'] = pd.to_numeric(Wound_dehiscence_boolean)
data_patients_filtered7_conditions1['Wound_dehiscence_date'] = pd.to_numeric(Wound_dehiscence_date)



pancreatic_fistula_boolean = []
pancreatic_fistula_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(pancreatic_fistula)]['patient_id']):
		pancreatic_fistula_boolean.append(1)
		pancreatic_fistula_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(pancreatic_fistula))]['date'].min())
	else:
            pancreatic_fistula_boolean.append(0)
            pancreatic_fistula_date.append(0)

data_patients_filtered7_conditions1['pancreatic_fistula'] = pd.to_numeric(pancreatic_fistula_boolean)
data_patients_filtered7_conditions1['pancreatic_fistula_date'] = pd.to_numeric(pancreatic_fistula_date)



bile_duct_stricture_boolean = []
bile_duct_stricture_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(bile_duct_stricture)]['patient_id']):
		bile_duct_stricture_boolean.append(1)
		bile_duct_stricture_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(bile_duct_stricture))]['date'].min())
	else:
            bile_duct_stricture_boolean.append(0)
            bile_duct_stricture_date.append(0)

data_patients_filtered7_conditions1['bile_duct_stricture'] = pd.to_numeric(bile_duct_stricture_boolean)
data_patients_filtered7_conditions1['bile_duct_stricture_date'] = pd.to_numeric(bile_duct_stricture_date)



Cjolangitis_boolean = []
Cjolangitis_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(Cjolangitis)]['patient_id']):
		Cjolangitis_boolean.append(1)
		Cjolangitis_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(Cjolangitis))]['date'].min())
	else:
            Cjolangitis_boolean.append(0)
            Cjolangitis_date.append(0)

data_patients_filtered7_conditions1['Cjolangitis'] = pd.to_numeric(Cjolangitis_boolean)
data_patients_filtered7_conditions1['Cjolangitis_date'] = pd.to_numeric(Cjolangitis_date)



acute_pancreatitis_boolean = []
acute_pancreatitis_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(acute_pancreatitis)]['patient_id']):
		acute_pancreatitis_boolean.append(1)
		acute_pancreatitis_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(acute_pancreatitis))]['date'].min())
	else:
            acute_pancreatitis_boolean.append(0)
            acute_pancreatitis_date.append(0)

data_patients_filtered7_conditions1['acute_pancreatitis'] = pd.to_numeric(acute_pancreatitis_boolean)
data_patients_filtered7_conditions1['acute_pancreatitis_date'] = pd.to_numeric(acute_pancreatitis_date)



sepsis_boolean = []
sepsis_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(sepsis)]['patient_id']):
		sepsis_boolean.append(1)
		sepsis_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(sepsis))]['date'].min())
	else:
            sepsis_boolean.append(0)
            sepsis_date.append(0)

data_patients_filtered7_conditions1['sepsis'] = pd.to_numeric(sepsis_boolean)
data_patients_filtered7_conditions1['sepsis_date'] = pd.to_numeric(sepsis_date)




emergency_department_visit_boolean = []
emergency_department_visit_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(emergency_department_visit)]['patient_id']):
		emergency_department_visit_boolean.append(1)
		emergency_department_visit_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(emergency_department_visit))]['date'].min())
	else:
            emergency_department_visit_boolean.append(0)
            emergency_department_visit_date.append(0)

data_patients_filtered7_conditions1['emergency_department_visit'] = pd.to_numeric(emergency_department_visit_boolean)
data_patients_filtered7_conditions1['emergency_department_visit_date'] = pd.to_numeric(emergency_department_visit_date)




All_hospitalization_boolean =[]
All_hospitalization_date =[]
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(All_hospitalization)]['patient_id']):
		All_hospitalization_boolean.append(1)
		All_hospitalization_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(All_hospitalization))]['date'].min())
	else:
            All_hospitalization_boolean.append(0)
            All_hospitalization_date.append(0)

data_patients_filtered7_conditions1['All_hospitalization'] = pd.to_numeric(All_hospitalization_boolean)
data_patients_filtered7_conditions1['All_hospitalization_date'] = pd.to_numeric(All_hospitalization_date)



obstructive_jaundice_boolean = []
obstructive_jaundice_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(obstructive_jaundice)]['patient_id']):
		obstructive_jaundice_boolean.append(1)
		obstructive_jaundice_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(obstructive_jaundice))]['date'].min())
	else:
            obstructive_jaundice_boolean.append(0)
            obstructive_jaundice_date.append(0)

data_patients_filtered7_conditions1['obstructive_jaundice'] = pd.to_numeric(obstructive_jaundice_boolean)
data_patients_filtered7_conditions1['obstructive_jaundice_date'] = pd.to_numeric(obstructive_jaundice_date)




acute_pancreatitis_boolean = []
acute_pancreatitis_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(acute_pancreatitis)]['patient_id']):
		acute_pancreatitis_boolean.append(1)
		acute_pancreatitis_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(acute_pancreatitis))]['date'].min())
	else:
            acute_pancreatitis_boolean.append(0)
            acute_pancreatitis_date.append(0)

data_patients_filtered7_conditions1['acute_pancreatitis'] = pd.to_numeric(acute_pancreatitis_boolean)
data_patients_filtered7_conditions1['acute_pancreatitis_date'] = pd.to_numeric(acute_pancreatitis_date)



liver_cirrhosis_boolean = []
liver_cirrhosis_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(liver_cirrhosis)]['patient_id']):
		liver_cirrhosis_boolean.append(1)
		liver_cirrhosis_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(liver_cirrhosis))]['date'].min())
	else:
            liver_cirrhosis_boolean.append(0)
            liver_cirrhosis_date.append(0)

data_patients_filtered7_conditions1['liver_cirrhosis'] = pd.to_numeric(liver_cirrhosis_boolean)
data_patients_filtered7_conditions1['liver_cirrhosis_date'] = pd.to_numeric(liver_cirrhosis_date)



Hypertension_boolean = []
Hypertension_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(Hypertension)]['patient_id']):
		Hypertension_boolean.append(1)
		Hypertension_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(Hypertension))]['date'].min())
	else:
            Hypertension_boolean.append(0)
            Hypertension_date.append(0)

data_patients_filtered7_conditions1['Hypertension'] = pd.to_numeric(Hypertension_boolean)
data_patients_filtered7_conditions1['Hypertension_date'] = pd.to_numeric(Hypertension_date)



Ischemic_heart_disease_boolean = []
Ischemic_heart_disease_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(Ischemic_heart_disease)]['patient_id']):
		Ischemic_heart_disease_boolean.append(1)
		Ischemic_heart_disease_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(Ischemic_heart_disease))]['date'].min())
	else:
            Ischemic_heart_disease_boolean.append(0)
            Ischemic_heart_disease_date.append(0)

data_patients_filtered7_conditions1['Ischemic_heart_disease'] = pd.to_numeric(Ischemic_heart_disease_boolean)
data_patients_filtered7_conditions1['Ischemic_heart_disease_date'] = pd.to_numeric(Ischemic_heart_disease_date)



Diabetic_mellitus_boolean = []
Diabetic_mellitus_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(Diabetic_mellitus)]['patient_id']):
		Diabetic_mellitus_boolean.append(1)
		Diabetic_mellitus_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(Diabetic_mellitus))]['date'].min())
	else:
            Diabetic_mellitus_boolean.append(0)
            Diabetic_mellitus_date.append(0)

data_patients_filtered7_conditions1['Diabetic_mellitus'] = pd.to_numeric(Diabetic_mellitus_boolean)
data_patients_filtered7_conditions1['Diabetic_mellitus_date'] = pd.to_numeric(Diabetic_mellitus_date)



ASthma_boolean = []
ASthma_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(ASthma)]['patient_id']):
		ASthma_boolean.append(1)
		ASthma_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(ASthma))]['date'].min())
	else:
            ASthma_boolean.append(0)
            ASthma_date.append(0)

data_patients_filtered7_conditions1['ASthma'] = pd.to_numeric(ASthma_boolean)
data_patients_filtered7_conditions1['ASthma_date'] = pd.to_numeric(ASthma_date)



COPD_boolean = []
COPD_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(COPD)]['patient_id']):
		COPD_boolean.append(1)
		COPD_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(COPD))]['date'].min())
	else:
            COPD_boolean.append(0)
            COPD_date.append(0)

data_patients_filtered7_conditions1['COPD'] = pd.to_numeric(COPD_boolean)
data_patients_filtered7_conditions1['COPD_date'] = pd.to_numeric(COPD_date)



CKD_boolean = []
CKD_date = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data_patients_filtered7[data_patients_filtered7['operation'].isin(CKD)]['patient_id']):
		CKD_boolean.append(1)
		CKD_date.append(data_patients_filtered7[(data_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i])&(data_patients_filtered7['operation'].isin(CKD))]['date'].min())
	else:
            CKD_boolean.append(0)
            CKD_date.append(0)

data_patients_filtered7_conditions1['CKD'] = pd.to_numeric(CKD_boolean)
data_patients_filtered7_conditions1['CKD_date'] = pd.to_numeric(CKD_date)

###
stage_code = []
tumor_size = []
number_of_lymph_nodes = []
metastatic = []

data5['stage_code'] = data5['stage_code'].fillna('0')
data5['tumor_size'] = data5['tumor_size'].fillna('0')
data5['number_of_lymph_nodes'] = data5['number_of_lymph_nodes'].fillna('0')
data5['metastatic'] = data5['metastatic'].fillna('0')


tumor_patients_filtered7 = data5[data5['patient_id'].isin(patients_filtered7)]

for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered7['patient_id']):
                stage_code.append(list(tumor_patients_filtered7[tumor_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i]]['stage_code']))
	else:
            stage_code.append(str(0))
            
for i in range(len(stage_code)):
	stage_code[i]='/'.join(np.unique(stage_code[i]))
data_patients_filtered7_conditions1['stage_code'] = stage_code



for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered7['patient_id']):
                tumor_size.append(list(tumor_patients_filtered7[tumor_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i]]['tumor_size']))
	else:
            tumor_size.append(str(0))
            
for i in range(len(tumor_size)):
	tumor_size[i]='/'.join(np.unique(tumor_size[i]))
data_patients_filtered7_conditions1['tumor_size'] = tumor_size



for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered7['patient_id']):
                number_of_lymph_nodes.append(list(tumor_patients_filtered7[tumor_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i]]['number_of_lymph_nodes']))
	else:
            number_of_lymph_nodes.append(str(0))
            
for i in range(len(number_of_lymph_nodes)):
	number_of_lymph_nodes[i]='/'.join(np.unique(number_of_lymph_nodes[i]))
data_patients_filtered7_conditions1['number_of_lymph_nodes'] = number_of_lymph_nodes



for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(tumor_patients_filtered7['patient_id']):
                metastatic.append(list(tumor_patients_filtered7[tumor_patients_filtered7['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i]]['metastatic']))
	else:
            metastatic.append(str(0))
            
for i in range(len(metastatic)):
	metastatic[i]='/'.join(np.unique(metastatic[i]))
data_patients_filtered7_conditions1['metastatic'] = metastatic



##############
data4 = pd.read_csv("E:\PDAC study\patient.csv")
data4.drop_duplicates(inplace=True)


month_year_death = []
for i in range(len(data_patients_filtered7_conditions1)):
	if data_patients_filtered7_conditions1['patient_id'].iloc[i] in np.unique(data4['patient_id']):
		try:
			month_year_death.append(int(data4[data4['patient_id']== data_patients_filtered7_conditions1['patient_id'].iloc[i]]['month_year_death']))
		except:
			month_year_death.append(0)

	else:
            month_year_death.append(0)
data_patients_filtered7_conditions1['month_year_death'] = pd.to_numeric(month_year_death)


            
##############
data_patients_filtered5 = data[data['patient_id'].isin(patients_filtered5)]
data_patients_filtered7 = data[data['patient_id'].isin(patients_filtered7)]


#data_patients_filtered5[data_patients_filtered5['code'].isin(conditions1)].to_csv("E:\PDAC study\patients_filtered5.csv")
#data_patients_filtered7[data_patients_filtered7['code'].isin(conditions1)].to_csv("E:\PDAC study\patients_filtered7.csv")


data_patients_filtered5_conditions1.to_csv("E:\PDAC study\data_patients_filtered5_conditions1.csv")
data_patients_filtered7_conditions1.to_csv("E:\PDAC study\data_patients_filtered7_conditions1.csv")

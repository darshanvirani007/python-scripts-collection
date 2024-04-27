import os
import pandas as pd
import re
from PyPDF2 import PdfReader
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Positive and negative symptoms lists
positive_symptoms = [
    "Further evaluation recommended for detected polyp.",
    "Mild inflammation noted, likely due to diverticulosis.",
    "Polyp removed and submitted for histopathological examination.",
    "Biopsy specimens obtained for further analysis.",
    "Follow-up colonoscopy recommended based on clinical findings.",
    "Biopsies taken from suspicious areas for pathological assessment.",
    "Polyp resected completely, no residual tissue observed.",
    "Polypoid lesions excised completely, no residual tissue present.",
    "Tissue samples collected for histological analysis.",
    "Tissue samples sent for pathological examination.",
    "Results pending",
    "No evidence of active bleeding or vascular abnormalities seen.",
    "No evidence of active inflammation or other acute abnormalities seen.",
    "No significant deviations from expected findings, no further intervention required.",
    "Polyps removed successfully, no complications encountered during the procedure.",
    "No concerning features noted, patient advised to maintain regular follow-up appointments.",
    "Colonoscopy results within expected range, no significant abnormalities detected.",
    "Tissue samples obtained for pathological assessment, results pending.",
    "Colonoscopy results within normal limits, no worrisome findings detected.",
    "Normal post-procedure impression, patient discharged home.",
    "No significant pathology identified, routine follow-up recommended.",
    "Impression unchanged from previous exams, no new concerns.",
    "Colonoscopy findings stable, no evidence of disease recurrence.",
    "Impression benign, no indication of significant mucosal abnormalities.",
    "No concerning lesions identified, patient advised to continue regular care.",
    "No need for immediate intervention, plan for routine follow-up.",
    "Impression normal, no evidence of significant colonic disease.",
    "Colonoscopy findings unremarkable, no new abnormalities detected.",
    "No features concerning for high-grade dysplasia or malignancy.",
    "Polyps removed completely, no residual adenomas visualized.",
    "No signs of procedural complications observed.",
    "Impression consistent with benign colorectal findings.",
    "Colonoscopy results negative for significant pathology.",
    "Findings consistent with normal colonic mucosa.",
    "No significant deviations from expected findings, no further intervention required.",
    "Polyps removed successfully, no complications encountered during the procedure.",
    "No concerning features noted, patient advised to maintain regular follow-up appointments.",
    "Colonoscopy results within expected range, no significant abnormalities detected.",
    "No evidence of dysplasia or malignancy, patient advised to continue surveillance as scheduled."
]

negative_symptoms = [
    "No significant abnormalities detected.",
    "Normal colonoscopy findings, no further action required.",
    "Impression consistent with routine colonoscopic examination.",
    "No concerning pathology identified, follow-up not necessary.",
    "Benign findings observed, no need for additional intervention.",
    "Colonoscopy results negative for significant abnormalities.",
    "No evidence of malignancy detected, routine surveillance recommended.",
    "No concerning features identified, ongoing surveillance advised.",
    "No acute abnormalities detected, continue with standard care.",
    "Normal post-procedure impression, no complications identified.",
    "Impression consistent with expected post-procedure course.",
    "No suspicious lesions seen, regular screening advised.",
    "No pathology requiring immediate attention identified.",
    "Colonoscopy results reassuring, no further action needed.",
    "No concerning features noted, plan for routine follow-up.",
    "No acute abnormalities seen, continue with standard follow-up.",
    "Impression normal, no pathology requiring further investigation.",
    "Colonoscopy results negative for high-risk lesions.",
    "No need for immediate intervention, continue with standard care.",
    "Impression unremarkable, no need for immediate intervention.",
    "No evidence of inflammatory bowel disease detected.",
    "Impression unchanged from prior examinations, no new pathology identified.",
    "No evidence of dysplasia or carcinoma detected.",
    "No evidence of ischemia or vascular abnormalities detected.",
    "Impression benign, no indication of significant pathology.",
    "No features suggestive of advanced neoplasia seen.",
    "No evidence of dysplasia or malignancy, continue with regular surveillance.",
    "Normal post-procedure impression, patient can resume normal activities.",
    "No features suggestive of advanced neoplasia seen.",
    "No evidence of malignancy or dysplasia, continue with routine surveillance.",
    "Normal post-procedure impression, patient discharged home.",
    "No significant pathology identified, routine follow-up recommended.",
    "Impression unchanged from previous exams, no new concerns.",
    "Colonoscopy findings stable, no evidence of disease recurrence.",
    "No features suggestive of infectious colitis or other acute pathology.",
    "Impression benign, no indication of significant mucosal abnormalities.",
    "Colonoscopy results consistent with expected post-procedure course.",
    "No concerning lesions identified, patient advised to continue regular care.",
    "No need for immediate intervention, plan for routine follow-up.",
    "Impression normal, no evidence of significant colonic disease.",
    "Colonoscopy findings unremarkable, no evidence of disease progression.",
    "No features concerning for malignancy detected.",
    "Polyps removed with clear margins, no residual adenomatous tissue.",
    "No signs of acute complications following the procedure.",
    "Impression consistent with benign colorectal changes.",
    "Colonoscopy results negative for advanced neoplasia.",
    "No evidence of active bleeding or vascular abnormalities seen.",
    "Findings consistent with benign mucosal changes.",
    "No significant deviations from expected findings, no further action needed.",
    "Polyps removed successfully, no complications encountered.",
    "No concerning features noted, continue with regular monitoring.",
    "Tissue samples sent for pathological examination.",
    "Colonoscopy results within normal limits, no worrisome findings detected.",
    "No evidence of malignancy or dysplasia, continue with routine surveillance.",
    "Normal post-procedure impression, patient discharged home.",
    "No significant pathology identified, routine follow-up recommended.",
    "Impression unchanged from previous exams, no new concerns.",
    "Colonoscopy findings stable, no evidence of disease recurrence.",
    "No features suggestive of infectious colitis or other acute pathology.",
    "Impression benign, no indication of significant mucosal abnormalities."
]

# Function to classify report as normal or abnormal
def classify_report(report_text):
    if any(symptom in report_text for symptom in positive_symptoms):
        return "Positive Symptoms"
    elif any(symptom in report_text for symptom in negative_symptoms):
        return "Negative Symptoms"
    else:
        return "Unknown"

# Function to extract patient name from report text
def extract_patient_name(report_text, pdf_filename):
    # Search for patterns indicating patient's name
    name_pattern = re.compile(r'Name:\s*([A-Za-z]+\s+[A-Za-z]+)', re.IGNORECASE)
    match = name_pattern.search(report_text)
    if match:
        return match.group(1)
    else:
        # If patient name couldn't be extracted from report text, use PDF filename
        return os.path.splitext(pdf_filename)[0]

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as f:
            pdf_reader = PdfReader(f)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error occurred while processing {pdf_path}: {e}")
    return text

# Read reports from directory
reports_directory = "C:\\Users\\Admin\\Desktop\\Medical Reports"
reports = []
for filename in os.listdir(reports_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(reports_directory, filename)
        report_text = extract_text_from_pdf(pdf_path)
        patient_name = extract_patient_name(report_text, filename)
        label = classify_report(report_text)
        reports.append((patient_name, report_text, label))

# Create DataFrame
df = pd.DataFrame(reports, columns=["PatientName", "ReportText", "Label"])

# Export results to Excel
df.to_excel("classification_results.xlsx", index=False)
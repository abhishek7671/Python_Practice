import os
import base64
import datetime
import time
import pandas as pd
import re

def extract_current_title_and_company(resume_content):
    title_pattern = re.compile(r'Current\s*Title\s*:\s*(.*?)\s', re.IGNORECASE)
    company_pattern = re.compile(r'Current\s*Company\s*:\s*(.*?)\s', re.IGNORECASE)
    
    title_match = re.search(title_pattern, resume_content)
    company_match = re.search(company_pattern, resume_content)
    
    current_title = title_match.group(1) if title_match else None
    current_company = company_match.group(1) if company_match else None
    
    return current_title, current_company

def main(resume_folder, job_folder, jd_input, experience, mandatory_skills, secondary_skills):
    '''
    Author: XYZ
    Description: This function call necessary functions and will score each resume one by one.
    input to this function comes from API and will provide appropriate response back.
    '''
    # Existing code...
    resp = process_file(org_input_file, job_folder, jd_input, experience, mandatory_skills, secondary_skills)
    
    if resp is not None:
        resp['Current_Title'] = ''
        resp['Current_Company'] = ''
        
        for i, row in resp.iterrows():
            current_title, current_company = extract_current_title_and_company(row['Candidate'])
            resp.at[i, 'Current_Title'] = current_title
            resp.at[i, 'Current_Company'] = current_company
    
    return resp


def bg_process(req_data):
    try:
        start = time.time()
        today = datetime.datetime.now()
        start_time = today.strftime("%m-%d-%Y %I:%M:%S %p")
        job_folder = 'file'
        jd_input = ''
        resume_folder = req_data["resume_folder"]
 
        enc_files = req_data['resfile']
        enc_file_names = resume_folder
 
        files = []
        org_input_file = []
        dec_file_data = None
        for i in range(0, len(enc_file_names)):
            dec_file_data = base64.b64decode((enc_files[i].split('base64,')[-1]))
            if enc_file_names[i].startswith('~$'):
                pass
            else:
                org_input_file.append(enc_file_names[i])
                file = open(os.path.join(cf.Resumes_File_Path, enc_file_names[i]), 'wb')
                file.write(dec_file_data)
                file.close()
                files.append(file)
 
        mandatory_skills = ','.join(req_data['mandatory_skills'])  
        secondary_skills = ','.join(req_data['secondary_skills'])  
        experience = req_data['experience']
        job_input = req_data.get('job_input', '')
        jd_input = req_data.get('jd_input', '')  
 
        resp, entry_time, exit_time = process_file(org_input_file, job_folder, jd_input, experience, mandatory_skills, secondary_skills)
        module_run_time = exit_time - entry_time
        overall_end_time = time.time() - start
 
        if not resp.empty:
            resp['Total_exp_cal'] = ''
            resp['Total_Exp_With_Years_lst'] = ''
            for i in range(len(resp)):
                if type(resp['Total_Exp_With_Years'][i]) == "NA":  
                    resp['Total_exp_cal'][i] = "NA"
                elif type(resp['Total_Exp_With_Years'][i]) == list:
                    resp['Total_exp_cal'][i] = resp['Total_Exp_With_Years'][i][0]
                else:
                    print("........................entered into else condition")
                    resp['Total_exp_cal'][i] = 'NA'
 
            # Calculate Low_Skill_Recency
            jd_mandatory_skills = resp['JD_Mandatory_skills'].str.split(',').fillna('')
            jd_secondary_skills = resp['JD_Secondary_skills'].str.split(',').fillna('')
            combined_skills = jd_mandatory_skills + jd_secondary_skills
            low_skill_recency = combined_skills.apply(lambda x: ','.join(x)).str.upper()
            resp['Low_Skill_Recency'] = low_skill_recency
 
            if resp['JD_Mandatory_skills'][0] == '':
                jd_man_skill_count = 0
            else:
                jd_man_skill_count = len(resp['JD_Mandatory_skills'][0].split(','))
            if resp['JD_Secondary_skills'][0] == '':
                jd_sec_skill_count = 0
            else:
                jd_sec_skill_count = len(resp['JD_Secondary_skills'][0].split(','))
            resp['mandatory_skill_score'] = resp['Mandatory_Skills_Score'].apply(
                lambda x: str(int(round(x * jd_man_skill_count, 0))) + "/" + str(jd_man_skill_count))
            resp['secondary_skill_score'] = resp['Secondary_Skills_Score'].apply(
                lambda x: str(int(round(x * jd_sec_skill_count, 0))) + "/" + str(jd_sec_skill_count))
            resp['JD_Rel_Res_Skills'] = resp['JD_Rel_Res_Skills'].str.upper()
 
            resp['Candidate'] = resp['Candidate'].apply(extract_candidate_name)
            resp['name']
        
        if resp is not None:
            for result in resp['result']:
                result['Current_Title'] = ''
                result['Current_Company'] = ''
                
                current_title, current_company = extract_current_title_and_company(result['Candidate'])
                result['Current_Title'] = current_title
                result['Current_Company'] = current_company

        return resp

    except Exception as e:
        # Handle exceptions

# Call bg_process or main function as needed based on your application's flow

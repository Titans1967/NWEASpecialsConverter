import csv
import paramiko
import os
with open('specials.csv','w',newline='') as output:
    spamwriter = csv.writer(output,delimiter=',')
    spamwriter.writerow(['Student ID','Program Name'])
    with open('SpecialsRaw.csv','r') as csvFile:
        specials = csv.DictReader(csvFile)
        for row in specials:
            rowContent = []
            if row['English Language Learner (ELL)'] == 'Yes':
                rowContent.append('English Language Learner (ELL)')
            if row['Title 1'] ==  'Yes':
                rowContent.append('Title I')
            if row['Talented and Gifted'] == 'Yes':
                rowContent.append('Talented and Gifted')
            if row['Section 504'] == 'Yes':
                rowContent.append('Section 504')
            if row['Special Education (SPED)'] == 'Yes':
                rowContent.append('Special Education (SPED)')
            if row['RTI'] != 'N':
                rowContent.append('RTI')
            if row['Free and Reduced Lunch (FRL)'] == '01':
                rowContent.append('Free and Reduced Lunch (FRL)')
            if row['Dist Cat Codes'] == 'DYS':
                rowContent.append('Dyslexia')
            string = ",".join(rowContent)
            spamwriter.writerow([row['Student ID'],string])
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='[ORGANIZATION].oneroster.com',username='BADPRACTICE',password='STOPDOINGTHIS')
sftp_client = ssh.open_sftp()
sftp_client.chdir(r'/DailyImport')
sftp_client.put('specials.csv',r'/DailyImport/specials.csv')
ssh.close()

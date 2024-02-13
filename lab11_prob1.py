"""
CISC 131 Problem 1 - Andrew Schmaderer (schm4013) - Tutor: Bach Dam
"""


def main():
    filename = readCsv("C:\\Users\\andre\\OneDrive - University of " +
                       "St. Thomas\\CISC 131-OSS429-04\\Lab\\Lab 11\\people.csv")
    print(filename)

def readCsv(filename):
    with open (filename, 'r', encoding='utf-8') as file:
        alines = file.readlines()
        headers = alines[0].strip()
        headers = headers.split(',')
        data = []
        for j in range(1, len(alines)):
            line = alines[j]
            line = line.strip()
            value = line.split(",")
            row = {}
            for i in range(len(value)):
                row[headers[i]] = value[i]
            data.append(row)
    file.close()
    return data

def filterOverallGpa(applicants, top_n):
    for i in range(len(applicants)-1):
        for j in range(i+1, len(applicants)):
            if applicants[j]["overall_gpa"] > applicants[i]["overall_gpa"]:
                tmp = applicants[i]
                applicants[i] = applicants[j]
                applicants[j] = tmp
    x = applicants[0:top_n]
    return x
def filterMajorGpa(applicants, top_n):
    for i in range(len(applicants)-1):
        for j in range(i+1, len(applicants)):
            if applicants[j]["major_gpa"] > applicants[i]["major_gpa"]:
                tmp = applicants[i]
                applicants[i] = applicants[j]
                applicants[j] = tmp
    x = applicants[0:top_n]
    return x
def filterCustomScore(applicants, top_n):
    for i in applicants:
        i["score"] = (10 * float(i["advanced_gpa"]) + (8 * float(i["intermediate_gpa"]))
                      + 6 * float(i["intro_gpa"]) + 4 * float(i["overall_gpa"])
                      + (.25 * float(i["years_experience"])))
    for i in range(len(applicants)-1):
        for j in range(i+1, len(applicants)):
            if applicants[j]["score"] > applicants[i]["score"]:
                tmp = applicants[i]
                applicants[i] = applicants[j]
                applicants[j] = tmp
    x = applicants[0:top_n]
    return x
main()

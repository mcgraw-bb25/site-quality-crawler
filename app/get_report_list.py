import os

def get_report_list():
    ''' creates reports to show user '''
    curpath = os.getcwd()
    newpath = curpath + '/reports/'

    report_list = []

    for report in os.listdir(newpath):
        if report.startswith('site_report-') and report.endswith('.json'):
            # print (report)
            report_list.append(report)

    return report_list

if __name__ == "__main__":
    pass
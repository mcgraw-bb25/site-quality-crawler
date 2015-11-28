import os


def get_report_list():
    ''' lists all site reports in the reports directory '''
    report_list = []

    for report in os.listdir(os.getcwd() + '/reports/'):
        if report.startswith('site_report-') and report.endswith('.json'):
            report_list.append(report)

    return report_list

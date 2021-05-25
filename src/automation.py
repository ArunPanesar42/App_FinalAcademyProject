from config_manager import itjobswatch_home_page_url
from src.itjobswatch_html_readers.itjobswatch_home_page_top_30 import ItJobsWatchHomePageTop30
from src.csv_generators.top_30_csv_generator import Top30CSVGenerator
import os
import boto3
bucket_name = 'eng84-final-project'
file_name = 'ItJobsWatchTop30.csv'


class Automation:

    def __init__(self):
        # Comment one of these out depending on if headings are wanted
        #self.run_automation_head_none()
        self.run_automation_head()
        self.upload_s3()

    def run_automation_head_none(self):
        Top30CSVGenerator().generate_top_30_csv(ItJobsWatchHomePageTop30(itjobswatch_home_page_url()).get_top_30_table_elements_into_array())
        print('Please check your downloads folder')

    def run_automation_head(self):
        top_30 = ItJobsWatchHomePageTop30(itjobswatch_home_page_url())
        Top30CSVGenerator().generate_top_30_csv(top_30.get_top_30_table_elements_into_array(), os.path.expanduser('~/Downloads/'), 'ItJobsWatchTop30.csv', top_30.get_table_headers_array())
        print('Please check your downloads folder')

    def upload_s3(self):
        region = "eu-west-1"
        file = open("credentials.cfg")
        awsKey = file.readline().strip("\n")
        secretKey = file.readline().strip("\n")

        s3 = boto3.client('s3',
                          region_name=region,
                          aws_access_key_id=awsKey,
                          aws_secret_access_key=secretKey)

        s3.upload_file(os.path.expanduser('~/Downloads/')+file_name, bucket_name, file_name)

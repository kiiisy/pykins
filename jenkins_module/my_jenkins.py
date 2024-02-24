import xml.etree.ElementTree as ET
import jenkins

JENKINS_URL = ''
API_KEY = ''
USER_NAME = ''
BASE_JOB_NAME = ''

class MyJenkins():

    def __init__(self) -> None:
        self.server = jenkins.Jenkins(JENKINS_URL, username=USER_NAME, password=API_KEY)
        self.user = self.__server.get_whoami()
        self.base_job_config = self.server.get_job_config(BASE_JOB_NAME)
        self.new_job_config = ''

    def create(self, job_name, job_desc, git_url, git_branch,
               teams_url, target_folder,
               is_sun, is_mon, is_tue, is_wed, is_thu, is_fri, is_sat,
               build_time) -> None:
        base_job_config = self.base_job_config
        self.edit(base_job_config)
        self.server.create_job(job_name, base_job_config)
        print(job_name)

    def recreate(self) -> None:
        pass

    def edit(self, config) -> None:
        root = ET.fromstring(config)
        for elem in root.findall('./description'):
            elem.text = 'from python'
        self.new_job_config = ET.tostring(root, encoding='utf-8').decode('utf-8')

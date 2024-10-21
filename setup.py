from setuptools import setup, find_packages
from typing import List


hypen_e_dot = '-e .'
def get_requirments(file_path: str) -> List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n', '') for req in requirments]

        if hypen_e_dot in requirments:
            requirments.remove(hypen_e_dot)
        
        return requirments




setup(
    name='MLproject',                  # Name of your project
    version='0.1',                      # Version of your project
    packages=find_packages(), # Tells where to find the code (in the src folder)
    install_requires=get_requirments('requirments.txt'),
    author='Yuvraj',                # Your name
    author_email='yuvrajmehta00@gmail.com', # Your email
    description='End to end ML project.', # What your project does
   
)
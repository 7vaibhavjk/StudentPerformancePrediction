from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()


setup(
    name='StudentPerformancePrediction',
    version='0.0.1',
    author='Vaibhav',
    author_email='7vaibhavjk@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
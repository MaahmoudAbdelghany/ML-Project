from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requierments(file_path:str) -> List[str] :
    '''
    this function will return the list of requierments
    '''
    requierments= []
    with open(file_path) as file_obj :
        requierments = file_obj.readlines()
        requierments =[req.replace("\n","" ) for req in requierments]

    if HYPEN_E_DOT in requierments :
        requierments.remove(HYPEN_E_DOT)


setup(

    name="mlproject",
    version="0.0.1",
    author="Mahmoud Abdelghany",
    author_email="sadimabdelghany@gmail.com",
    packages=find_packages(), 
    install_requiers=get_requierments('requierments.txt')
    
)


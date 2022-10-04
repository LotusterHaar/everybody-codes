from typing import List
import csv
from domain.camera import Camera
from domain.camera_repository import CameraRepository
import re
from copy import deepcopy

class InMemoryCameraRepository(CameraRepository):
    def __init__(self):
        self.cameras = []
        self.readCSV()
        
    
    def extract_id(self, camera):
        #use regular expression to extract id in numbers from the camera name string
        # throw an exception if the identifier doesnt start with the right code
       
        index = [int(s) for s in re.findall(r'\d+', camera.get('Camera'))] 
    
        assert(not camera.get('Camera').startswith('UTR-CM-'), "f,Camera Identifier is not valid")
         
        return index[0]
    
    def filter_on_id(self, id):
        for camera in self.cameras:
            if 'Camera' in camera:
                if camera.get('Camera').startswith('UTR-CM-'+str(id)):
                    return camera

    def readCSV(self):
        with open(r'C:\everybody-codes\app\adapter\cameras-defb.csv') as f:
            reader = csv.DictReader(f, delimiter=";")
            for cols in reader:
                if cols.get('Camera'):
                        camera = deepcopy(cols)
                        camera['Camera_Id'] =  self.extract_id(cols)
                        self.cameras.append(camera)
                        
    def get_camera(self, id:int) -> Camera:
        return self.filter_on_id(id)
    

    def add_camera(self, camera: Camera) -> Camera:
        self.cameras.append(camera)
        return camera
    
    def search_cameras(self, keyword: str) -> List[Camera]:
        found_cameras = []
        #Open the CSV file with locations of the camera, and find location on name
        
        for item in self.cameras:
            if item.get('Camera'):
                if keyword in item['Camera']:
                    found_cameras.append(item)
        print(found_cameras)
        return found_cameras
                     
    def all_cameras(self) -> List[Camera]:
        return self.cameras

    def count_cameras(self) -> int:
        return len(self.cameras)
    
   
    
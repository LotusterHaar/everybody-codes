import inject

from domain.camera import Camera
from domain.database_interface import CameraRepository

class getCamera:
    def __init__(self, csv: CSVInterface):
        self.__database = database

    def execute(self, camera_id: int) -> Camera:
        return self.__csv.get_Camera(camera_id)
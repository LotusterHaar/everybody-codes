from  abc import ABC, abstractmethod
from typing import Optional, List

from domain.camera import Camera

class CameraRepository(ABC):
    @abstractmethod
    def get_camera(self, camera_id:int) -> Camera:
        pass
    
    @abstractmethod
    def all_cameras(self) -> List[Camera]:
        pass
    
    @abstractmethod
    def search_cameras(self, start_after: Optional[int] = None, end_before: Optional[int] = None) -> List[Camera]:
        pass
    
    @abstractmethod
    def count_cameras(self) -> int:
        pass
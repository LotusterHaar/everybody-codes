from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from domain.vote_repository import VoteRepository
    
@dataclass
class Camera:
    camera_id: int
    camera: str
    latitude:float
    longitude:float
    
    def get(self, camera_repository: 'CameraRepository'):
        return camera_repository.get()
    
    def save(self, camera_repository: 'CameraRepository'):
        return camera_repository.add(self)

    def __hash__(self):
        return hash(self.camera_id)
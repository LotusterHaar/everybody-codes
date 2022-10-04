from typing import Optional, List, Tuple

import inject

from domain.camera import Camera
from domain.camera_repository import CameraRepository


class SearchCameras:
    @inject.autoparams()
    def __init__(self, repository: CameraRepository):
        self.__repository = repository

    def execute(self, start_after: Optional[int],
                end_before: Optional[int]) -> Tuple[List[Post], int]:
        results = self.__repository.search_cameras(start_after=start_after, end_before=end_before)
        count = self.__repository.count_cameras()

        return results, count
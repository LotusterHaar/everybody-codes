from adapter.inmemory_camera_repository import InMemoryCameraRepository
from domain.camera import Camera
from typing import List
import argparse 
from flask import Flask, render_template
from copy import deepcopy

#method that uses Euclidian Algorithm to return the greatest common denominator of two integers int1 and int2
def gcd(a, b):
    while b: 
        a, b = b, a % b
        return abs(a)
    

def cli_args():
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('--name', type=str, required=False)

    # Parse the argument
    args = parser.parse_args()
    
    return args

def divide_number_per_column(number):
    if number % 3 == 0 and number % 5 == 0:
        return 15
    elif number % 3 == 3:
        return 3
    elif number % 5 == 0:
        return 5
    else:
        return 0

def sort_camera_data(cameras):
    sorted_cameras = []
    for camera in cameras:
        number = camera.get('Camera_Id')
        column = divide_number_per_column(number)
        item = deepcopy(camera)
        item["Column"] = column
        sorted_cameras.append(item)
    return sorted_cameras

def create_app(camera_name): 
    app = Flask(__name__)

    camera_repository = InMemoryCameraRepository()
    
    @app.get('/')
    def index():
        data=sort_camera_data(camera_repository.all_cameras())
        return render_template('table.html', data=data)
    
    @app.get('/camera/<int:item_id>')
    def get_camera(item_id: int)-> Camera:
        return camera_repository.get_camera(item_id)
    
    @app.get('/cameras/name=<string:name>')
    def search_cameras(name: str)-> List[Camera]:
        return camera_repository.search_cameras(name)

    @app.get('/cameras/all')
    def all_cameras()-> List[Camera]:
        return camera_repository.all_cameras()
    
    @app.get('/cameras/total')
    def count_cameras()-> int:
        return str(camera_repository.count_cameras())
        
    return app

if __name__ == "__main__":

    args = cli_args()
    app = create_app(args.name)
    app.run(host="0.0.0.0", port=8000)
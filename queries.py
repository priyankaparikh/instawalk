""" Holds all the queries made by the application to the postgres SQL db.
Db name: """

from models import connect_to_db, db
from models import (User, Comp_Routes, User_Routes, Route, Waypoint, Step, Path,
                    Direction, Step_Direction, Path_Step)
from server import app
from geopy import Nominatim

# def get_tokens(user_id):
#     """Get the amount of tokens that a user already has."""

#     user = User.query.filter(User.user_id == user_id).first()
#     user.tokens += 5
#     tokens = user.tokens
#     db.session.commit()

#     return str(tokens)


def jsonify_paths():
    paths = Path.query.all()

    for path in paths:
        path_start = path.start_point
        path_end = path.end_point
        start_point = Waypoint.query.filter(Waypoint.waypoint_id == path_start).first()
        end_point = Waypoint.query.filter(Waypoint.waypoint_id == path_end).first()
        s_location = geolocator.reverse(start_point.latitude, start_point.longitude)
        start_address = s_location.address
        e_location = geolocator.reverse(end_point.latitude, end_point.longitude)
        end_address = e_location.address

        temp_dict = {
        "start_point": {
            "latitude": start_point.latitude,
            "longitude": start_point.longitude,
            "address": start_address,
            "images": [{"filename": start_point.image_url}],
            "descriptions": [start_point.location]
        },
        "end_point": {
            "latitude": end_point.latitude,
            "longitude": end_point.longitude,
            "address": end_address,
            "images": [{"filename": end_point.image_url}],
            "descriptions": [end_point.location]
        },
            "id": path.path_id
        }

        curr_path = temp_dict

        path_step_id = path.steps 
        path_steps = Path_Steps.query.filter(Path_Steps.ps_id == path_step_id).first()
        steps = path_steps.steps #array of step ids
        step_list = []

        for step in steps:
            curr_step = Step.query.filter(Step.step_id == step).first()
            start = curr_step.start_point
            end = curr_step.end_point
            sd_id = curr_step.sd_id
            step_directions = Step_Directions.query.filter(Step_Directions.sd_id == sd_id).first()
            directions = step_directions.directions #array of direction ids

            start_point = Waypoint.query.filter(Waypoint.waypoint_id == start).first()
            end_point = Waypoint.query.filter(Waypoint.waypoint_id == end).first()

            s_location = geolocator.reverse(start_point.latitude, start_point.longitude)
            start_address = s_location.address
            e_location = geolocator.reverse(end_point.latitude, end_point.longitude)
            end_address = e_location.address

            start_point_dict = {"start_point": {
                    "latitude": start_point.latitude,
                    "longitude": start_point.longitude,
                    "address": start_address,
                    "images": [{"filename": start_point.image_url}],
                    "descriptions": [start_point.description]
                    }
            }

            end_point_dict = {"end_point": {
                    "latitude": end_point.latitude,
                    "longitude": end_point.longitude,
                    "address": end_address,
                    "images": [{"filename": end_point.image_url}],
                    "descriptions": [end_point.description]
                    }
            }

            step_dict = {start_point_dict, end_point_dict}
            i = 1
            for direction in directions:
                curr_direction = Direction.query.filter(Direction.direction_id == direction).first()
                direction_image = curr_direction.image_url
                direction_text = curr_direction.direction_text

                direction_dict = {
                "direction": direction_text,
                "data_points": [{
                    "images": [{
                            "filename": direction_image
                        }]
                    }],
                    "descriptions": [direction_text]
                }

                direction_num = "direction" + str(i)
                i += 1

                step_dict[direction_num] = direction_dict
                step_list.append(step_dict)

        curr_path["steps"] = step_list


# if __name__ == "__main__":
#     connect_to_db(app)



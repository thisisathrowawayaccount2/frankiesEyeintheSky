from math import radians, sin, cos, sqrt, atan2, degrees

EARTH_RADIUS_MILES = 3958.8
FEET_PER_MILE = 5280

def haversine_distance(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float
) -> float:
    """
    Calculates the great-circle distance
    between two GPS coordinates.
    """
    
    lat1 = radians(lat1)
    lon1 = radians(lon1)

    lat2 = radians(lat2)
    lon2 = radians(lon2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (
        sin(delta_lat / 2) ** 2
        + cos(lat1)
        * cos(lat2)
        * sin(delta_lon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a),
    )

    return EARTH_RADIUS_MILES * c

def feet_to_miles(
    feet: float,
) -> float:
    """
    Converts a distance from feet to miles.
    """

    return  feet / FEET_PER_MILE

def calculate_bearing(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    
    """
    Calculate the initial bearing from point A to point B.
    
    Returns a compass bearing in degrees.
    """

    lat1 = radians(lat1)
    lat2 = radians(lat2)

    delta_lon = radians(lon2 - lon1)

    x = sin(delta_lon) * cos(lat2)

    y = (
        cos(lat1) * sin(lat2)
        - sin(lat1)
        * cos(lat2)
        * cos(delta_lon)
    )

    bearing = degrees(
        atan2(
            x,
            y
        )
    )

    return (bearing +360) % 360

def angular_difference(
        angle1: float,
        angle2: float,
) -> float:
    """
    Return the smallest difference between two headings.
    """

    difference = abs(angle1 - angle2)

    if difference > 180:
        difference = 360 - difference

    return difference
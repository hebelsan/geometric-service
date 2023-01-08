from flask import Flask, request, jsonify

from shapes.plane import Plane
from shapes.polygon import Polygon

app = Flask(__name__)


@app.route('/cut', methods=['POST'])
def cut():
    """
    Cut the polygon at the given plane and return the resulting cut.

    Example Body:
    {
        "polygon": {
            "vertices": [[-0.5, 0, 0], [0, 1, 0], [0.5, 0, 0]]
        },
        "plane": {
            "point": [0, 0.5, 0],
            "normal": [0, 1, 0]
        }
    }

    Returns:
    {
        "cut": [
            [-0.25, 0.5, 0.0],
            [0.25, 0.5, 0.0]
        ]
    }
    """
    try:
        # Parse the request payload
        data = request.get_json()
        # Extract the polygon and plane data from the payload
        polygon = Polygon(data['polygon']['vertices'])
        plane = Plane(data['plane']['point'], data['plane']['normal'])
        cut_p = polygon.cut(plane)
        # Return the cut polygon as a response
        return jsonify({'cut': cut_p.vertices.tolist()})
    except Exception as err:
        return jsonify({'error': str(err)})


if __name__ == '__main__':
    app.run()

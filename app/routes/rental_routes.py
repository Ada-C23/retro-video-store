from flask import Blueprint, request
from .route_utilties import validate_model, create_response_for_model
from ..models.customer import Customer
from ..models.video import Video
from ..models.rental import Rental

bp = Blueprint("rentals", __name__, url_prefix="/rentals")

@bp.post("/check-out")
def checkout():
    request_body = request.get_json()
    customer_id = request_body["customer_id"]
    video_id = request_body["video_id"]
    customer = validate_model(Customer, customer_id)
    video = validate_model(Video, video_id)

    # is the video available
    if not video.is_available():
        response = {"details": f"insufficient inventory"}
        return response, 400

    return create_response_for_model(Rental, request_body)
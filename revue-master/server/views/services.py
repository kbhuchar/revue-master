from app import app
from flask import jsonify, request
from models import Services, Reviews, Locations, User
from schema import Schema, And, Use
from authorization import login_required
from mongoengine.errors import ValidationError

@app.route("/api/services")
def listServices():
    serviceList = [s.to_public_json() for s in Services.objects()]
    return jsonify(serviceList)

@app.route("/api/services/<string:servicename>")
def getService(servicename: str) -> str:
    service = Services.objects(name=servicename).first()
    if service:
        return jsonify(service.to_public_json())
    else:
        return jsonify({"error": "Service not found"}), 404


@app.route("/api/addreview", methods=["POST"])
@login_required
def reviews_added(username: str):
    print(request.form.get("rating"), type(request.form.get("rating")))
    schema = Schema({
        "title": And(str, len, error="Title not specified"),
        "location": And(str, len, error="Location not specified"),
        "rating": And(Use(int), error="Rating is not out of 5"),
        "content": And(str, len, error="Content not specified"),
        "service": And(str, len, error="Not a valid service")
    })
    form = {
        "title": request.form.get("title"),
        "location": request.form.get("location"),
        "rating": request.form.get("rating"),
        "content": request.form.get("content"),
        "service": request.form.get("service")
    }
    validated = schema.validate(form)

    user = User.objects(username=username).first()

    review = Reviews(
        title=validated["title"],
        location=validated["location"],
        rating=validated["rating"],
        content=validated["content"],
        service=validated["service"],
        username=username,
    )
    service = Services.objects(locations__name = review.location).first()
    location = service.locations.get(name = review.location)
    location.reviewList.append(review)
    service.save()
    return {"message": "ok"}

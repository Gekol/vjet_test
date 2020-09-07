from flask import Flask, render_template, request, make_response
from flask_restful import Api, Resource
from birthday_probability import birthday_probability

app = Flask(__name__)
api = Api(app)


class PostInputAPI(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('base.html'), 200, headers)

    def post(self):
        days = int(request.form["days"])
        people = int(request.form["people"])
        interval = int(request.form["range"])
        if 0 <= interval <= days and people > 1 and days > 0:
            return {
                "result": birthday_probability(days, people, interval)
            }
        return {
                   "result": "Wrong data!!!"
               }, 400


api.add_resource(PostInputAPI, '/')

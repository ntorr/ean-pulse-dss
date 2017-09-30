import json
import logging
from flask import Flask, request, abort, jsonify
from flask_restful import Api, Resource, reqparse

from pulse_dss.utils import validate_request_data, convert_to_df

app = Flask(__name__)
api = Api(app)

logging.basicConfig(level='INFO')


class Score(Resource):
    def post(self):
        data = validate_request_data(request)
        logging.info(data)

        train = convert_to_df(data['train'])
        score = convert_to_df(data['score'])

        logging.info('train data \n%s' % str(train))
        logging.info('score data \n%s' % str(score))

        return jsonify('Success')


api.add_resource(Score, '/score')


"""
@app.route('/dss/test', methods=['POST'])
def score():
    logging.info('received data %s' % str(request.__dict__))
    if not request.json:
        abort(400)
    return jsonify('Success')
"""


if __name__ == '__main__':
    # start api
    app.run(debug=True)

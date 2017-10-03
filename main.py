import importlib
import logging
import notebooks.utils as notebook_utils
from flask import Flask, request, make_response
from flask_restful import Api, Resource

from pulse_dss.request_handler import validate_request_data, convert_dict_to_df, convert_df_to_json

app = Flask(__name__)
api = Api(app)

logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__file__)


class Score(Resource):
    @staticmethod
    def post():
        # validate request
        data = validate_request_data(request)
        logging.info(data)

        # set train and score data
        train = convert_dict_to_df(data['train'])
        score = convert_dict_to_df(data['score'])
        logger.info('train data \n%s' % str(train))
        logger.info('score data \n%s' % str(score))

        # get config (when service exists)
        config = None

        # collect notebook details
        module_path = data['notebook']
        logger.info('collecting notebook %s.%s' % (module_path, 'ipynb'))
        logger.info('notebook_id = %s' % notebook_utils.hash_notebook(module_path))

        # import notebook as module
        nb_module = importlib.import_module(module_path)

        # call execute method
        result = nb_module.execute(train, score, config=config)

        return make_response(convert_df_to_json(result))


api.add_resource(Score, '/score')


if __name__ == '__main__':
    # start api
    app.run(debug=True)

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class Greaterthan(Resource):
    def get(self, n1, n2):
        n1 = float(n1)
        n2 = float(n2)
        if n1>n2:
            return {'ans': 'True'}
        else:
            return {'ans': 'False'}

api.add_resource(Greaterthan, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5055,
        host="0.0.0.0"
    )

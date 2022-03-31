from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class Exponent(Resource):
    def get(self, n1, n2):
        n1 = float(n1)
        n2 = float(n2)
        if n2==0:
            return {'ans': 1.0}
        else:
            return {'ans' : n1**n2}

api.add_resource(Exponent, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5056,
        host="0.0.0.0"
    )

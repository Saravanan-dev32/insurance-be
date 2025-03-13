from flask import Flask
from flask_restful import Api
from flask_cors import CORS


from api.policies_api import GetPolicies,GetPolicyTypes


application = Flask(__name__)
restful_api = Api(application)

CORS(application, origins=["https://insurance-be.onrender.com"])


restful_api.add_resource(GetPolicies,"/api/policies",methods=['GET'])
restful_api.add_resource(GetPolicyTypes,"/api/policy-types",methods=['GET'])


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080,debug=True)
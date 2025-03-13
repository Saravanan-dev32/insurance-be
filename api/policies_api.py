from flask_restful import Resource
from services.middlewares.common_middlewares import do_validation
from schemas.policies_schema import get_search
from services.policies_services import get_policy_list,get_policy_types
from services.middlewares.common_middlewares import do_validation



class GetPolicies(Resource):
    @do_validation(get_search)
    def get(self):
        result = get_policy_list()
        return result
    
class GetPolicyTypes(Resource):

    def get(self):
        result = get_policy_types()
        return result
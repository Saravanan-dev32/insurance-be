from models.service_result import ServiceResult
from db.db_utils_json import JSONPolicyDatabase
from flask import request


db = JSONPolicyDatabase()

def get_policy_list():

    search_term = request.args.get('search')
    
    min_premium = request.args.get('min_premium')
    if min_premium:
        min_premium = float(min_premium)
    
    max_premium = request.args.get('max_premium')
    if max_premium:
        max_premium = float(max_premium)
    
    policy_type = request.args.get('policy_type')
    
    min_coverage = request.args.get('min_coverage')
    if min_coverage:
        min_coverage = float(min_coverage)
    
    sort_by = request.args.get('sort_by')
    sort_direction = request.args.get('sort_direction', 'asc')
    policies = db.get_filtered_policies(
        search_term=search_term,
        min_premium=min_premium,
        max_premium=max_premium,
        policy_type=policy_type,
        min_coverage=min_coverage,
        sort_by=sort_by,
        sort_direction=sort_direction
    )
    return ServiceResult(code=200, data=policies).make_response()


def get_policy_types():
    types = db.get_policy_types()
    return  ServiceResult(code=200, data=types).make_response()

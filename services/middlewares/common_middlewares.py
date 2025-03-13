from flask import request
from functools import wraps
from models.service_result import ServiceResult
from marshmallow import ValidationError

def do_validation(schema):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                if request.method == "GET":
                    json_data = request.args  
                else:
                    json_data = request.get_json() 
                
                if not json_data:
                    return ServiceResult(
                        code=400,
                        data=[{"key": "request", "msg": "Invalid or missing JSON in request body"}]
                    ).make_response()
                
                schema.load(json_data)

            except ValidationError as err:
                results = []
                for key, value in err.messages.items(): 
                    if isinstance(value, dict):
                        for v in value.values():
                            try:
                                for sub_key, sub_value in v.items():
                                    res = {"key": f"{key}.{sub_key}", "msg": ' '.join(map(str, sub_value))}
                                    results.append(res)
                            except:
                                res = {"key": key, "msg": ' '.join(map(str, v))}
                                results.append(res)
                    else:
                        res = {"key": key, "msg": ' '.join(map(str, value))}
                        results.append(res)

                return ServiceResult(code=400, data=results).make_response()

            return fn(*args, **kwargs)

        return wrapper
    return decorator

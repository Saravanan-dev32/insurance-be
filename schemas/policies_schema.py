
from marshmallow import (fields,validate,Schema)

  
class Get_Search(Schema):
     search = fields.String(
        required = False, allow_none=False
     )
     min_premium = fields.String(
        required = True, allow_none=False, validate=validate.Length(min=1)
     )
     max_premium = fields.String(
        required = True, allow_none=False, validate=validate.Length(min=1)
     )
     min_coverage =  fields.String(
        required = True, allow_none=False, validate=validate.Length(min=1)
     )
     sort_by = fields.String(
        required = True, allow_none=False
     )
     policy_type = fields.String(
        required = True, allow_none=False
     )
     sort_direction = fields.String(
        required = False, allow_none=False
     )
     
  
    
get_search = Get_Search()


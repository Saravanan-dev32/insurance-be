


class ServiceResult:
    
    def __init__(self, code=200, data={}, msg=None):
        self.code = code
        self.msg =msg
        self.data = data
    
    def make_response(self):
        code = self.code
        results = self.data
        
        ALL_SUCCESS_CODES = {
            200 : "Fetch successfully",
            205 : "Updated successfully",
        }
        
        ALL_ERROR_CODES = {
            404 : "Resource not found",
            400 : "Validation error",
            500 : "Something went wrong"
        }
        
        if code in ALL_SUCCESS_CODES:
            status = "success"
            msg = ALL_SUCCESS_CODES[code] 
        else: 
            status = "error"
            if code in ALL_ERROR_CODES:
                msg = ALL_ERROR_CODES[code]   
         
        response_data = {
                "status": status,
                "code": code,
                "message": msg,
                "results": results
            }   
        return response_data
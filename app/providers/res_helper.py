from fastapi import Response, status


def response_success(data):
    return {"result": True, "data": data}


def response_failure(response: Response, e: Exception):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"result": False, "error_msg": str(e)}

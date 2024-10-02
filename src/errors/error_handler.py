from src.presentation.http.http_response import HttpResponse
from .types import HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                    'errors': [
                        {
                            'title': error.name,
                            'detail': error.message
                        }
                    ]
                }
        )

    return HttpResponse(status_code=500, body={
        'errors': [
            {
                'title': 'Internal Server Error',
                'detail': str(error)
            }
        ]
        })

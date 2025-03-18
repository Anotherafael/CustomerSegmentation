import sys


def detailed_error_msg(error, error_details: sys):
    _, _, exception_traceback = error_details.exc_info()
    file_name = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    detailed_error_message = f"An error occurred in python file [{file_name}] line number [{line_number}] error message [{str(error)}]"

    return detailed_error_message


class CustomException(Exception):

    def __init__(self, detailed_error_message: str, error_details: sys) -> None:
        super().__init__(detailed_error_message)
        self.detailed_error_message = detailed_error_msg(
            detailed_error_message, error_details=error_details
        )

    def __str__(self) -> str:
        return self.detailed_error_message

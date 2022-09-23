from services.dto.dto_base import DTO_base

class ErrorDTO(DTO_base):
    def __init__(self):
        self.message = "500 Internal server Error"
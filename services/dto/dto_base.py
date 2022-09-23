import json


class DTO_base:
    def get_json(self):
        return json.loads(json.dumps(self, default=lambda o: getattr(o, '__dict__', str(o))))

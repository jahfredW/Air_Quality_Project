from utils.configuration import Configuration
from business.components import pollution


class PollutionAPI:

    @staticmethod
    def get_environment():
        environment = (Configuration().get_instance().version,
                       Configuration().get_instance().target)

        return {
            "version": environment[0],
            "target": environment[1],
        }
 
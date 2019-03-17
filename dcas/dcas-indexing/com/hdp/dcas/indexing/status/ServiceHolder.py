from abc import ABC
from abc import abstractmethod


class StatusOP(ABC):
    """
    This is CRUD operations for Service object
    """

    @abstractmethod
    def add_or_update_service(self, service_job_key, service_obj):
        """
        add or update the Service obj to StatusJson in memory and persistence

        :param service_job_key:
        :param service_obj:
        :return: void
        """
        pass

    @abstractmethod
    def get_service(self, service_obj):
        """
        query the Service object by its job_key

        :param service_obj:
        :return: the Service object
        """
        pass

from abc import ABC
from abc import abstractmethod
import jsonpickle


class StatusHolder(ABC):
    """
    This is persistence API for StatusJson
    """

    @abstractmethod
    def get_status(self, job_key):
        """

        :param job_key:
        :return: the StatusJson object
        """
        pass

    @abstractmethod
    def add_or_update_status(self, job_key, status_obj):
        """
         persistence of StatusJson object to file of status.json

        :param job_key: the jobKey
        :param status_obj: the StatusJson object
        :return:
        """
        pass


class StatusHolderImpl(StatusHolder):
    file_folder = '/temp/index'

    def __init__(self):
        pass

    def get_status(self, job_key):
        file = self.get_file(job_key);
        f = open(file, 'r')
        content = f.readlines()
        print("content from file--> {}".format(content))
        status_obj = jsonpickle.decode(content)
        return status_obj

    def add_or_update_status(self, job_key, status_obj):
        json_str = jsonpickle.encode(status_obj, unpicklable=False)
        f = open(self.get_file(job_key), 'w')
        f.write(json_str)

    @staticmethod
    def get_file(job_key):
        return StatusHolderImpl.file_folder + '/' + job_key + '/status.json'


def test():
    st = StatusHolderImpl()
    print(isinstance(st, StatusHolder))


if __name__ == '__main__':
    test()

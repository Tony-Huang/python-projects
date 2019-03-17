from abc import ABC
from abc import abstractmethod


class StatusFactory(ABC):
    @abstractmethod
    def new_status(self, service_tuple_list):
        """
        generate StatusJson object by list of service tuple ,
        [(service_name,job_key),(,)...]
        :param service_tuple_list:
        :return:
        """
        pass

    @abstractmethod
    def new_service(self, service_tuple):
        """
        generate service object by service_tuple, (service_name, job_key)

        :param service_tuple: ( service_name, job_key)
        :return: Service
        """
        pass

    @abstractmethod
    def new_metainfo(self, service_tuple):
        """
        generate Metainfo object by service_tuple

        :param service_tuple: (service_name, job_key)
        :return:
        """
        pass


class StatusFactoryImpl(StatusFactory):

    def new_status(self, service_tuple_list):
        for t in service_tuple_list:
            svc_name = t[0]
            job_key = t[1]
            print(svc_name, job_key)

    def new_service(self, service_tuple):
        svc_name = service_tuple[0]
        job_key = service_tuple[1]
        print(svc_name, job_key)

    def new_metainfo(self, service_tuple):
        svc_name = service_tuple[0]
        job_key = service_tuple[1]
        print(svc_name, job_key)


def test():
    f = StatusFactoryImpl()
    t1 = ('ADDRESS', 'jk001')
    t2 = ('POI', 'jk002')
    t3 = ('KNOWLEDGE', 'jk003')
    ls = [t1, t2, t3]
    f.new_status(ls)
    f.new_metainfo(t1)
    f.new_service(t2)


if __name__ == '__main__':
    test()

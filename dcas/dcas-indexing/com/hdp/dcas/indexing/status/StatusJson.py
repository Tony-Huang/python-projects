import jsonpickle
import time
import datetime


class StatusJson(object):

    def __init__(self, services, meta_info):
        self.services = services
        self.metaInfo = meta_info

    @property
    def svcs(self):
        return self.svcs

    @svcs.setter
    def svcs(self, servcs):
        self.services = servcs

    @property
    def meta(self):
        return self.metaInfo

    @meta.setter
    def meta(self, meta_info):
        self.metaInfo = meta_info

    def __repr__(self):
        return "services->:{}, meta->:{}".format(self.services, self.metaInfo)


class Service:
    def __init__(self, job_key, core_result, system, output):
        self.jobKey = job_key
        self.coreResult = core_result
        self.system = system
        self.output = output

    def __repr__(self):
        return "{ jobKey :" + self.jobKey + ", system:" + str(self.system)
        + "}"


class MetaInfo(object):
    def __init__(self, count, meta):
        self.count = count
        self.names = meta

    def __repr__(self):
        return "{count=" + str(self.count) + " , names=" + str(self.names) + "}"


class CoreResult:
    def __init__(self, start_time, end_time, status):
        self.startTime = start_time
        self.endTime = end_time
        self.status = status


class Output:
    def __init__(self, index_path, report_path):
        self.indexFolder = index_path
        self.reportFolder = report_path


class System:
    def __init__(self, hostname):
        self.hostName = hostname

    def __repr__(self):
        return self.hostName


def main():
    print("----------- ------------")
    system = System("host-xx")

    r1 = CoreResult(datetime.datetime.now().isoformat('T'), None, 'IN_PROGRESS')
    o1 = Output('/temp/index/job1', '/temp/logs/job1')
    svc1 = Service('job1', None, None, None)
    svc1.system = system
    svc1.coreResult = r1
    svc1.output = o1

    r2 = CoreResult(datetime.datetime.now().isoformat('T'), None, 'IN_PROGRESS')
    o2 = Output('/temp/index/job2', '/temp/logs/job2')
    svc2 = Service('job2', None, None, None)
    svc2.system = system
    svc2.coreResult = r2
    svc2.output = o2

    # services
    services = [svc1, svc2]
    # MetaInfo

    names = ['address', 'POI']
    count = len(names)
    meta_info = MetaInfo(count, names)
    status = StatusJson(services, meta_info)

    print("----------- as json------------")
    json_str = jsonpickle.encode(status, unpicklable=False)
    print(json_str)
    f = open('status.json', 'w')
    f.write(json_str)

    print(time.time())
    print(datetime.date.today())
    print(datetime.date.fromtimestamp(time.time()))

    print(datetime.datetime.now())
    print(datetime.datetime.now().isoformat('T'))
    print(datetime.datetime.utcnow())


if __name__ == '__main__':
    main()

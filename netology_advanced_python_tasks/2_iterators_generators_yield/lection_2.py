import requests


class HealthCheck:

    def __init__(self, path):
        self.file = open(path, encoding='utf-8')
        self.session = requests.Session()

    def __iter__(self):
        return self

    def __next__(self):
        host = self.file.readline().strip()
        if not host:
            raise StopIteration
        try:
            response = self.session.get(f'http://{host}')
            status = response.status_code
        except requests.ConnectionError as er:
            status = str(er)
        return {host: status}


def health_check(path):
    session = requests.Session()
    with open(path) as hosts_file:
        for host in hosts_file:
            host = host.strip()
            try:
                response = session.get(f'http://{host}')
                status = response.status_code
            except requests.ConnectionError as er:
                status = str(er)
            yield {host: status}


if __name__ == '__main__':
    for status in HealthCheck('sites.list'):
        print(status)

    for status in health_check('sites.list'):
        print(status)

    sample_list = [2, 5, 1, 0]
    sample_list_sq = []
    for n in sample_list:
        sample_list_sq.append(n * n)

    sample_list_sq = [n * n for n in sample_list]
    sample_list_sq_gen = (n * n for n in sample_list)

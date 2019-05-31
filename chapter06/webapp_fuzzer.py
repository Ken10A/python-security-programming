#!/usr/bin/python
# -*- coding:utf: 8 -*-

import click
import glob


class WebAppFuzzer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)

        files = glob.glob('./fuzzdb/attack/xss/**/*.txt', recursive=True)
        self.fuzzdb = []

        for fname in files:
            with open(fname, 'rb') as f:
                data = f.read().decode('utf-8').splitlines()
                self.fuzzdb += data

        with open('./http_template.txt', 'rb') as f:
            data = f.read().decode('utf-8').replace('\n', '\r\n')
            self.http_template = string.Template(data)

        self.status_code = 0

    def gen_fuzz(self, index):
        return self.fuzzdb[index]

    def gen_fuzz(self):
        pass

    def do_fuzz(self):
        pass

    def is_vulnerable(self):
        pass

    def dump(self):
        pass


@click.command()
@click.argument('host')
@click.argument('port')
def run(host, port):
    fuzzer = WebAppFuzzer(host, port)

    while 1:
        fuzz = fuzzer.gen_fuzz()
        response = fuzzer.do_fuzz(fuzz)
        if fuzzer.is_vulnerable():
            fuzzer.dump()


def main():
    run()


if __name__ == '__main__':
    main()
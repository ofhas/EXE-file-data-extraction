#!/usr/bin/env python3
import json
from subprocess import Popen, PIPE
from threading import Thread
import pathlib
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):

        self.path = str(pathlib.Path().absolute()) + '\\file.html'
        try:
            file_to_open = open(self.path).read()

            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


class Consumer(Thread):
    def run(self):
        httpd = HTTPServer(('localhost', 8080), Serv)
        httpd.serve_forever()


class Producer(Thread):

    def run(self):
        path = str(
            pathlib.Path().absolute())  # using the pathlib enables to get the path of the file without the need to copy and paste it manually
        cmd = path + '\\generator-windows-amd64.exe'
        eventTypes = []
        dataWords = []

        p = Popen(cmd, stdout=PIPE)  # this will enables to extract the data out of the exe file output
        for line in iter(p.stdout.readline, ''):  # we'll run using iter on each output iteration

            # we'll use try and except block in order to preform error handling in case we'll get a bad output and
            # then turn it to a dict object that will later be written into a html file

            try:
                res = json.loads(line)
                # add all of the event types and data into a new lists
                eventTypes.append(res['event_type'])
                dataWords.append(res['data'])

                # we'll using list comprehension in order to count all different data and event type and store them into a new dict objects
                result_dictEvents = dict([(i, eventTypes.count(i)) for i in set(eventTypes)])
                result_dictdata = dict([(i, dataWords.count(i)) for i in set(dataWords)])

                # we'll create a new html file that gets all of the data that was stored in both event type and data lists

                with open('file.html', 'w') as file:
                    file.write('events:\n')
                    file.write(json.dumps(result_dictEvents))
                    file.write('\n')
                    file.write('data:\n')
                    file.write(json.dumps(result_dictdata))


            except:
                pass


producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()

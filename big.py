import json
from subprocess import Popen, PIPE
import time

global now
import pathlib


def execute(cmd):
    now = int(time.time())
    eventTypes = []
    dataWords = []

    p = Popen(cmd, stdout=PIPE)  # this will enables to extract the data out of the exe file output
    for line in iter(p.stdout.readline, ''):  # we'll run using iter on each output iteration

        # we'll use try and except block in order to preform error handling in case we'll get a bad output and
        # then turn it to a dict object that will later be written into a html file

        try:
            res = json.loads(line)
            seconds = res['timestamp']
            timmme = seconds - now
            print(timmme)
            if timmme > 60:
                print(f'The last 60 seconds count is {result_dictEvents} and {result_dictdata}')
                now = int(time.time())

            # add all of the event types and data into a new lists
            eventTypes.append(res['event_type'])
            dataWords.append(res['data'])

            # we'll using list comprehension in order to count all different data and event type and store them into a new dict objects
            result_dictEvents = dict([(i, eventTypes.count(i)) for i in set(eventTypes)])
            result_dictdata = dict([(i, dataWords.count(i)) for i in set(dataWords)])
            print(result_dictdata)
            print(result_dictEvents)
            # we'll create a new html file that gets all of the data that was stored in both event type and data lists

            with open('file.html', 'w') as file:
                file.write('events:\n')
                file.write(json.dumps(result_dictEvents))
                file.write('\n')
                file.write('data:\n')
                file.write(json.dumps(result_dictdata))


        except:
            pass

    p.stdout.close()


path = str(pathlib.Path().absolute()) # using the pathlib enables to get the path of the file without the need to copy and paste it manually

cmd = path + '\\generator-windows-amd64.exe'

execute(cmd)

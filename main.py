import pandas
import functions_framework
import datetime
import sys

@functions_framework.http
def get_time(request):
   
  timestamp = datetime.datetime.now().strftime("%H:%M:%S")
  request_json = request.get_json(silent=True)
  request_args = request.args

  return (f" Making another change {timestamp}!")

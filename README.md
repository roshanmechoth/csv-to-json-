https://www.bseindia.com/download/BhavCopy/Equity/EQ200318_CSV.ZIP 

In the zip there is a csv file that has data in this format:
code, name, open, high, low, close

From this csv we want a http api such that when I pass code as "GET" variable to api it gives me the (Fields: code, name, open, high, low, close) as a json response.

Django Requirment:
  django 1.8
http api such that when I pass code as "GET" variable to api
http://127.0.0.1:8000/app/e2enetwork/create-sccode/500040/
it will response as json format in browser :
{"SC_CODE": "500040", "SC_NAME": "CENTURY TEXT", "HIGH": "1167.25", "LOW": "1137.85", "CLOSE": "1154.15", "OPEN": "1150.00"}

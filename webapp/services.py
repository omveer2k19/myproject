from django.http import HttpResponse
import requests

# def get_employees(firstname, lastname, emp_id):
#     url = 'http://127.0.0.1:8000/employees/' 
#     params = {'firstname': firstname, 'lastname': lastname, 'emp_id': emp_id}
#     r = requests.get(url, params=params)
#     employee1 = r.json()
#     employee1_list = {'employee1':employee1['results']}
#     return employee1_list

def get_employees(request):
    if request.method == 'POST':
        # r = requests.post('https://www.somedomain.com/some/url/save', params=request.POST)
        pass
    else:
        r = requests.get('/employees/', params=request.GET)
    if r.status_code == 200:
        print(r)
        return HttpResponse(r)
    return HttpResponse('Could not save data')
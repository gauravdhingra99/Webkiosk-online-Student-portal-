from django.shortcuts import render
from kiosk.forms import NewUserForm
from django.template import Template, Context
from django.http import HttpResponse
# Create your views here.

def login(request):
    print(request.POST)
    if request.method == 'POST':
        global ern
        global dob
        global passw
        ern=request.POST.get("Enrollment")
        dob=request.POST.get("DOB")
        passw=request.POST.get("pass1")
        print(ern)
        print(dob)
        print(passw)
        #print(type(ern))
        #print(type(dob))
        #print(type(passw))
        import requests
        from bs4 import BeautifulSoup
        s=requests.Session()
        import urllib3
        requests.packages.urllib3.disable_warnings()
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
        except AttributeError:
            # no pyopenssl support used / needed / available
            pass

        head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Content-Length":"195",
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie": "switchmenu=sub4;",
        "Host":"webkiosk.juet.ac.in",
        "Origin":"https://webkiosk.juet.ac.in",
        "Referer": "https://webkiosk.juet.ac.in/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


        data={"x":"",
        "txtInst": "Institute",
        "InstCode": "JUET",
        "txtuType": "Member Type",
        "UserType": "S",
        "txtCode": "Enrollment No",
        "MemberCode": str(ern),
        "DOB": "DOB",
        "DATE1": str(dob),
        "txtPin": "Password/Pin",
        "Password": str(passw),
        "BTNSubmit": "Submit",
        }
        url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
        r=s.post(url,headers=head,data=data)
        #print(type(r.text))
        #print(len(r.text))

        #print(data)
        new=s.cookies.get_dict()
        print("this is total length"+str(len(r.text)))
        if(len(r.text) == 472 or len(r.text) > 1434 ):
            print("i m in if")
            return render(request,'kiosk/user.html')
        else:
            print("i m in else")
            return render(request,'kiosk/login.html',{"message":"Wrong credentials"})

    return render(request,'kiosk/login.html')



def user(request):
    return render(request,'kiosk/user.html')

def personal_info(request):

    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/PersonalFiles/StudPersonalInfo.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    per_info=[]
    for link in soup.findAll("tr"):
        for y in link.findAll("td"):
            for x in y.findAll("font",{"color" : "black"}):
                if x not in y.findAll("font",{"face" : "Arial"}):
                    d=str(x.text)
                    per_info.append(d)
    per_info[1]=''
    per_info[21]=''
    '''for i in per_info:
        print(i)'''

    #print(type(per_info))
    name=per_info[0]
    enroll=per_info[2]
    course=per_info[4]
    fathersname=per_info[3]
    semester=per_info[5]
    aadhar=per_info[6]
    smobile=per_info[7]
    telephone=per_info[9]
    semail=per_info[11]
    pmobile=per_info[8]
    telephone2=per_info[10]
    pemail=per_info[12]
    caddress=per_info[13]
    cdistrict=per_info[20]
    ccitypin=per_info[22]
    cstate=per_info[24]
    paddress=per_info[16]
    pdistrict=per_info[19]
    pcitypin=per_info[23]
    pstate=per_info[25]

    #print (per_info)


    return render(request,'kiosk/personal_info.html',{'name':name,'enroll':enroll,'course':course,'fathersname':fathersname,'semester':semester,'aadhar':aadhar,
                    'smobile':smobile,'telephone':telephone,'semail':semail,'pmobile':pmobile,'telephone2':telephone2,'pemail':pemail,
                    'caddress':caddress,'paddress':paddress,'cdistrict':cdistrict,'pdistrict':pdistrict,
                    'ccitypin':ccitypin,'pcitypin':pcitypin,'cstate':cstate,'pstate':pstate})
    #return HttpResponse(html)

def regsinfo(request):
    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/FAS/StudRegFee.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)


    r=s.get(url,headers=head)

    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst=[]
    for tab in soup.findAll("tbody"):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                lst.append(i)

    print(lst)

    thead=[]
    for tab in soup.findAll("thead"):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                thead.append(i)

    print(thead)


    return render(request,'kiosk/regsinfo.html',{ 'all':lst,'thead':thead,})

def feereciept(request):
    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/FAS/FeeReceipt.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)

    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    head=[]
    for tab in soup.findAll("table",{'rules':'groups'}):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                head.append(i)

    print(head)

    lst=[]
    for tab in soup.findAll("tbody"):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                lst.append(i)

    print(lst)

    thead=[]
    for tab in soup.findAll("thead"):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                thead.append(i)

    print(thead)


    return render(request,'kiosk/feereciept.html',{ 'all':lst,'head':head,'thead':thead,})


def feepayrec(request):
    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/pgfiles/OnlinePaymentHistory.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst=[]
    for tab in soup.findAll("table"):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                lst.append(i)


    print(lst)

    return render(request,'kiosk/feepayrec.html',{ 'all':lst[1:] })

def Attendance(request):
    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/Academic/StudentAttendanceList.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')

#used for attendence
    lst=[]
    for link in soup.findAll("tbody"):
         x=str(link.text)
         d=(x.split('\n'))


    for i in d:
        lst.append(i)

    # table = soup.find( "table", {"class":"sort-table"} )
    # final_list=list()
    # for row in table.findAll("td"):
    #     final_list.append(row.text)
    #     for x in row.findAll('a'):
    #         href_link=x.get('href')
    #         final_list.append(href_link)



    print(lst)
    return render(request,'kiosk/Attendance.html',{'all':lst,})

def CGPA(request):

    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/Exam/StudCGPAReport.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst=[]
    for tab in soup.findAll("table",{"align" : "center","id":"table-1"}):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                lst.append(i)


    print(lst)

    lsta=[]
    for tab in soup.findAll("table",{"rules" : "NONE"}):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                lsta.append(i)


    course=lsta[0]
    name=lsta[2]
    enroll=lsta[3]
    branch=lsta[4]
    aadhar=lsta[5]

    return render(request,'kiosk/CGPA.html',{'course':course,'name':name,'enroll':enroll,'branch':branch,'aadhar':aadhar,'all':lst })

def subjregister(request):

    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/Academic/StudSubjectTaken.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst=[]
    for tab in soup.findAll("table",{"align" : "middle","cellspacing":"0"}):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                lst.append(i)


    print(lst)

    return render(request,'kiosk/subjregister.html',{ 'all':lst })

def subjfaculty(request):

    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/Academic/StudSubjectFaculty.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    lst=[]
    for tab in soup.findAll("table",{"align" : "middle","id":"table-1"}):
        for link in tab.findAll("td"):
            h=str(link.text)
            d=(h.split('\n'))

            for i in d:
                lst.append(i)

    lst=lst[5:]
    NEWLIST=[]
    Rem=0
    while(Rem < len(lst)):
        if lst[Rem] != '\r':
            if lst[Rem] != '\t\t':
                if lst[Rem] != '\t\t\t\r' :
                    if lst[Rem] != '\t\t\t\t\r' :
                        if lst[Rem] != '\t\t\t\t\r' :
                            if lst[Rem] != '\t\t\r' :
                                NEWLIST.append(lst[Rem])
        Rem=Rem+1


    lsta=[]
    for tab in soup.findAll("table",{"align" : "middle","id":"table-1"}):
        for link in tab.findAll("tr",{'bgcolor' : '#c00000'}):
            for j in link.findAll('td'):


                h=str(j.text)
                d=(h.split('\n'))

                for i in d:
                    lsta.append(i)

    #print(lsta)

    return render(request,'kiosk/subjectfaculty.html',{'all':NEWLIST,'every':lsta,})

def displinary(request):

    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/Academic/DisciplinaryAction.jsp"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    head=[]
    for thead in soup.findAll("th"):
        h=str(thead.text)
        d=(h.split('\n'))

        for i in d:
            head.append(i)

    print(head)

    lst=[]
    for tab in soup.findAll("td"):
        h=str(tab.text)
        d=(h.split('\n'))

        for i in d:
            lst.append(i)


    print (lst)

    return render(request,'kiosk/displinary.html',{'all':lst,'thead':head})




def exammarks(request):

    import requests
    from bs4 import BeautifulSoup
    s=requests.Session()
    import urllib3
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    head={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"195",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "switchmenu=sub4;",
    "Host":"webkiosk.juet.ac.in",
    "Origin":"https://webkiosk.juet.ac.in",
    "Referer": "https://webkiosk.juet.ac.in/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


    data={"x":"",
    "txtInst": "Institute",
    "InstCode": "JUET",
    "txtuType": "Member Type",
    "UserType": "S",
    "txtCode": "Enrollment No",
    "MemberCode": str(ern),
    "DOB": "DOB",
    "DATE1": str(dob),
    "txtPin": "Password/Pin",
    "Password": str(passw),
    "BTNSubmit": "Submit",
    }
    url="https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp"
    r=s.post(url,headers=head,data=data)
    new=s.cookies.get_dict()
    for i,j in new.items():
    	x=str(i)
    	y=str(j)


    url="https://webkiosk.juet.ac.in/StudentFiles/Exam/StudentEventMarksView.jsp?x=&exam=2018ODDSEM"
    head ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Cookie":"switchmenu=sub1; JSESSIONID=str(new.values())",
    "Host":"webkiosk.juet.ac.in",
    "Referer":"https://webkiosk.juet.ac.in/StudentFiles/FrameLeftStudent.jsp",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    for key, value in head.items():
        head['Cookie'] = 'switchmenu=sub1; JSESSIONID='+str(y)

    r=s.get(url,headers=head)
    #print(r.text)
    html=(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    head=[]
    for thead in soup.findAll("thead"):
        h=str(thead.text)
        d=(h.split('\n'))

        for i in d:
            head.append(i)

    print(head)

    lst=[]
    for tab in soup.findAll("tbody"):
        h=str(tab.text)
        d=(h.split('\n'))

        for i in d:
            lst.append(i)


    print (lst)

    return render(request,'kiosk/exammarks.html',{'all':lst,'thead':head})

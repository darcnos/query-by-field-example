import requests

def login():
    """Logs into a FileBound site with provided credentials, returns a string-based GUID"""
    siteurl = input('https://')
    u = input('Username: ')
    p = input('Password: ')
    data = {
        'username': u,
        'password': p
    }
    loginstring = 'https://{}.filebound.com/api/login/'.format(siteurl)
    
    #Try to login, return GUID
    try:
        r = requests.post(loginstring, data)
        return(r.json())
    except requests.exceptions.RequestException as e:
        print('Catastrophic error. Bailing.')
        print(e)

def querysite(dcn):
    projectid = input('Enter a projectId: ')
    response = requests.get('https://{}}.filebound.com/api/files?filter=projectId_{},f1_{}&guid={}'.format(siteurl, projectid, dcn, guid)).json()

    if len(response) <= 0:
        print('No File found with DCN {}'.format(dcn))
        return None
    else:
        print('FileID: {}'.format(response[0]['fileId']))
    return(response[0]['fileId'])
        

guid = login()
dcn = input('Enter a DCN to query: ')
fileId = querysite(dcn)

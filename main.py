import requests, random, string, time
from requests.structures import CaseInsensitiveDict

url = "https://www.nitrotype.com/api/v2/auth/register/username"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json, text/plain, */*"
headers["accept-encoding"] = "gzip, deflate, br"
headers["accept-language"] = "en-US,en;q=0.9"
headers["content-length"] = "171"
headers["Content-Type"] = "application/json"
headers["cookie"] = """st-id=7; ntdev=14914982; __stripe_mid=a0b62274-8b9e-4d44-b1f9-83fee7ff16f41cf946; _ga=GA1.2.1152503635.1649978089; _gcl_au=1.1.318394311.1649978089; _fbp=fb.1.1649978089053.1652364230; ki_r=; __qca=P0-1679903801-1649978089336; permutive-id=a239cf6d-fe8d-40d3-bf3a-b08b173e5e55; FCNEC=[["AKsRol8jdO99CFSOY7vzMGCa8SebbldeCA2PhDD4Y4fiHFj9yJyzWMmeA9ciGd4VNgGiOwJBy1x6KI1d5DmwkyV8reqS86AOQ9ZTFwWLjV51iiFA5jJUf7G4dVgBhhqM8XFnlb1DZUza47fsNIygTrz0XWziWC5JBg=="],null,[]]; ki_t=1649978089339%3B1649978089339%3B1649978100167%3B1%3B3; ntuserguest=g0.5359869151507133"""
headers["origin"] = "https://www.nitrotype.com"
headers["referer"] = "https://www.nitrotype.com/race"
headers["sec-ch-ua"] = """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"""""
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = """"Windows"""""
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "same-origin"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    

while True:
    

    data = """
    {
      "username" : "xxx" ,
      "password" : "Thebest1!" ,
      "acceptPolicy" : "yes" ,
      "receiveContact" : "" ,
      "tz" : "America%2FChicago" ,
      "qualifying" : "1" ,
      "avgSpeed" : "60" , 
      "avgAcc" : "100" ,
      "carID" : "9" ,
      "raceSounds" : "only_fx"
    }
    """
    letters = string.ascii_lowercase
    user = ''.join(random.choice(letters) for i in range(10))


    data = data.replace("xxx", user)
    print(user)
    resp = requests.post(url, headers=headers, data=data)
    print(resp)
    try:
        tok = resp.json()['results']['token']
    except KeyError:
        pass
        tok = "aa"
    newheaders = CaseInsensitiveDict()
    newheaders["accept"] = "application/json, text/plain, */*"
    newheaders["accept-encoding"] = "gzip, deflate, br"
    newheaders["accept-language"] = "en-US,en;q=0.9"
    newheaders["authorization"] = "Bearer " + tok
    newheaders["content-length"] = "0"
    newheaders["Content-Type"] = "application/json"
    newheaders["cookie"] = """st-id=7; ntdev=149514982; __stripe_mid=a0b62274-8b9e-4d44-b1f9-83fee7ff16f41cf946; _ga=GA1.2.1152503635.1649978089; _gcl_au=1.1.318394311.1649978089; _fbp=fb.1.1649978089053.1652364230; ki_r=; __qca=P0-1679903801-1649978089336; permutive-id=a239cf6d-fe8d-40d3-bf3a-b08b173e5e55; FCNEC=[["AKsRol8jdO99CFSOY7vzMGCa8SebbldeCA2PhDD4Y4fiHFj9yJyzWMmeA9ciGd4VNgGiOwJBy1x6KI1d5DmwkyV8reqS86AOQ9ZTFwWLjV51iiFA5jJUf7G4dVgBhhqM8XFnlb1DZUza47fsNIygTrz0XWziWC5JBg=="],null,[]]; ki_t=1649978089339%3B1649978089339%3B1649978100167%3B1%3B3; ntuserguest=g0.5359869151507133"""
    newheaders["origin"] = "https://www.nitrotype.com"
    newheaders["referer"] = "https://www.nitrotype.com/racer/legendary_bih"
    newheaders["sec-ch-ua"] = """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"""""
    newheaders["sec-ch-ua-mobile"] = "?0"
    newheaders["sec-ch-ua-platform"] = """"Windows"""""
    newheaders["sec-fetch-dest"] = "empty"
    newheaders["sec-fetch-mode"] = "cors"
    newheaders["sec-fetch-site"] = "same-origin"
    newheaders["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    requests.post("https://www.nitrotype.com/api/v2/friend-requests/42580095/request", headers=newheaders)
    print("friend req sent")

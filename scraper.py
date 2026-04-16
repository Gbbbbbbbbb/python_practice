import requests

from bs4 import BeautifulSoup

url="https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content,
                     "html.parser",)
jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]

for job in jobs : 
    title = job.find("span", class_="new-listing__header__title__text")
    region=job.find_all("p",class_="new-listing__categories__category")
    
    # if region : 
    #     region_text=region.text.strip()
    #     print(region_text)
    print(title,"------",region)
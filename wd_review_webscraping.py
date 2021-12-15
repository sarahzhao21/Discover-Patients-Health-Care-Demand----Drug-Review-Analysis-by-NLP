from bs4 import BeautifulSoup
import requests
import json
import cfscrape
import pandas as pd

# def get_drug_dictionary(base_url, drug_list_url):
#     response = requests.get(drug_list_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     drug_dic = {}
#     #drug_group = soup.find('div', data-metrics-module="drugs-az")
#     #drug_list = drug_group.find_all('li')
#     print (soup)


drug_list_url = "https://www.webmd.com/drugs/2/index"
scraper = cfscrape.create_scraper()
content = scraper.get(drug_list_url).content
soup = BeautifulSoup(content, 'html.parser')
drug_group = soup.find('div', class_="drugs-list-index")
drug_list = drug_group.find_all('li')
print("total number of drugs:", len(drug_list))

drug_dic = {}
for drug in drug_list:
    drug_data = []
    drug_name = drug.find('a', class_="common-drug-name").text.strip()
    drug_url = drug.find('a', class_="common-drugs-review")['href']  
    #drug_pagenumber = int((drug_page.split(' ')[-1]).strip("()"))//5
    drug_content = scraper.get(drug_url).content
    drug_soup = BeautifulSoup(drug_content, 'html.parser')
    try:
       pagenumber = drug_soup.find('div', class_='postPaging').text.strip()
       number = int(pagenumber.split(' ')[-2])//5
    except:
       pagenumber = drug_soup.find('a',href="javascript:void()").text.strip()
       number = int(pagenumber.split('(')[-1].strip(')'))//5
       #pagenumber = drug_soup.find('label', class_ = 'count').text.strip()

    drug_data.append(drug_url)
    drug_data.append(number)
    drug_dic[drug_name] = drug_data

print("drug_dic:", len(drug_dic))

# def get_review_info_one(review_soup):
#     patient = review_soup.find('div', class_="details").find_all('span')
#     age = patient[1].text.strip()
#     gender = patient[2].text.strip()
#     date = review_soup.find('div', class_="date").text.strip()
#     rate = review_soup.find('div', class_="overall-rating").find('strong').text.strip()
#     stars = review_soup.find('div', class_="categories").find_all('section')
#     effect = int(stars[0].find('div')['aria-valuenow'])
#     ease =int(stars[1].find('div')['aria-valuenow'])
#     satisfy =int(stars[2].find('div')['aria-valuenow'])
#     try:
#         review = review_soup.find('p', class_="description").text.strip()
#     except:
#         review = None
#     return age, gender, date, rate, effect, ease, satisfy, review

#sub_dic = {key: value for key, value in drug_dic.items() if key != 'abilify'}
#print("sub_dic:", len(sub_dic))

def get_review_info(review_soup):
    try:
        date = str(review_soup.find('div', class_="date").text.strip())
    except:
        date = None

    try:
        condition = review_soup.find('strong', class_="condition").text.strip().split(':')[-1].strip()
    except:
        condition = None

    try:
        effect = review_soup.find('div', class_="categories").find_all('section')[0].find('div')["aria-valuenow"]
    except:
        effect = None

    try:
        ease = review_soup.find('div', class_="categories").find_all('section')[1].find('div')["aria-valuenow"]
    except:
        ease = None
    
    try:
        satisfy = review_soup.find('div', class_="categories").find_all('section')[2].find('div')["aria-valuenow"]
    except:
        satisfy = None
    
    try:
        helpful = int(review_soup.find('span', class_="likes").text.strip())
    except:
        helpful = None
    
    try:
        review = str(review_soup.find('p', class_ = "description").text.strip())
    except:
        review = None

    return date, condition, effect, ease, satisfy, helpful, review
    


drug_nm = []
date = []
condition = []
effect = []
ease = []
satisfy = []
helpful = []
review = []
#base_url = 'https://www.webmd.com'
for key, value in drug_dic.items():
    print(key)
    print(len(date), len(effect), len(review))
    for p in range(1, value[1]+1):
        review_url = value[0]+ '&pagenumber=' + str(p)
        r_content = scraper.get(review_url).content
        r_soup = BeautifulSoup(r_content, 'html.parser')
        try:
            review_list = r_soup.find('div', class_= "shared-reviews-container").find_all('div', class_="review-details")
        except: 
            review_list = None
            #review_list = r_soup.find('div', class_ = "shared-reviews-container").find_all('div', class_="review-details")
        if review_list:
            for r in review_list:
                r_date, r_condition, r_effect, r_ease, r_satisfy, r_helpful, r_review = get_review_info(r)
                drug_nm.append(key)
                date.append(r_date)
                condition.append(r_condition)
                effect.append(r_effect)
                ease.append(r_ease)
                satisfy.append(r_satisfy)
                helpful.append(r_helpful)
                review.append(r_review)
     
            

drug_reviews = pd.DataFrame({'drug_name':drug_nm, 'date':date, 'condition':condition, 'effect':effect, 'ease':ease, 'satisfy':satisfy, 'helpful':helpful, 'review':review})

drug_reviews.to_csv (r'drug_reviews.csv', index = True, header=True)

# import requests 
# from bs4 import BeautifulSoup 
# import csv 
# URL = "https://www.tripadvisor.com/Attractions-g293890-Activities-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html"
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }

# response=requests.get(URL, headers=headers)
# soup= BeautifulSoup(response.content,'html.parser')

# destinations=[]
# for item in soup.select('div.listing_title a')[:30]:
#     name= item.get_text(strip=True)
#     link = 'https://www.tripadvisor.com' + item['href']
#     destinations.append({'place_name': name, 'tripadvisor_link': link})


# Save to CSV
# keys = destinations[0].keys()
# with open('../data/dataCollection/destinations_sample.csv', 'w', newline='', encoding='utf-8') as f:
#     dict_writer = csv.DictWriter(f, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(destinations)

# print(f"Scraped {len(destinations)} destinations")
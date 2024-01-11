from bs4 import BeautifulSoup
import requests
import random as r
# Hey :D
# Webscriping mini project with random movie generator form 100 Best Movies of All Time :)

responce = requests.get("https://www.timeout.com/film/best-movies-of-all-time")

# print(responce.text)
soup = BeautifulSoup(responce.text, 'html.parser')


titles = soup.find_all(name="h3", class_="_h3_cuogz_1" )
categories = soup.find_all(name="span", class_ ="_text_163gl_28")

destription = soup.find_all(name="div",class_="_summary_kc5qn_21")

list_index_name= [(title.get_text()).split('.\xa0', 1) for title in titles ]

list_minus_one=list_index_name[:-1]

for i in list_minus_one:
    index_of_movie =[int(i[0]) for i in list_minus_one ]
    name_of_movie = [i[1] for i in list_minus_one] 
# for title in titles:
# .split('.\xa0', 1)

cate_strip = [cat.text for cat in categories if cat.text != "Film"]

#.find_all(name="p")

destr_strip = [des.find(name="p").text for des in destription]

def random_movie_100():
    random_nr = r.choice(index_of_movie)
    print(f"Rank: {index_of_movie[random_nr]} \nMovie: {name_of_movie[random_nr]} \nDestription: {destr_strip[random_nr]}")

random_movie_100()
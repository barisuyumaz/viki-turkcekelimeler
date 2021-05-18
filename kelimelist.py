#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import random




link1 = 'https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:S%C3%B6zc%C3%BCk_listesi'

icerik = requests.get(link1).content

soup = BeautifulSoup(icerik,"html.parser")

yeni = soup.find_all("div",{"style":"-webkit-column-count: 2;-moz-column-count: 2;column-count: 2;","class":"magicColumn"})[0]


pekyeni = yeni.find_all("li")

alfabe_list = []

for i in pekyeni:
	kelime = i.text
	alfabe_list.append(kelime[0])

print(alfabe_list)



def tumkelimeleri_al():
	with open('C:/Users/Administrator/Desktop/vikikelimelist.txt','w',newline='') as dosya:
		thewriter = csv.writer(dosya, delimiter="\n")
		tumkelimeler_list = []
		for j in alfabe_list:
			print(j)

			icerik1 = requests.get("https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:S%C3%B6zc%C3%BCk_listesi_("+j+")").content
			soup1 = BeautifulSoup(icerik1,"html.parser")


			yeni1 = soup1.find_all("div",{"class":"mw-parser-output"})[0]


			pekyeni1 = yeni1.find_all("li")

			for l in pekyeni1:

				if(l.text[0].isdigit() == True):
					pass
				else:
					tumkelimeler_list.append(l.text)
		thewriter.writerow(tumkelimeler_list)
		dosya.close()


def random_100_al():
	with open('C:/Users/Administrator/Desktop/random100vikikelimelist.txt','w',newline='') as dosya:
		thewriter = csv.writer(dosya, delimiter="\n")
		tumkelimeler_list = []
		random_100list = []
		for j in alfabe_list:
			print(j)

			icerik1 = requests.get("https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:S%C3%B6zc%C3%BCk_listesi_("+j+")").content
			soup1 = BeautifulSoup(icerik1,"html.parser")


			yeni1 = soup1.find_all("div",{"class":"mw-parser-output"})[0]


			pekyeni1 = yeni1.find_all("li")

			for l in pekyeni1:

				kelime = l.text
				if(kelime[0].isdigit() == True):
					pass
				elif(" " in kelime):
					pass
				elif(len(kelime)>5 and kelime[:4] in tumkelimeler_list):
					pass
				elif(len(kelime)<5 and kelime[:3] in tumkelimeler_list):
					pass
				else:
					tumkelimeler_list.append(kelime)
		while(len(random_100list)<100):

			index = random.randint(1,len(tumkelimeler_list))
			if(tumkelimeler_list[index] in random_100list):
				pass
			else:
				random_100list.append(tumkelimeler_list[index])

		thewriter.writerow(random_100list)
		dosya.close()

#random_100_al()

tumkelimeleri_al()
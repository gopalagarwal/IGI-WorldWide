#!/usr/bin/python2
import requests
import pymysql
from bs4 import BeautifulSoup

addDataRangeFrom=cgi.FormContent()['addDataRangeFrom'][0]
addDataRangeTo=cgi.FormContent()['addDataRangeTo'][0]
print ("Hello, starting to scrape data from igi")
db = pymysql.connect("localhost", "root", "root", "diamond_db")
cur = db.cursor()
print ("Hello, starting to scrape data from igi")
i = addDataRangeFrom
while i < addDataRangeTo:
	page = requests.get("http://www.igiworldwide.com/searchreport_postreq.php?r="+str(i))
	if (page.status_code == 200 and page.content != b'0'):
		soup = BeautifulSoup(page.content, 'html.parser')
		report_number = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl02_Labenew1"))[0].get_text()
		report_city_date = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl03_Labenew1"))[0].get_text()
		description = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl04_Labenew1"))[0].get_text()
		shape_and_cut = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl05_Labenew1"))[0].get_text()
		carat_weight = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl06_Labenew1"))[0].get_text()
		color_grade = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl07_Labenew1"))[0].get_text()
		clarity_grade = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl08_Labenew1"))[0].get_text()
		cut_grade = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl09_Labenew1"))[0].get_text()
		polish = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl10_Labenew1"))[0].get_text()
		symmetry = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl11_Labenew1"))[0].get_text()
		measurements = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl12_Labenew1"))[0].get_text()
		table_size = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl13_Labenew1"))[0].get_text()
		crown_height_angle = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl14_Labenew1"))[0].get_text()
		pavilion_depth_angle = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl15_Labenew1"))[0].get_text()
		girdle_thickness = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl16_Labenew1"))[0].get_text()
		culet = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl17_Labenew1"))[0].get_text()
		total_depth = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl18_Labenew1"))[0].get_text()
		fluorescence = list(soup.find_all(id="ctl00_ContentPlaceHolder1_dgReport_ctl19_Labenew1"))[0].get_text()
		sql = "INSERT INTO diamonds (report_number, report_city_date, description, shape_and_cut, carat_weight, color_grade, clarity_grade, cut_grade, polish, symmetry, measurements, table_size, crown_height_angle, pavilion_depth_angle, girdle_thickness, culet, total_depth, fluorescence) VALUES ('"+report_number+"', '"+report_city_date+"', '"+description+"', '"+shape_and_cut+"', '"+carat_weight+"', '"+color_grade+"', '"+clarity_grade+"', '"+cut_grade+"', '"+polish+"', '"+symmetry+"', '"+measurements+"', '"+table_size+"', '"+crown_height_angle+"', '"+pavilion_depth_angle+"', '"+girdle_thickness+"', '"+culet+"', '"+total_depth+"', '"+fluorescence+"');"
		try:
			cur.execute(sql)
			db.commit()
		except (pymysql.Error) as e:
			print(e)
			db.rollback()
		print("data inserted for report num "+str(i))
	else:
		print("NO RECORD for "+str(i))
	i = i + 1
db.close()

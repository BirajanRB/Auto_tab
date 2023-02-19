from os import system

with open("links.txt","r") as link_data:
	for i in link_data:
		system(f"start chrome -incognito {i}")

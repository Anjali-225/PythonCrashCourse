#8-6

def city_country(city_name, country_name):
	"""Return a full name, neatly formatted."""
	country_city = f"{city_name}, {country_name}"
	return country_city.title()

City_Names = city_country('santiago', 'chile')
print(f"\"{City_Names}\"")

City_Names = city_country('cape town', 'south africa')
print(f"\"{City_Names}\"")

City_Names = city_country('bulgaria', 'russia')
print(f"\"{City_Names}\"")

print("")
#----------------------------------------------------------------------------------
#8-7--Part 1

def make_album1(artist_name, album_title):
	#Returns a dictionary of information of an album with its artist
	album_info1 = {'artist': artist_name,'title': album_title}
	return album_info1

album1 = make_album1('Zero to infinity', 'Raftaar')
print(album1)

album1= make_album1('O.N.E', 'Badshah')
print(album1)

album1 = make_album1('Coca Cola Tu', 'Tony Kakkar')
print(album1)

print("")
######################################################################
#8-7--Part 2

def make_album2(artist_name, album_title, nr_songs=None):
	#Returns a dictionary of information about an album
	album_info2 = {'artist': artist_name,'title': album_title}
	if nr_songs:
		album_info2['nr_songs'] = nr_songs
	return album_info2

album2 = make_album2('Zero to infinity', 'Raftaar', 8)
print(album2)

album2= make_album2('O.N.E', 'Badshah', nr_songs=17)
print(album2)

album2 = make_album2('Coca Cola Tu', 'Tony Kakkar')
print(album2)

print("")
#----------------------------------------------------------------------------------
#8-8

def make_album(artist_name, album_title):
	#Returns a dictionary of information of an album with its artist
	album_info = {'artist': artist_name,'title': album_title}
	return album_info

while True:
	print("\nPlease enter album information:")
	print("(enter 'q' at any time to quit)")

	a_name = input("Artist Name: ")
	if a_name == 'q':
		break

	a_title = input("Album Title: ")
	if a_title == 'q':
		break

	album = make_album(a_name, a_title)
	print(f"\n{album.title()}")
	#----------------------------------------------------------------------------------
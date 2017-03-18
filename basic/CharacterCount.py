import pprint
message='it was a bright cold day in na abril.'

count={}

for character  in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)

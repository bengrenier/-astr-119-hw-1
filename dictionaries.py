#define a dictionary data structure

#dictionaries have key : value for the elements
example_dict = {
	"class" : "ASTR 119",
	"prof" : "Brant",
	"awesomeness" : 10
}
print(type(example_dict))     #will say dict

#get value via key
course = example_dict["class"]
print(course)

#change value via key
example_dict["awesomeness"] += 1     #increase awesomenessbu 1

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])
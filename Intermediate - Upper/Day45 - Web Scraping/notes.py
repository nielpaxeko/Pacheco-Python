from bs4 import BeautifulSoup

# Open contents of html file 
with open("website.html") as file:
    contents = file.read()
    
# Analyze and parse html file
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title) # Prints: <title>Angela's Personal Site</title>
print(soup.title.string) # Prints: Angela's Personal Site

# Prints entire html doc
# print(soup) 
# print(soup.prettify)  Same but indented

# Gets the first <a> tag
# print(soup.a) 

# Get all a tags
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)


for tag in all_anchor_tags:
    print(tag.getText()) # Print text in all anchor tags
    print(tag.get("href")) # Print links in all anchor tags
    pass

# Get a specific heding or other elem by looking for it by name(type) and id or class
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

# Selectors, in this example we select the a tag that is inside a p tag
company_url = soup.select_one(selector="p a")
print(company_url)

# Select elem by class
headings = soup.select(selector=".heading")
print(headings)
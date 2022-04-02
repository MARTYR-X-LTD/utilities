from bs4 import BeautifulSoup

with open("creative.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

links = []

for link in soup.find_all("td", class_="cell-=xXt"):
    print(link.a.text)
    links.append(link.a.text)
    link.decompose()

print(links)
   
for th in soup.findAll('th'):
    if 'URL' in th.text:
        th.decompose()

for a_tag in soup.find_all('a'):
    if "notion.so" in a_tag['href']:
        print(a_tag)
        a_tag['href'] = links.pop(0)
        # a_tag.replace_with(f"{a_tag.text}")
        # print(a_tag['href'])

for tr in soup.find_all("tr", attrs={'id': True}):
    print(tr['id'])
    del tr['id']

output = str(soup).replace("index-list-tag ", "")
output = output.replace("select-value-", "")
output = output.replace("cell-e~xq", "index-list-tag-cell")
output = output.replace("cell-title", "index-list-title-cell")

soup = BeautifulSoup(output, 'html.parser')

with open("full_output.html", "w") as file:
    file.write(soup.prettify())

with open("table.html", "w") as file:
    file.write(soup.find('table').prettify())

import requests, bs4
def getPresidents():
    link = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    res = requests.get(link,'lxml')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 2:
                d = cells[0].text
                if "Washington" in d:
                    data = d
    data = data.splitlines()
    for i in data:
        if "Washington" not in data[0]:
            del data[0]
        else:
            break

    return data


print(getPresidents())
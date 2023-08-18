import mechanicalsoup

def main():

    browser = mechanicalsoup.StatefulBrowser()  
    browser.open("https://en.wikipedia.org/wiki/Web_scraping")

    title = browser.page.select_one('span.mw-page-title-main')

    print("title: " + title.string)

    references = browser.page.select_one('ol.references')

    references_list = references.select('span.reference-text')

    for reference in references_list:
        link_tags = reference.find_all("a")
        
        for link_tag in link_tags:
            link = link_tag.get("href")
            if link:
                print(link)

main()
import mechanicalsoup
import csv
browser = mechanicalsoup.StatefulBrowser()


def extract_table_data(file_name):
    results = browser.page.select_one('table')

    file = open(file_name, 'w')
    csvwriter = csv.writer(file)

    headers = results.select('th')

    temp_header_row = []

    for header in headers:
        temp_header_row.append(header.string.strip().replace(",", ""))

    csvwriter.writerow(temp_header_row)

    rows = results.select('tr.team')

    for row in rows:
        cells = row.select('td')
        temp_row = []

        for cell in cells:
            temp_row.append(cell.string.strip().replace(",", ""))

        csvwriter.writerow(temp_row)

    file.close()

def navigate():
    browser.open("https://www.scrapethissite.com/")

    print(browser.url)

    sandbox_nav_link = browser.page.select_one('li#nav-sandbox')

    sandbox_link = sandbox_nav_link.select_one('a')

    browser.follow_link(sandbox_link)

    print(browser.url)

    sandbox_list_items = browser.page.select('div.page')

    hockey_list_item = sandbox_list_items[1]

    forms_sandbox_link = hockey_list_item.select_one('a')

    browser.follow_link(forms_sandbox_link)

    print(browser.url)

def handle_form():
    browser.select_form('form.form-inline')

    browser.form.input({"q": "new"})

    browser.submit_selected()

    extract_table_data("first-page-results.csv")

def handle_pagination():
    pagination_links = browser.page.select_one('ul.pagination')

    page_links = pagination_links.select('li')

    next_page = page_links[1]

    next_page_link = next_page.select_one('a')

    browser.follow_link(next_page_link)

    print(browser.url)

    extract_table_data('second-page-results.csv')

def main():
    navigate()
    handle_form()
    handle_pagination()

main()
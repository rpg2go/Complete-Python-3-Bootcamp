import requests
import bs4

base_url_books = "http://books.toscrape.com/catalogue/page-{}.html"
base_url_quotes = "http://quotes.toscrape.com/page/{}/"
format = "lxml"

def get_titles_first_page():
    global title
    two_start_titles = []
    for n in range(1, 51):

        scrape_url = base_url_books.format(n)
        print(scrape_url)

        req = requests.get(scrape_url)

        soap = bs4.BeautifulSoup(req.text, 'lxml')

        books = soap.select(".product_pod")

        for book in books:
            if len(book.select('.star-rating.Two')) != 0:
                title = book.select('a')[1]['title']
                two_start_titles.append(title)
    print(len(two_start_titles))
    for title in two_start_titles:
        print(title)


def get_all_authors():
    global title
    global format
    author_list = []

    pageIdx = 0

    while True:
        pageIdx += 1
        scrape_url = base_url_quotes.format(pageIdx)
        print(scrape_url)

        req = requests.get(scrape_url)
        #print(req.text)

        soap = bs4.BeautifulSoup(req.text, format)
        end_of_pages = soap.select(".col-md-8")
        #print(len(end_of_pages), end_of_pages[-1].text)
        if 'No quotes found!' in end_of_pages[-1].text:
            #print(end_of_pages[-1])
            print("End of pagination : ", "No more quotes found!")
            break

        authors = soap.select(".author")

        for author in authors:
            #print(author, type(author), author.text)
            author_list.append(author.text)


    authors = set(author_list)
    k = 0
    for a in authors:
        k += 1
        print(str(k), " - ", a)

if __name__== "__main__":
    # books site scraping
    #get_titles_first_page()

    # quote site scraping
    get_all_authors()
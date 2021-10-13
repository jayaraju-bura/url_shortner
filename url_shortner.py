import csv
import logging
import sys
import random

MAIN_URL_PREFIX = "https://shorturl.com/"
FILE_NAME = "database/tiny_urls.csv"
BASE_KEY = "AEIOSUMA23"
TEST_URLS = ["https://github.com/",
             "https://geeksforgeeks.org/",
             "https://hackerrank.com/",
             "https://twitter.com/"]


class UrlShortner:
    def __init__(self):
        self.long_url = None
        self.short_keys = []

    def short_url(self):
        tiny_url = ''.join(random.choice(BASE_KEY) for x in range(8))
        while tiny_url in self.short_keys:
            tiny_url = ''.join(random.choice(BASE_KEY) for x in range(8))
        return MAIN_URL_PREFIX + tiny_url

    def search_url(self):
        url_found = None
        try:
            with open(FILE_NAME, 'r') as file:
                csv_reader = csv.reader(file, delimiter=':')
                short_keys = []
                for row in csv_reader:
                    short_keys.append(row[1])
                    if row[0] == self.long_url:
                        url_found = row[1]
                self.short_keys = short_keys
                return url_found

        except  IOError as error:
            logging.debug("Short URL for the requested long url doesn't exist")
            return url_found

    def write_to_file(self, short_url=None):
        with open(FILE_NAME, 'a') as file:
            csv_writer = csv.writer(file, delimiter=':')
            csv_writer.writerow([self.long_url, short_url])

    def run(self):
        tiny_url = self.search_url()
        if tiny_url is None:
            tiny_url = self.short_url()
            self.write_to_file(short_url=tiny_url)
        logging.info("tiny url for the requested URL is " + tiny_url)
        return tiny_url

    def run_tests(self):
        for test_url in TEST_URLS:
            self.long_url = test_url
            self.run()


if __name__ == "__main__":
    url_inst = UrlShortner()
    long_url = sys.argv[1]
    url_inst.run_tests()
    url_inst.long_url = long_url
    print("tiny url for the requested URL is " + url_inst.run())


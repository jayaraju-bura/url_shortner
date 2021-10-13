"""
This script takes a long URL as input from the user through CLI and shortens it and writes to file
"""
import csv
import logging
import sys
import random

MAIN_URL_PREFIX = "https://shorturl.com/"
FILE_NAME = "database/tiny_urls.csv"
BASE_KEY = "ACEGJLUXY6789"
TEST_URLS = ["https://github.com/",
             "https://geeksforgeeks.org/",
             "https://hackerrank.com/",
             "https://twitter.com/",
             "https://economictimes.indiatimes.com/markets/stocks/stock-watch/tata-power-shares-up-8-58-as-nifty-gains/articleshow/86984317.cms"]


class UrlShortner:
    def __init__(self):
        self.long_url = None
        self.short_keys = []

    def short_url(self):
        """
        This method shortens the long url using the BASE_KEY by trial and error
        :return: returns the shortened URL
        """
        tiny_url = ''.join(random.choice(BASE_KEY) for x in range(0, len(BASE_KEY)))
        while tiny_url in self.short_keys:
            tiny_url = ''.join(random.choice(BASE_KEY) for x in range(0, len(BASE_KEY)))
        return MAIN_URL_PREFIX + tiny_url

    def search_url(self):
        """
        This method searches whether shortened url is already existed or not for
        requested long URL
        :return: returns the status whether or not shortened URL is found in the file
        """
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

        except IOError as error:
            logging.debug("Short URL for the requested long url doesn't exist")
            return url_found

    def write_to_file(self, short_url=None):
        """
        This method writes the shortened URL to file in the form of key-value pair
        key - long URL
        value - shortened URL
        :param short_url:
        """
        with open(FILE_NAME, 'a') as file:
            csv_writer = csv.writer(file, delimiter=':')
            csv_writer.writerow([self.long_url, short_url])

    def run(self):
        """
        This is the base method of this class, looks out for shortened URL
        is existing or not for requested long URL. if it is found returns it otherwise
        calls short_utl() method to create a tiny url for the long URL
        :return:
        """
        tiny_url = self.search_url()
        if tiny_url is None:
            tiny_url = self.short_url()
            self.write_to_file(short_url=tiny_url)
        logging.info("tiny url for the requested URL is " + tiny_url)
        return tiny_url

    def run_tests(self):
        """
        This method tests the functionality of the class by taking few websites as examples
        :return:
        """
        for test_url in TEST_URLS:
            self.long_url = test_url
            self.run()


if __name__ == "__main__":
    url_inst = UrlShortner()
    long_url = sys.argv[1]
    url_inst.run_tests()
    url_inst.long_url = long_url
    print("tiny url for the requested URL is " + url_inst.run())


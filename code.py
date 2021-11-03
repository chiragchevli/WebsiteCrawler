from urllib.request import urlopenfrom bs4 import BeautifulSoupimport stringimport argparseparser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True,  help="Get url from the cli")
parser.add_argument("-w", "--words", required=True, help="get wordlist from the cli")
args = parser.parse_args()

class HTTPRequest:
    def __init__(self,url,wordlist):
        html = urlopen(url).read()
        self.soup = BeautifulSoup(html, features="html.parser")
        self.__init__worddict(wordlist)
        self.__removeUnwanted()
        self.__makeLines()
        self.__countwords()
		
    def __init__worddict(self,wordlist):
        self.worddict = dict()
        for word in wordlist:
            wl = word.lower()
            self.worddict[wl] = {​"word": word, "count": 0}​
			
    def __removeUnwanted(self):
        for script in self.soup(["script", "style"]):
            script.extract()
        self.text = self.soup.get_text()
		
    def __makeLines(self):
        lines = (line.strip() for line in self.text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        chunks = [chunk.translate(str.maketrans('', '', string.punctuation)) for chunk in chunks if chunk]
        for chunk in chunks:
            for word in chunk.split(" "):
                if word.lower() in self.worddict:
                    self.worddict[word.lower()]["count"] +=  1    def __countwords(self):
        self.wl = ''        for w in self.worddict:
            k = self.worddict[w]["word"]
            v = self.worddict[w]["count"]
            self.wl += f'{​k}​: {​v}​\n'if __name__ == '__main__':
    url = args.url    wordlist = args.words.split(',')
    h = HTTPRequest(url,wordlist)
    print(h.wl)

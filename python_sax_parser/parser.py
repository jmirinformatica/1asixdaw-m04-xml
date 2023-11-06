import sys
from xml.sax import parse
from xml.sax.handler import ContentHandler

class MyParser(ContentHandler):

    def startElement(self, name, attrs):
        print(f"# BEGIN: <{name}>, {attrs.keys()}")

    def endElement(self, name):
        print(f"# END: </{name}>")

    def characters(self, content):
        if content.strip() != "":
            print(f"# CONTENT: {content}")

def parse_files(file_names):
    for file_name in file_names:
        if file_name.endswith(".xml"):
            print("#############################################################")
            print(f"# PARSE {file_name}")
            print("#############################################################")
            parse(file_name, MyParser())

if __name__ == "__main__":
    # crido a la funció parse amb els paràmetres
    parse_files(sys.argv)

from bs4 import BeautifulSoup
from markov_python.cc_markov import MarkovChain

#data_file = raw_input("Enter path to your file: ")
data_file = "data2.txt"
def read_data(data_file):
    data = ""
    with open(data_file, "r") as g:
        for line in g:
            data += line
    return data

def generate_data():
    raw_text = read_data(data_file)
    mc = MarkovChain()
    mc.add_string(raw_text)
    mcg = mc.generate_text()
    return mcg

def print_data():
    text = ""
    i = 0
    dot = "."
    while i < len(generate_data()):
        if i < len(generate_data()):
            text = text + str(generate_data()[i],)+" "
            i += 1

    print text[:1:].upper()+text[1::]+dot

### run section

        

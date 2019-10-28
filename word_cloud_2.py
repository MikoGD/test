"""
Program description: Implement word cloud
Author: Mikael Escolin
Date started: 26/10/19 22:39
"""

def main():
    """ Program will start here """
    WORD_CLOUD = WordCloud()
#END MAIN()

class WordCloud:
    """
    This class will make read a txt file.

    Count all the words and store frequency in a dictionary.

    A HTML file will then be created with each word and their font size will equal
    their frequency multiplied by 10.
    """
    dict_file = {}

    def __init__(self):
        # Create dictionar of words and their frequency from a txt file
        self.create_dict()
        # Create the HTML file
        self.create_html()

        for key in self.dict_file:
            print("Key: %s\nFrequency: %d\n" % (key, self.dict_file[key]))
    #END __init__()

    def create_dict(self):
        """
        Open a file and read it.

        Store the word in a dictionary:
            Key is the word
            Value is the frequency
        """
        try:
            with open("gettisburg.txt", "r") as file_txt:
                # Go through file line by line
                for line in file_txt:
                    line = line.lower()
                    line = line.split(" ")
                    # Go through line word by word
                    for word in line:
                        if word.find(".") > -1:
                            word = word[0:word.find(".")]
                        elif word.find(",") > -1:
                            word = word[0:word.find(",")]
                        elif word.find("\n") > -1:
                            word = word[0:word.find("\r\n")]
                        else:
                            word = word

                        if word.isalpha():
                            self.add_to_dictionary(word)
                        #END IF
                    #END INNER FOR
                #END FOR
            #END WITH
        except FileNotFoundError:
            print("File does not exits")
        #END TRY
    #END create_dict()

    def add_to_dictionary(self, word):
        """
        Store the word in a dictionary:
            Key is the word
            Value is the frequency
        """
        if word in self.dict_file:
            self.dict_file[word] += 1
        else:
            self.dict_file[word] = 1
        #END IF
    #END add_to_dictionary()

    def create_html(self):
        """
        Open new file to write to.

        Add the start of the HTML.

        Add the words with their styling.

        Add the end of the HTML.
        """

        html_tags_start = \
"""
<!DOCTYPE html>
<html>
<head lang=”en”>
<meta charset=”UTF-8”
<title>Tag Cloud Generator</title>
</head>
<body>
<div style=”text-align: center; vertical-align: middle; font-family: arial; color: white;\
            background-color: black; border: 1px solid black”>
"""

        html_tags_end = \
"""
</div>
</body>
</html>
"""

        with open("index.html", "w") as file_html:
            file_html.write(html_tags_start)

            for key in self.dict_file:
                value = self.dict_file[key]
                font_size = value * 10

                span_elemnent = "<span style=\"font-size: %dpx\">%s </span>" % (font_size, key)

                file_html.write(span_elemnent)
            #END FOR

            file_html.write(html_tags_end)
        #END WITH
    #END create_HTML()

if __name__ == "__main__":
    main()
#END IF

# TODO: 
# 1. Rewrite as class structure
# 2. Add new technique functions
# 3. Optimise import statements

import re
import pefile
import matplotlib.pyplot as plt



def get_strings(data, min_len=4):
    regex = b'[\x20-\x7e]{%d,}' % min_len
    return re.findall(regex, data)

def extract_strings_from_binary(binary_path, min_string_len=4):
    pe = pefile.PE(binary_path)
    ascii_strings = []
    for section in pe.sections:
        ascii_strings.extend(get_strings(section.get_data(), min_string_len))

    return [s.decode('utf-8', 'ignore') for s in ascii_strings]



def generate_word_cloud(strings_list):
    from wordcloud import WordCloud

    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = set(),
                min_font_size = 10).generate(' '.join(strings_list))

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def most_common(strings):
    from collections import Counter
    freqs= Counter(strings)
    count = 10 
    common = freqs.most_common(count)     #Add support for user defined value here

    word_x = list()
    count_y = list()
    
    for x, y in common:
        print(x, y)
        word_x.append(x)
        count_y.append(y)

    plt.title(str(count) + " most common strings in binary source")
    plt.scatter(word_x, count_y)
    plt.xticks(rotation=90)
    ax = plt.gca()
    ax.set_ylim([0, max(count_y)+1])
    plt.show()



def main(path, visualisation):    
    binary_path = path
    extracted_strings = extract_strings_from_binary(binary_path)

    if (visualisation == "-wordcloud"):
        generate_word_cloud(extracted_strings)

    elif (visualisation == "-most-common"):
        most_common(extracted_strings)
    
if __name__ == '__main__':
    main()
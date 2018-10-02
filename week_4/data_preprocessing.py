import re
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

def readFile(filename):
    f = open(filename, 'r', encoding='UTF-8')
    content = f.readlines()
    f.close()
    return content


def tokenization(content):
    # strip and replace space
    for i in range(len(content)):
        content[i] = content[i].strip()
        content[i] = content[i].replace(" ", "")
    #remove empty item
    content = list(filter(None, content))
    #join all list to string
    content = ''.join(content)
    #remove \t\n\r\f\v
    content = re.sub('[\t\n\r\f\v]', '', content)
    #remove punctuation marks
    puncs = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.。'
    content = re.sub('['+puncs+']', '', content)

    token_list = jieba.cut(content, cut_all=False)
    token_list = list(token_list)

    return token_list


def removeStopWord(token_list):
    #Read Stop Word List
    stop_word_list = readFile('stop-word-list.txt')
    for i in range(len(stop_word_list)):
        stop_word_list[i] = stop_word_list[i].rstrip('\n')
    # print(stop_word_list)
    #remove stop word from token_list
    token_list = [token for token in token_list if token not in stop_word_list]
    return token_list


def wordDict(token_list):
    wordDict = {}
    for w in token_list:
        if w in wordDict:
            wordDict[w] = wordDict[w] + 1
        else:
            wordDict[w] = 1
    return wordDict


def writeFile(filename, token_list):
    f = open(filename, 'w', encoding='UTF-8')
    for token in token_list:
        f.write("%s\n" % token)
    f.close()


def main():
    content = readFile('附錄.txt')
    token_list = tokenization(content)
    token_list = removeStopWord(token_list)
    word_Dict = wordDict(token_list)
    print(word_Dict)
    # writeFile('result.txt',token_list)


if __name__ == "__main__":
	main()

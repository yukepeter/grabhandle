# from bs4 import BeautifulSoup
import re
import urllib2
import json

url_list1 = ['https://twitter.com/QueenOfSass','https://twitter.com/?lang=en','https://twitter.com/SportMan']
url_list = ['https://www.pastemagazine.com/articles/2017/01/the-75-best-twitter-accounts-of-2016-1.html']



#def save_dict(obj, name):
#    with open('obj/'+ name + '.pkl', 'wb') as f:
#        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def crawlWeb(url_list):
    url_handle_dict = {}
    reg1 = r'(?:@[\w_]+)'  
    for i in url_list:
        response = urllib2.urlopen(i)
        html_doc = response.read()
        handle_list = re.findall(reg1, html_doc)
        url_handle_dict[i] = handle_list
        #print handle_list
    return url_handle_dict
    #To Store page as a .html file
    #with open('temp1.html','w') as f2:
        #f2.write(html_doc)
        
if __name__ == "__main__":
    url_handle_dict = crawlWeb(url_list)
    json.dump(url_handle_dict, open("text.txt",'w'))

#save_dict(url_handle_dict,'url_handle')

# with open('url_handle.html','w') as f1:
#     f1.write(url_handle_dict)

# soup = BeautifulSoup(html_doc)
# movie_table = soup.find_all('table')[0]
# for row in movie_table.find_all('tr'):
# row.a.get('href')

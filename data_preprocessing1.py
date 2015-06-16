#encoding=utf-8
'''
Created on 2014-9-10

@author: 张江涛
'''
import codecs
import re
import json
import os

class preProcessing():
    def __init__(self,in_dir,out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir
      
    def split_comment(self):
        if not os.path.isdir(self.out_dir) :
            os.mkdir(self.out_dir)
        for name in os.listdir(self.in_dir):
            fi = codecs.open(self.in_dir+name,'r','utf-8' )
            title = ""
            movie = ""
            movie_dir = self.out_dir
            for line in fi:
                if line.startswith("Title:"):
                    title = line.split(":::")[0][6:]
                    movie_id = line.split(":::")[1]
                    movie_dir = self.out_dir+title+'-' + movie_id + '/'
                    if not os.path.isdir(movie_dir) :
                        os.mkdir(movie_dir)
                    
                if '{' in line:
                    main = line[line.find('{'):]
                    try:
                        comment_dict = json.loads(main)
                    except:
                        print("error line: " +line)
                        continue
                    source = comment_dict.get("dtf_s","")
                    type =comment_dict.get("dtf_t","")
                    fw = codecs.open(movie_dir+type+'-'+source,'a','utf-8')
                    fw.write(line)
                    fw.close()

            fi.close()
            
    def load_data(self,in_dir,out_dir):
        for sub_dir in os.listdir(in_dir):
            print(sub_dir)
            if not os.path.isdir(out_dir + sub_dir ):
                    os.mkdir(out_dir + sub_dir)
            for name in os.listdir(in_dir + sub_dir):                
                print(name)
                fi = codecs.open(in_dir+sub_dir+'/' +name, 'r', "utf-8")
                fw = codecs.open(out_dir+sub_dir+'/' +name, 'w', "utf-8")
                for line in fi:
                    print(line)
                    fw.write(line)
                    break
        
if __name__ == '__main__':
    process = preProcessing("./data/test/",'./data/split/')
    process.split_comment()
#     process.load_data('./data/split/','./data/output/')
    
                
                
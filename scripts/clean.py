# input json file,  return cleaned json file
import json
import argparse
import pandas as pd
import random

def merge(file,data):    
    f=open(file)
    while True:
        line=f.readline()
        try:
            data.append(json.loads(line))

        except Exception:
            pass
            ## skip invalid json format
        #break if eof
        if not line:
            break
    f.close
    return data

def cleanData(data):
    #selecting contents to output
    content=[]
    randonLine=random.sample(range(1, len(data)), 1000)
    for i in randonLine:
        content.append(data[i])

    titles=[]
    authors=[]
    for c in content:
        titles.append(c['data']['title'])
        authors.append(c['data']['name'])

    return [titles,authors]

def filterData(titles,authors):
    removeIndex=[]

    for index in range(len(titles)):
        if not (('Trump' in titles[index]) or ('Biden' in titles[index])):
            removeIndex.append(index)

    titleList=[]
    nameList=[]
    for i in range(1000):
        if i not in removeIndex:
            titleList.append(titles[i])
            nameList.append(authors[i])
        
    return [titleList,nameList]

def writeData(titles,authors,fileOut):
    ## create dataframe for Names and Titles
    df=pd.DataFrame(columns=['Name','Title','Coding'])
    df['Name']=authors
    df['Title']=titles
    df['Coding']=' '
    ## save in tsv
    df.to_csv(fileOut, index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('f1')
    parser.add_argument('f2')
    parser.add_argument('f3')    
    parser.add_argument('fileOut')
    args = parser.parse_args()
    file1=args.f1
    file2=args.f2
    file3=args.f3
    fileOut=args.fileOut

############################################

    ## data = merged contents over 3 days
    data=[]
    data=merge(file1,data)
    data=merge(file2,data)
    data=merge(file3,data)
    ## titles and authors with length 1000
    titles=[]
    authors=[]
    [titles,authors]=cleanData(data)
    
    '''
    keep posts with titles containing 'Trump' or 'Biden'
    case sensitive 
    '''

    [titles,authors]=filterData(titles,authors)

    writeData(titles,authors,fileOut)


if __name__ == "__main__":
    main()

import collections
def count(obj):
    with open(obj,'r') as f:
        data=f.read()
    data=data.split(' ')
    str=''
    counter=collections.Counter(data)
    for keys,values in counter.items():
       print(keys,end='\t')
       print(values,end='\t')
if __name__ == '__main__':
    count('foruse.txt')

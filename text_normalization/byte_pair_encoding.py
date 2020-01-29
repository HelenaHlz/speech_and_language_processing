import re,collections

def get_stats(vocab):
    '''
    defaultdict: means that if a key is not found in the dictionary,
     then instead of a KeyError being thrown, a new entry is created.
     The type of this new entry is given by the argument of defaultdict.

     dict.items() 以列表返回可遍历的(键, 值) 元组数组

     split:Split a string into a list where each word is a list item

     python tuple same with list , but elements in tuple can't be changed
     tup1 = ('Google', 'Runoob', 1997, 2000)
     tup3 = "a", "b", "c", "d"   #  不需要括号也可以

     dist pairs.keys tuple(symbol i,symbol i+1)

     vocab 词和对应的词频
     初始化一个空的dict pairs避免抛出key error
     遍历单词和词频
     每个单词拿到字符
     遍历前后两个字符 求词频总数
     返回的pairs dict key是一前一后字符元祖 value是对应词频
    '''
    pairs = collections.defaultdict(int)
    for word,freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return  pairs

def merge_vocab(pair,v_in):
    '''
    ' '.join(pair)把pair里面用' '连起来
    re.escape(pattern) ，有的时候我们需要使用一些特殊符号如”$ * . ^”等的原意，可以对字符串中所有可能被解释为正则运算符的字符进行转义
    re.compile 该函数根据包含的正则表达式的字符串创建模式对象得到pattern。可以实现更有效率的匹配.而使用compile完成一次转换之后，在每次使用模式的时候就不用重复转换
    pattern.sub(rep,string) 在word里面 找到bigram 词频最多的两个连起来的字符 替换成把它们连起来''.join操作
    v_out 就是拼接之后的字符字典 词频
    '''
    v_out={}
    bigram = re.escape(' '.join(pair))
    p=re.compile(r'(?<!\S)'+bigram+r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair),word)
        v_out[w_out] = v_in[word]
    return v_out

vocab={'l o w </w>':5, 'l o w e s t </w>':2,'n e w e r </w>':6,'w i d e r </w>':3, 'n e w </w>':2}
'''迭代几次 输出几个'''
num_merges=1000

for i in range(num_merges):
    pairs = get_stats(vocab)
    '''
    本函数是迭代对象iterable进行比较，找出最大值返回。当key参数不为空时，就以key的函数对象为判断的标准。
    pairs.get(p in pairs)=> p.value 得到词频最大那个元祖
    '''
    best = max(pairs,key=pairs.get)
    vocab = merge_vocab(best,vocab)
    print(best)

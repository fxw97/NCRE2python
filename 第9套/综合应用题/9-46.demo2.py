fi = open('关山月-诗歌.txt','r')
fo = open('关山月—反转.txt','w')
txt = fi.readlines()
ls = txt[::-1]
fo.writelines(ls)
fi.close()
fo.close()
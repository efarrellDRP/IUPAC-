import re
import tkinter
carbon_dic={re.compile(r"[m]eth"):1,re.compile(r"[^Mm]eth"):2, re.compile("r^eth"):2,re.compile(r"prop"):3,
            re.compile(r"but"):4,re.compile(r"pen"):5,re.compile(r"hex"):6,
            re.compile(r"hep"):7,re.compile(r"oct"):8,re.compile(r"non"):9,
            re.compile(r"dec"):10,re.compile(r"und"):11,re.compile(r"dod"):12}
prefix_dic={re.compile(r"di"):1,re.compile(r"tri"):2,re.compile(r"tetra"):3}
def carbonCheck(mol_name):
    prefix_list=[]
    chains_list=[]
    carbon_count=[]
    check=0
    comp_check=0
    for i in carbon_dic:
        if i==re.compile("r^eth"):
            if re.match(i,mol_name):
                carbon_count.append(carbon_dic[i])

        regexes=[]
        mol_check=0 # determines how many of each lengthed chain appear in the molecule
        prefix_check=''
        prefix_count=0
        if re.findall(i,mol_name):

            mol_check=len(re.findall(i,mol_name))
            for k in prefix_dic:
                if i==re.compile(r"[^Mm]eth"):
                    s=i.pattern
                    s=s[5:]
                    prefix_check=re.compile(r'{}{}'.format(k.pattern,s))
                else:
                    prefix_check=re.compile(r'{}{}'.format(k.pattern,i.pattern))


                if re.findall(prefix_check,mol_name):
                    check+=1
                    mol_check=mol_check+prefix_dic[k]

            for j in range (mol_check):
                chains_list.append(i) # appends that chain for as many times it appears in the name


    for i in chains_list:
        carbon_count.append(carbon_dic[i])
    carbon_count.sort(reverse=True)

    return carbon_count





class Carbon_Chain(object):
    def __init__(self,name):
        self.name=name
    def count (self, count):
        cobject_list=[]
        j=0
        for i in range (count):
            j=i+1
            carbon_name= 'C'+str(j)
            c=Carbon(carbon_name)
            cobject_list.append(c.name)
        return cobject_list

class Carbon (object):
    def  __init__(self,name):
        self.name=name
def main():
    c_count=carbonCheck(raw_input("Type your molecule: "))
    del carbon_dic[re.compile("r^eth")]
    c_list=[]
    for i in c_count:

        for key,value in carbon_dic.iteritems():

            if i==value:

                c_list.append(Carbon_Chain(key.pattern).count(i))
    print c_list

main()

#print carbonCheck('18-bromo-12,11,10-tributyl-11-chloro-4,8-diethyl-5-hydroxy-15-methoxy')

import re
import Tkinter
import tkMessageBox
chains_list=[]
top = Tkinter.Tk()
T = Tkinter.Canvas(top, height=500, width=500)
carbon_dic={re.compile(r"[m]eth"):1,re.compile(r"[^Mm]eth"):2, re.compile(r"^eth"):2,re.compile(r"prop"):3,
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

    return chains_list

def parent_branch(mol_name, carbon_list):
    bc_object_list=[]
    rx=r"\d"
    digit_RE=re.compile(rx)

    lis_dig=re.findall(digit_RE,mol_name)
    check=0
    for i in lis_dig:

        for c in carbon_list:
            if i in c.name:
                c.branched=True
                c.branches+=1


    return carbon_list





class Carbon_Chain(object):
    def __init__(self,name,length):
        self.name=name
        self.length=length

def create (length):
    cobject_list=[]
    j=0
    x_i=50
    y_i=250
    x_f=55
    y_f=255

    atom_coord=x_i,y_i,x_f,y_f
    n_y=5




    for i in range (length):
        if i>0:


            j=i+1
            carbon_name= 'C'+str(j)
            n_y=n_y*-1

            x_i+=30
            y_i=y_i+(n_y*(-1))
            x_f+=30
            y_f=y_f+(n_y*(-1))

            atom_coord=x_i,y_i,x_f,y_f

            c=Carbon(carbon_name,atom_coord,T.create_oval(atom_coord, fill="black"),False,0,0)

            cobject_list.append(c)
        else:
            j=i+1
            carbon_name= 'C'+str(j)
            c=Carbon(carbon_name,atom_coord,T.create_oval(atom_coord, fill="black"),False,0,0)
            cobject_list.append(c)




    return cobject_list

def create_bond(initial_carbon,next_carbon):
    x_i,y_i,x_f,y_f=initial_carbon.atom_position
    n_xi,n_yi,n_xf,n_yf=next_carbon.atom_position
    i_x=(x_i+x_f)/2
    i_y=(y_i+y_f)/2
    ni_x=((n_xi+n_xf)/2)
    ni_y=((n_yi+n_yf)/2)
    b_coord=(i_x,i_y,ni_x,ni_y)
    return T.create_line(b_coord)

def create_branch(initial_carbon,length):
    branch_ls=[]
    n_x=5
    x_i,y_i,x_f,y_f=initial_carbon.atom_position

    n_xi=0
    n_yi=0
    n_xf=0
    n_yf=0
    k=0
    for i in range(length):

        n_x=n_x*-1
        x_i=x_i+n_x
        x_f=x_f+n_x
        y_i=y_i-30
        y_f=y_f-30
        k+=1
        carbon_name= 'C'+str(k)

        atom_coord=x_i,y_i,x_f,y_f
        c=Carbon(carbon_name,atom_coord,T.create_oval(atom_coord, fill="black"),False,0,0)
        branch_ls.append(c)
        if i==0:
            create_bond(initial_carbon,c)

    return branch_ls

def branch_check(mol_name,chain_list,chain_name,carbon):
    check=False
    b_count=0
    if carbon.branched==False or 3>len(chain_list):


        return False
    else:
        c_number=carbon.name[1:]
        c_re=r"{}[,|-]*[^{}]*[{}]"
        for chain in chain_list[1:]:

            re_chain_name=re.sub(r"\[m\]",'m',chain_name)
            re_chain_name=re.sub(r"\[\^Mm\]",'',re_chain_name)
            re_chain_name_l=re.sub(r"\[\^Mm\]",'',chain.name)
            re_chain_name_l=re.sub(r"\[m\]",'m',re_chain_name_l)
            print(chain.name,chain_name)
            if chain.name!=chain_name:
                print (re_chain_name_l,re_chain_name)
                c_regex=re.compile(c_re.format(c_number,re_chain_name_l,re_chain_name))
                print c_re.format(c_number,re_chain_name_l,re_chain_name)
                if re.search(c_regex,mol_name) and carbon.b_check!=carbon.branches:
                    check=True
                    print check
                    carbon.b_check+=1


        if check==True:
            return True











class Carbon (object):
    def  __init__(self,name,atom_position,form,branched,branches,b_check):
        self.name=name
        self.atom_position=atom_position
        self.form=form
        self.branched=branched
        self.branches=branches
        self.b_check=b_check





def main():
    parent=False
    carbon_count=[]
    c_list=[]
    parent_list=[]
    branch_list=[]
    full_list=[]
    mol_name=raw_input("Type your molecule: ")
    c_count=carbonCheck(mol_name)


    for i in c_count:
        carbon_count.append(carbon_dic[i])
    carbon_count.sort(reverse=True)


    del carbon_dic[re.compile(r"^eth")]


    for i in carbon_count:


        for key,value in carbon_dic.iteritems():


            if i==value:
                chain_name=key.pattern
                c_list.append(Carbon_Chain(chain_name,i))

    for chain in c_list:

        if parent==False:

            parent_list=(parent_branch(mol_name,create(chain.length)))


            parent=True

        else:
            for c in parent_list:


                    if branch_check(mol_name,c_list,chain.name,c):
                            print c.name

                            branch_list.append(create_branch(c,chain.length))

                    #print carbon.name,chain.length
    full_list.append(parent_list)
    full_list=full_list+branch_list
    print parent_list
    print branch_list
    print full_list
    for chain in full_list:
        if len(chain)>1:
            for v, w in zip(chain[:-1], chain[1:]):
                create_bond(v,w)





        #for carbon in cobject_list:
        #        branches=branch(mol_name,chain.length,carbon)
        #        if branches==True:
        #            branched=True
        #else:
        #    cobject_list=chain.create_branch(chain.length)







    T.pack()
    top.mainloop()
    #print cname_list
    #print c_list


main()

carbon_dic={'meth':1,'eth':2,'prop':3,'but':4,'pen':5,'hex':6,'hep':7,'oct':8,'non':9,'dec':10,'und':11,'dod':12}
#list that detects 12 kinds of carbon chains of varying length
prefix_dic=['di','tri','tetra']
def carbonCheck(mol_name):
    prefix_list=[]
    chains_list=[]
    carbon_count=[]
    #list initializers

    meth_check=mol_name.count('meth')
    eth_check=mol_name.count('eth')
    total_check=eth_check-meth_check
    #neccesary check to determine between methyl and ethyl groups, can't simply use in func due to 'eth' being in 'meth'
    #Works by counting the number of meth and eth appearances in the initial input. Ethyl will always appear just as many
    #times as methyl. The function will append both a methyl and ethyl group for just one appearance of methyl.
    #So if total_check is non-zero that means there's at least one ethyl group. If total_check returns
    #zero than that means there are no ethyl groups.

    if total_check==0:
        meth_prefix=''
        prefix_amount=0
        for k in prefix_dic:
            print(k)
            prefix_amount+=1
            meth_prefix=k+'meth'
            print (meth_prefix)
            if meth_prefix in mol_name:
                meth_check=meth_check+prefix_amount
        for i in range(meth_check):
            chains_list.append('meth')


    if total_check>0: #this ensures the proper amount of ethyl groups are appended to the chains_list
        meth_prefix=''
        eth_prefix=''
        prefix_amount=0
        ethyl_amount=0
        for k in prefix_dic:
            prefix_amount+=1
            meth_prefix=k+'meth'
            if meth_prefix in mol_name:
                meth_check=meth_check+prefix_amount
        for j in prefix_dic:
            ethyl_amount+=1

            eth_prefix=j+'eth'

            if eth_prefix in mol_name:
                total_check=total_check+ethyl_amount

        for i in range(total_check):
            chains_list.append('eth')
        for i in range(meth_check):
            chains_list.append('meth')
    #

    for i in carbon_dic:
        mol_check=0 # determines how many of each lengthed chain appear in the molecule
        prefix_check=''
        prefix_count=0
        if i in mol_name and i!='meth' and i!='eth':
            mol_check=mol_name.count(i)
            for k in prefix_dic:
                print(i)
                print(k)
                prefix_count+=1
                prefix_check=k+i
                print (prefix_check)
                if prefix_check in mol_name:
                    mol_check=mol_check+prefix_count
            for j in range (mol_check):
                chains_list.append(i) # appends that chain for as many times it appears in the name
            print(chains_list)

    for i in chains_list:
        carbon_count.append(carbon_dic[i])


    carbon_count.sort(reverse=True)





    return carbon_count

#class Carbon_Chain:
#    def __init__(self, carbons):
#        carbons=
 #def main():
#     c_count=carbonCheck(raw_input("Type your molecule: "))
#     c_list
#     for i in c_count:
#         c_list.append(Carbon_Chain(i))


print carbonCheck('18-bromo-12,11,10-tributyl-11-chloro-4,8-diethyl-5-hydroxy-15-methoxy')

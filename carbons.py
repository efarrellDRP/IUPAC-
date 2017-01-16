carbon_dic={'meth':1,'eth':2,'prop':3,'but':4,'pen':5,'hex':6,'hep':7,'oct':8,'non':9,'dec':10,'und':11,'dod':12}

def carbonCheck(mol_name):
    chains_list=[]
    carbon_count=[]

    #list initializers
    meth_check=mol_name.count('meth')
    eth_check=mol_name.count('eth')
    total_check=eth_check-meth_check
    #neccesary check to determine between methyl and ethyl groups, can't simply use in func due to 'eth' being in 'meth'


    if total_check==0:
        for i in range(meth_check):
            chains_list.append('meth')

    if total_check>0:
        for i in range(total_check):
            chains_list.append('eth')
        for i in range(meth_check):
            chains_list.append('meth')
    #appends eth or meth to the list

    for i in carbon_dic:
        mol_check=0 # determines how many of each lengthed chain appear in the molecule

        if i in mol_name and i!='meth' and i!='eth':
            mol_check=mol_name.count(i)
            for j in range (mol_check):
                chains_list.append(i) # appends that chain to the list
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

print carbonCheck('propane methane propane')
print carbonCheck('ethane methane ethane methane')

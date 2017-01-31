import cgi
string="Hello there {username}"
params= {'username':'the boss'}


print (string.format(**params))

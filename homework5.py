immutable_var=(1,2,'a','b')
print(immutable_var)
#immutable_var[0] = 2 # менять переменные кортежа нельзя , если он не в списке
#print(immutable_var)
mutable_list=([1,2,3,4],12)
mutable_list[0][2]=5
print(mutable_list)

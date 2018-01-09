my_list=list(range(0,100))

fp= open("e:\\file1.txt","w")

for each in my_list:
    if each<2:
         fp.write("{}\n".format(each))
    else:
        for i in range(2,each):
            if each%i==0:
                break;
        else:
            fp.write("{}\n".format(each))

fp.close()
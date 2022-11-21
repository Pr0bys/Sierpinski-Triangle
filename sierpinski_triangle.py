n=int(input("Enter triangle level(recommend 1-8):"));
n=2**(n+1);
length = n+n-1;
k = 2;
result_for_show = [[length//2], [length//2-1, length//2+1], [length//2-2, length//2+2], [length//2-2-1, length//2-2+1, length//2+2-1, length//2+2+1]]

print(result_for_show)

temp_array = []
temp_for_show = result_for_show.copy();

#Initial point minus Last from point from right or left
z=abs(result_for_show[0][0]-result_for_show[len(result_for_show)-1][len(result_for_show[len(result_for_show)-1])-1])+1;
while(result_for_show[len(result_for_show)-1][len(result_for_show[len(result_for_show)-1])-1]+1<length):
    for points in result_for_show:
        temp_array = [i-z for i in points];
        temp_array += [i+z for i in points];
        temp_for_show.append(temp_array)
    result_for_show=temp_for_show.copy();
    #Initial point minus Last from point from right or left
    z=abs(result_for_show[0][0]-result_for_show[len(result_for_show)-1][len(result_for_show[len(result_for_show)-1])-1])+1

for points in result_for_show:
    print_line="";
    x=0;
    temp_array=[];
    while(x<length):
        if(x in points):
            print_line+="*";
        else:
            print_line+=" ";
        x+=1;
    print(print_line);
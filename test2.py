import read_names
import sys
read_names.read_from_file("top_names_1880_to_2014.txt")
def name_stats(i):  #prints the rank, name, count, and percentages for the name of a given index
    sum_counts = sum(f_counts)
    print i+1, "%s %5d %7.3f %7.3f" %(f_names[i] + (" " * (11-(len(f_names[i])+2))), f_counts[i], (float(f_counts[i])/int(f_counts[0]))*100, (float(f_counts[i])/sum_counts)*100)
    
def female_info(year, name):  #prints the top and 250th female names for the inputted year, as well as information about the inputted female name.
    
    (f_names,f_counts) = read_names.top_in_year(year, 'f')
    sum_counts = sum(f_counts)
    
    i = f_names.index(name)
    if name in f_names == False:
        print "The name %s is not in the top 250 female names for %d." %(name, year)
    
            
        
    print "Data about female names"
    print "Top ranked name %s" %f_names[0]
    print "250th ranked name %s" %f_names[249]
    name_stats(i-2)
    name_stats(i-1)
    name_stats(i)
    name_stats(i+1)
    name_stats(i+2)
    
name = "Emma"
year = 2014


(f_names,f_counts) = read_names.top_in_year(year, 'f') 
print name in f_names
female_info(year, name)
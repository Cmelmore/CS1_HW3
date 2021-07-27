"""
Author: Christina Elmore
Section Number: 02
RIN: 661542904
Assignment: HW 3 Part 1
Purpose: Asks the user for a year within range, asks the user for a female name and finds the index of that name in the list, outputs the top ranked and 250th ranked female and male names, and then does the same for a male name.
"""

import read_names
import sys

def name_stats_f(i):  #prints the rank, name, count, and percentages for the female name of a given index
    sum_counts = sum(f_counts)
    print "%s%d %s   %5d %7.3f %7.3f" %(" " * (3-len(str(i))), i+1, f_names[i] + (" " * (11-(len(f_names[i])+2))), f_counts[i], (float(f_counts[i])/int(f_counts[0]))*100, (float(f_counts[i])/sum_counts)*100)
    
def name_stats_m(i):  #prints the rank, name, count, and percentages for the male name of a given index
    sum_counts = sum(m_counts)
    print "%s%d %s   %5d %7.3f %7.3f" %(" " * (3-len(str(i))), i+1, m_names[i] + (" " * (11-(len(m_names[i])+2))), m_counts[i], (float(m_counts[i])/int(m_counts[0]))*100, (float(m_counts[i])/sum_counts)*100)
    
def female_info(year, name):  #prints the top and 250th female names for the inputted year, as well as information about the inputted female name.
    
    (f_names,f_counts) = read_names.top_in_year(year, 'f')
    print "Data about female names"
    print "Top ranked name %s" %f_names[0]
    print "250th ranked name %s" %f_names[249]    
    if (name in f_names) == False:
        print "%s is not in top 250." %(name)        
    else:
        i = f_names.index(name)
        if 247 >= i >= 2:
            name_stats_f(i-2)
            name_stats_f(i-1)
            name_stats_f(i)
            name_stats_f(i+1)
            name_stats_f(i+2)
        elif i == 248:
            name_stats_f(i-2)
            name_stats_f(i-1)
            name_stats_f(i)
            name_stats_f(i+1)
        elif i == 249:
            name_stats_f(i-2)
            name_stats_f(i-1)
            name_stats_f(i)        
        elif i == 1:
            name_stats_f(i-1)
            name_stats_f(i)
            name_stats_f(i+1)
            name_stats_f(i+2)
        elif i == 0:
            name_stats_f(i)
            name_stats_f(i+1)
            name_stats_f(i+2)        

def male_info(year, name):  #prints the top and 250th male names for the inputted year, as well as information about the inputted male name.
    (m_names,m_counts) = read_names.top_in_year(year, 'm')
    print "Data about male names"
    print "Top ranked name %s" %m_names[0]
    print "250th ranked name %s" %m_names[249]
    if (name in m_names) == False:
        print "%s is not in top 250." %(name)
    else: 
        i = m_names.index(name)
        if 247 >= i >= 2:
            name_stats_m(i-2)
            name_stats_m(i-1)
            name_stats_m(i)
            name_stats_m(i+1)
            name_stats_m(i+2)
        elif i == 248:
            name_stats_m(i-2)
            name_stats_m(i-1)
            name_stats_m(i)
            name_stats_m(i+1)
        elif i == 249:
            name_stats_m(i-2)
            name_stats_m(i-1)
            name_stats_m(i)
        elif i == 1:
            name_stats_m(i-1)
            name_stats_m(i)
            name_stats_m(i+1)
            name_stats_m(i+2)
        elif i == 0:
            name_stats_m(i)
            name_stats_m(i+1)
            name_stats_m(i+2)        

read_names.read_from_file("top_names_1880_to_2014.txt")
year = int(raw_input("Enter the year to check => "))
print year
if 1880 > year or year > 2014:
    print "Year must be at least 1880 and at most 2014"
    sys.exit()
print ""
f_name = raw_input("Enter a female name => ")
print f_name
(f_names,f_counts) = read_names.top_in_year(year, 'f')
female_info(year, f_name)
print ""

m_name = raw_input("Enter a male name => ")
print m_name
(m_names,m_counts) = read_names.top_in_year(year, 'm')
male_info(year, m_name)
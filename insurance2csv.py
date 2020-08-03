#!/usr/bin/env python
import csv
import insurance2csv_config as config 
import sys

auto = "input/Homework - Auto Insurance.csv"
home = "input/Homework - Home Insurance.csv"
inputs = auto, home 
fieldnames = ['Provider Name','CampaignID','Cost Per Ad Click','Redirect Link','Phone Number','Address','Zipcode']       

def write_csv():
    with open("output/out.csv", "w", newline="") as out:   
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        
        for filename in inputs:
            with open(filename, "r", newline="") as ins_csv:
                reader = csv.DictReader(ins_csv)
                
                for line in reader:
                    new_line = config.UniformRow(fieldnames)
                    
                    new_line.add(line)                      #adding new line to dict
                    new_line.normalize()                    #trimming 
                    try:
                        new_line.check_instance_type()      #break and report if types don't match
                        new_line.set_new_type()             #try to set new types (CPC => float)
                        writer.writerow(new_line.new_row)            
                    except:
                        print('Offending data: ' + str(new_line.new_row))
                        next
                    

write_csv()

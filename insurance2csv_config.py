#!/usr/bin/env python 

class UniformRow():
    
    def __init__(self, fieldnames):
        self.new_row = dict()
        for name in fieldnames:
            self.new_row[name] = None

    def add(self, row):
        
        for k in row.keys():
            if k in self.new_row: 
                self.new_row[k] = row[k]
            else: 
                next

    def normalize(self):
        #trim up excessive quotes
        for k in self.new_row.keys():
            if self.new_row[k] == None:
                next
            else:
                self.new_row[k] = self.new_row[k].replace('"', '') #smarter replace here for punctuations
                if self.new_row[k] == '':
                    self.new_row[k] = None
                else:
                    next

    def check_instance_type(self):
        #check for null/empty before writing (phone number excluded)
        for k in self.new_row.keys():
            if k == 'Phone Number':
                next
            elif isinstance(self.new_row[k], type(None)):  
                raise TypeError


    def set_new_type(self):
        #set CPC as float
        try: 
            self.new_row['Cost Per Ad Click'] = float(self.new_row['Cost Per Ad Click'])
            return self.new_row
        #report non-convertibles 
        except:
            raise TypeError


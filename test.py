#!/usr/bin/env python
import unittest
from insurance2csv_config import UniformRow
fieldnames = ['Provider Name','CampaignID','Cost Per Ad Click','Redirect Link','Phone Number','Address','Zipcode']


class TestUniformRow(unittest.TestCase):
    
    def setUp(self):
        self.test_row = UniformRow(fieldnames)

    def tearDown(self):
        pass

    def test_add(self):
        #check dict for proper value set, only include matching kvs
        std =   {'Provider Name':'Texas Homes','CampaignID':'HOME8','Cost Per Ad Click':'1.07','Redirect Link':'txhomes.com',\
                'Phone Number':'1234567','Address':'200 Guadalupe St','Zipcode':'74389'}

        extra = {'Provider Name':'Texas Homes','CampaignID':'HOME8','Cost Per Ad Click':'1.07','Redirect Link':'txhomes.com',\
                'Phone Number':'1234567','Address':'200 Guadalupe St','Zipcode':'74389','Time Zone':'PST'}

        extra_row = self.test_row
        extra_row.add(extra)

        self.assertEqual(extra_row.new_row, std)

    def test_normalize(self):
        
        test_row = self.test_row

        quotes = {'Provider Name': '""""'}
        no_quotes = {'Provider Name': 'Texas Homes'}

        test_row.new_row['Provider Name'] = quotes['Provider Name']
        test_row.normalize()
        #test removal of quotes
        self.assertEqual(test_row.new_row['Provider Name'], None)

        test_row.new_row['Provider Name'] = no_quotes['Provider Name']
        test_row.normalize()
        #test removal of quotes
        self.assertEqual(test_row.new_row['Provider Name'], 'Texas Homes')

    
    def test_set_new_type(self):

        test_row = self.test_row

        str_to_int = {'Cost Per Ad Click':'1.05'}

        test_row.add(str_to_int)
        test_row.set_new_type()

        self.assertIsInstance(test_row.new_row['Cost Per Ad Click'], float)


if __name__ == '__main__':
    unittest.main()
# The Zebra Interview Assignment - insurance2csv.py

The goal of the exercise was to combine two given CSVs into one CSV with schema as described in the instructions. Any rows with non-conforming data was to be excluded and reported. The new unified CSV is written to the_zebra/output/out.csv


##Setup

This code was tested on Python 3.7. 

To run the script, pull down a copy of the repo and run from the the_zebra/ dir:

```python3 insurance2csv.py```

This will blend the two CSVs into one `out.csv` file. If any data is non-conforming it will be reported in the console. 

##Testing

To run the tests, run from the the_zebra/ dir:

```python3 test.py```

The tests currently execute a few rudimentary assertions on all methods in the UniformRow class. 


##Thoughts

There is definitely room here to add more tests, particularly around the data type setting and normalization methods. 

The current strategy for removing extraneous quotes could also be expanded to trim any extra punctuations, further clean casing, etc.






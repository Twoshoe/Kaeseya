#!/usr/bin/env python3
'''Create a JSON document of location data.

Take, as input, a text file of the form:
Account Name
Location 1
Location 2
Location 3

Generate, as output, a JSON object of the form:
[
   {
       "AccountName": <Account Name>,
       "LocationName": <Location>,
       "isMain": <Boolean>
   },
   ...
]
'''

import argparse
import json


def main():
    PARSER = argparse.ArgumentParser(description='Convert location text files to JSON',
                                     epilog='Redirect stdout to a file if needed')
    PARSER.add_argument('input_file', metavar='FILE', type=str,
            help='Path to input file')
    ARGS = PARSER.parse_args()

    account = ''
    data = []

    with open(ARGS.input_file, 'r') as fp:
        account = fp.readline().strip('\n')
        data = [{"AccountName": account, "LocationName": line.strip('\n'), "isMain": "false"} for line in fp]

    print(json.dumps(data, indent='\t'))


if __name__ == '__main__':
    main()


# vim: tabstop=4 softtabstop=4 shiftwidth=4 expandtab

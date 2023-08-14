"""
This module contains From, To, CC, BCC mails List
"""

import csv


class EmailList:

    _FROM_LIST = []
    _TO_LIST = []
    _CC_LIST = []
    _BCC_LIST = []
    

    def __init__(self):
        pass


    def set_Email_lists_csv(self, from_csv, to_csv, cc_csv, bcc_csv):
        self._FROM_LIST = self._tolower_parse(self, from_csv)
        self._TO_LIST = self._tolower_parse(self, to_csv)
        self._CC_LIST = self._tolower_parse(self, cc_csv)
        self._BCC_LIST = self._tolower_parse(self, bcc_csv)

    def get_from_list_all(self):
          # print(f'_FROM_LIST {str(self._FROM_LIST)}')
          return self._FROM_LIST

    def get_from_list_index(self, index):
        return self._get_index_list(self, index,self._FROM_LIST)


    def get_to_list_all(self):
        # print(f'_TO_LIST {str(self._TO_LIST)}')
        return self._TO_LIST


    def get_to_list_index(self, index):
        return self._get_index_list(self, index,self._TO_LIST)


    def get_cc_list_all(self):
        # print(f'_CC_LIST {str(self._CC_LIST)}')
        return self._CC_LIST


    def get_cc_list_index(self, index):
        return self._get_index_list(self, index,self._CC_LIST)


    def get_bcc_list_all(self):
        # print(f'BCC_LIST {str(self._BCC_LIST)}')
        return self._BCC_LIST
    

    def get_bcc_list_index(self, index):
       return self._get_index_list(self, index,self._BCC_LIST)


    def _tolower_parse(self, list):
        # print(f'input list {list}')
        base = []
        if list:
           if "," in list: 
                parse = list.lower().split(",")
                for item in parse:
                    item = item.strip()
                    if item and (item not in base):
                        base.append(item)
                    
           else:
                base=[list.lower()]

        # print(f'putpt list {str(base)}')
        return base

    def _get_index_list(self, index, list):
        if (index >= len(list)):
            return ""
        else:
            return list[index]

    


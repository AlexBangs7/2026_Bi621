#!/usr/bin/env Python


DNAbases = set('ATGCNatcgn')
RNAbases = set('AUGCNaucgn')
if __name__ is "__main__":
    def validate_base_seq(seq,RNAflag=False):
        '''This function takes a string. Returns True if string is composed
        of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
        return set(seq)<=(RNAbases if RNAflag else DNAbases)

assert validate_base_seq("AATAGAT") == True, "Validate base seq does not work on DNA"
assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
assert validate_base_seq("Hi there!") == False, "Validate base seq fails to recognize nonDNA"
assert validate_base_seq("Hi there!", True) == False, "Validate base seq fails to recognize nonDNA"
print("Passed DNA and RNA tests")
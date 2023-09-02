"""
Identify Chain Businesses

Dataset：
1. A list of businesses containing only popular chains (Starbucks, Walmart, etc)。Business names are of the format：CHAIN_NAME - LOCATION - BUSINESS_ID。
2. A particular location。This is the last line of input entered.

Unfortunately, input 1 may contain duplicate lines ( exact line appearing multiple times).
"""

from collections import Counter

class Business:
    def __init__(self, name, location, identifier):
        self.name = name
        self.location = location
        self.identifier = identifier

class Chain:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

def detect_and_order_chain_businesses(businesses, location):
    """
    desc ordered retrun location and the corresponding count nubmer.
    If the number of multiple unique businesses on a location is the same, 
    use the chain name to sort alphabetically as a secondary sorting criteria.
    
    Input:
        businesses: list of Business: List of Business objects.
        location: str: Location of the chain we are interested in.
    
    Output:
        List of Chain objects.
    """
    # count the frequency of each business
    business_counter = Counter()
    for business in businesses:
        business_counter[business.name] += 1

    # sort the business by frequency and name
    chains = []
    for name, frequency in business_counter.items():
        chains.append(Chain(name, frequency))
    chains.sort(key=lambda chain: (-chain.frequency, chain.name))

    # return the location and the corresponding count number
    return location, chains[0].frequency
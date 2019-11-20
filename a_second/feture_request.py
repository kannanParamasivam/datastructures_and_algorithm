''' Givent the feature requests fro Kindle from customers, find the n most popular futures requested '''

from collections import defaultdict
import re

def popularNFeatures(numFeatures, topFeatures, possibleFeatures, numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    if  possibleFeatures == None or len(possibleFeatures) == 0:
        return []
    
    possible_features_set = set()

    word_frequency = defaultdict(int)

    

    for feature in possibleFeatures:

        possible_features_set.add(feature)

    

    for featureRequest in featureRequests:

        featureRequest = re.sub(r'[?|$|.|!]',r'',featureRequest)

        unique_features_per_user = set(featureRequest.split())

        for feature_word in unique_features_per_user:
            feature_word = feature_word.lower()

            if feature_word in possible_features_set:

                word_frequency[feature_word]+=1;

    top_n_features = sorted(word_frequency,key=word_frequency.get,reverse=True)[:topFeatures]
        
    return top_n_features
    



featureRequests = ["I wish my kindle battery battery had even more storage!", "I wish the battery life on my kindle waterproof lasted 2 years","I read in the bath and would enjoy a waterproof kindle"]
print(popularNFeatures(6,0,["storage","battery","hover","alexa","waterproof","solar"],3,featureRequests))
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
import os
from googletrans import Translator
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "agrobharat-a6dd2-firebase-adminsdk-phayg-2ada36986e.json"
keywords = ["wheat","rice","maize","cotton"]   ################ PADDY = RICE #####################
stopper = [".",",","!"]
db = firestore.Client()
translator = Translator()
lang_dict = {"Kannada":"kn","Bengali":"bn","Malay":"ms","english":"en","tamil":"ta","Telugu":"te","Gujarati":"gu","hindi":"hi","Urdu":"ur" }
collection =["english","tamil","hindi"]
translator = Translator(service_urls=[  'translate.google.com'   ])


for col in collection:
    convert_list = []
    doc_ref = db.collection(col)
    docs = doc_ref.stream()
    for doc in docs:
        #print(doc.id)
        #print(u'Document data: {}'.format(doc.to_dict()))
        data = doc.to_dict()
        id = doc.id
        desc = data["description"]
        desc2 = data["description"]
        desc_list = []
        desc1 = " "
        bucket = " "
        #for d in desc:
        #    print(d)
        #    if d not in stopper:                    ###################### REMOVE STOPPERS ###############################
        #        desc_list.append(d)
        #        #print(desc_list)    
        #desc1 = ''.join([str(elem) for elem in desc_list])
        #print(desc)
        #print(data["Description"].split("."))
        #print(type(desc))
        transtext = translator.translate(desc)
        desc = transtext.text
        desc = desc.lower()
        for key in keywords:
            if key in desc.split():
                #print(type(key))
                bucket = key
        #print(bucket)
        print("From collection(OG LANG):",col)
        print("Post id:",id)
        print("Username:",data["username"])
        print("Timestamp:",data["timeStamp"])
        print("Description translated:",desc)
        print("Bucket:",bucket)
        print(" "*3)
        srcc = str(translator.detect(desc2))
        srcc = srcc[14] + srcc[15]
        #print("SRCCCCCCCCC",srcc)
        for lang in collection:
            if lang != col:
                convert_list.append(lang)
            elif lang == col:
                OG = lang    

       
        
    print(convert_list)        














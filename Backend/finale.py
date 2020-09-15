import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
import os
from googletrans import Translator
import re
import copy

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "agrobharat-a6dd2-firebase-adminsdk-phayg-2ada36986e.json"
keywords = ["wheat","rice","maize","cotton"]
stopper = [".",",","!"]
db = firestore.Client()
lang_dict = {"Kannada":"kn","Bengali":"bn","Malay":"ms","english":"en","tamil":"ta","Telugu":"te","Gujarati":"gu","hindi":"hi","Urdu":"ur" }
collection =["english","tamil","hindi"]

while True:
    translator = Translator()
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
            for key in keywords:
                if key in desc.split():
                    print(type(key))
                    bucket = key
            #print(bucket)
            print("From collection(OG LANG):",col)
            print("Post id:",id)
            print("Username:",data["username"])
            print("Timestamp:",data["timeStamp"])
            print("Description translated:",desc)
            print("Bucket:",bucket)
            print(" "*3)
   
            #for lang in collection:
            #   if lang != col:
            #    convert_list.append(lang)

            for conv in collection:
                transtext = translator.translate(desc, dest=lang_dict[conv])
                desc1 = transtext.text
                new_buck = bucket + "_" + conv            
                bucket_post = db.collection(new_buck).document(id)
                bucket_post.set({
                    u'description': desc1,
                    u'imageURL': data["imageURL"],
                    u'timeStamp': data["timeStamp"],
                    u'username': data["username"]
                }, merge=True)
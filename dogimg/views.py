from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
from .models import dogcharacter

model=load_model('./my_model2')
Image_size=[224,224]

resultlist = {0: 'Chihuahua',
1: 'Japanese spaniel',
2: 'Maltese',
3: 'Pekingese',
4: 'Shih-Tzu',
5: 'King Charles Spaniel',
6: 'papillon',
7: 'English Toy Terrier',
8: 'Rhodesian Ridgeback',
9: 'Afghan Hound',
10: 'Basset Hound',
11: 'Beagle',
12: 'Bloodhound',
13: 'Bluetick',
14: 'Black and tan Coonhound',
15: 'Treeing Walker Coonhound',
16: 'English Foxhound',
17: 'Redbone Coonhound',
18: 'Borzoi',
19: 'Irish Wwolfhound',
20: 'Italian Greyhound',
21: 'Whippet',
22: 'Ibizan Hound',
23: 'Norwegian Elkhound',
24: 'Otterhound',
25: 'Saluki',
26: 'Scottish Deerhound',
27: 'Weimaraner',
28: 'Staffordshire Bullterrier',
29: 'American Staffordshire Terrier',
30: 'Bedlington Terrier',
31: 'Border Terrier',
32: 'Kerry Blue Terrier',
33: 'Irish Terrier',
34: 'Norfolk Terrier',
35: 'Norwich Terrier',
36: 'Yorkshire Terrier',
37: 'Wire Fox Terrier',
38: 'Lakeland Terrier',
39: 'Sealyham Terrier',
40: 'Airedale Terrier',
41: 'Cairn Terrier',
42: 'Australian Terrier',
43: 'Dandie Dinmont Terrier',
44: 'Boston Terrier',
45: 'Miniature Schnauzer',
46: 'Giant Schnauzer',
47: 'Standard Schnauzer',
48: 'Scottish Terrier',
49: 'Tibetan Terrier',
50: 'Silky Terrier',
51: 'Soft Coated Wheaten Terrier',
52: 'West Highland White Terrier',
53: 'Lhasa Apso',
54: 'Flat-Coated Retriever',
55: 'Curly-Coated Retriever',
56: 'Golden Retriever',
57: 'Labrador Retriever',
58: 'Chesapeake Bay Retriever',
59: 'German Shorthaired Pointer',
60: 'Vizsla',
61: 'English Setter',
62: 'Irish Setter',
63: 'Gordon Setter',
64: 'Brittany',
65: 'Clumber Spaniel',
66: 'English Springer Spaniel',
67: 'Welsh Springer Spaniel',
68: 'Cocker Spaniel',
69: 'Sussex Spaniel',
70: 'Irish Water Spaniel',
71: 'Kuvasz',
72: 'Schipperke',
73: 'Belgian Groenendael',
74: 'Belgian Malinois',
75: 'Briard',
76: 'Kelpie',
77: 'Komondor',
78: 'Old English Sheepdog',
79: 'Shetland Sheepdog',
80: 'Collie',
81: 'Border Collie',
82: 'Bouvier des Flandres',
83: 'Rottweiler',
84: 'German Shepherd',
85: 'Dobermann Pinscher',
86: 'Miniature Pinscher',
87: 'Greater Swiss Mountain Dog',
88: 'Bernese Mountain Dog',
89: 'Appenzeller Sennenhund',
90: 'Entlebucher Mountain Dog',
91: 'Boxer',
92: 'Bullmastiff',
93: 'Tibetan Mastiff',
94: 'French Bulldog',
95: 'Great Dane',
96: 'Saint Bernard',
97: 'Eskimo Dog',
98: 'Malamute',
99: 'Siberian Husky',
100: 'Affenpinscher',
101: 'Basenji',
102: 'Pug',
103: 'Leonberger',
104: 'Newfoundland',
105: 'Great Pyrenees',
106: 'Samoyed',
107: 'Pomeranian',
108: 'Chow Chow',
109: 'Keeshond',
110: 'Brussels Griffon',
111: 'Pembroke Welsh Corgi',
112: 'Cardigan Welsh Corgi',
113: 'Toy Poodle',
114: 'Miniature Poodle',
115: 'Standard Poodle',
116: 'Xoloitzcuintli',
117: 'Dingo'}

def index(request):
    return render(request, 'fileupload.html')

def predict(request):
    if request.method == "POST":
        fileObj = request.FILES['filePath']
        fs = FileSystemStorage()
        
        filePathName = fs.save(fileObj.name, fileObj)
        filePathName = fs.url(filePathName)
        testimage = '.' + filePathName

        img = image.load_img(testimage, target_size=Image_size)
        img = image.img_to_array(img)
        img = img/255.
        img = img.reshape(1,224,224,3)
        predict = model.predict(img)
        import numpy as np
        np_predict = np.argmax(predict)
        answer = resultlist[np_predict]
        
        doginfo = dogcharacter.objects.get(idx=np_predict)
        
        context={'filePathName':filePathName,'answer':answer,'doginfo':doginfo}
        return render(request,'fileupload.html', context)
    else:
        return render(request, 'fileupload.html')



# def predict(request):
#     if request.method == "POST":
#         fileObj = request.FILES['filePath']
#         fs = FileSystemStorage()
        
#         filePathName = fs.save(fileObj.name, fileObj)
#         filePathName = fs.url(filePathName)
#         testimage = '.' + filePathName

#         img = image.load_img(testimage, target_size=Image_size)
#         img = image.img_to_array(img)
#         img = img/255.
#         img = img.reshape(1,224,224,3)
#         predict = model.predict(img)
#         import numpy as np
#         np_predict = np.argmax(predict)
#         np_predict = resultlist[np_predict]

#         context={'filePathName':filePathName,'np_predict':np_predict}
#         return render(request,'fileupload.html', context)
#     else:
#         return render(request, 'fileupload.html')

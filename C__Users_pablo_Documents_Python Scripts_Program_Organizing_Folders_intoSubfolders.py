#!/usr/bin/env python
# coding: utf-8

# In[61]:


import os, re, shutil

keyword = re.compile('''(
(.*(python|programming|data|R)(.*))
)''',re.VERBOSE)
file = []
countpdf = 0
countpdfneg = 0
counttxt = 0
countjpeg = 0
countzip = 0
countmp3 = 0
countfolder = 0
countexe = 0
countapp = 0
countepub = 0
total = []

for filename in os.listdir('C:/Users/pablo/Downloads/'):
    if filename.endswith('.pdf') and keyword.findall(filename.lower()):
        file = ''.join(filename)
        countpdf += 1
        print('\n' + file)
        
    elif filename.endswith('.pdf') and not keyword.findall(filename.lower()):
        countpdfneg +=1
        
    if filename.lower().endswith('.txt'):
        counttxt += 1
        
    elif filename.lower().endswith('.zip'):
        countzip += 1
        
    elif filename.lower().endswith('.jpeg'):
        countjpeg += 1
        
    elif filename.lower().endswith('.mp3'):
        countmp3 += 1
        
    elif filename.lower().endswith('.File folder'):
        countfolder += 1
        
    elif filename.lower().endswith('.exe'):
        countexe += 1
        
    elif filename.lower().endswith('.app'):
        countapp += 1
        
    elif filename.lower().endswith('.epub'):
        countapp += 1
        
print("\nThere are " + str(countpdf) + ' ' + "files that end with .pdf and contain at leat one keyword")
print("\nThere are " + str(countpdfneg) + ' ' + "files that end with .pdf but do not have keywords")
print("\nThere are " + str(counttxt) + ' ' + "files that end with .txt" )
print("\nThere are " + str(countjpeg) + ' ' + "files that end with .jpeg")
print("\nThere are " + str(countzip) + ' ' + "files that end with .zip")
print("\nThere are " + str(countmp3) + ' ' + "files that end with .mp3")
print("\nThere are " + str(countfolder) + ' ' + "files that end with .folder")
print("\nThere are " + str(countexe) + ' ' + "files that end with .exe")
print("\nThere are " + str(countapp) + ' ' + "files that end with .app")
print("\nThere are " + str(countepub) + ' ' + "files that end with .epub")


# In[60]:


import os, re, shutil

datakeyword = re.compile('''(
(.*(python|programming|data|R)(.*))
)''',re.VERBOSE)

mushroomkeyword = re.compile('''(
(.*(mushroom))
)''', re.VERBOSE)

inkscapekeyword = re.compile('''(
(.*(inkscape))
)''', re.VERBOSE)

for folderName, subfolders, filenames in os.walk('C:/Users/pablo/Downloads/'):
    print('\nThe current folder is ' + folderName)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        if not os.path.exists('C:/Users/pablo/Downloads/Applications'):
            os.makedirs('C:/Users/pablo/Downloads/Applications')
    break

    
for filename in os.listdir('C:/Users/pablo/Downloads/'):
    '''Moving PDF files to its folder'''
    if filename.lower().endswith('.pdf'):
        shutil.move('C:/Users/pablo/Downloads/' + filename, 'C:/Users/pablo/Downloads/PDF')
    
    '''Moving app files to its folder'''
    if filename.lower().endswith('.app'):
        shutil.move('C:/Users/pablo/Downloads/'+ filename, 'C:/Users/pablo/Downloads/Applications')
    
    '''Creating PDF subFolders'''
    
    if not os.path.exists('C:/Users/pablo/Downloads/PDF/Data_Science'):
        os.makedirs('C:/Users/pablo/Downloads/PDF/Data_Science')
    if not os.path.exists('C:/Users/pablo/Downloads/PDF/Mushrooms'):
        os.makedirs('C:/Users/pablo/Downloads/PDF/Mushrooms')
    if not os.path.exists('C:/Users/pablo/Downloads/PDF/Inkscape'):
        os.makedirs('C:/Users/pablo/Downloads/PDF/Inkscape')
        
    '''Moving PDF files to respective Subfolders according to their keywords'''
        
for pdf in os.listdir('C:/Users/pablo/Downloads/PDF'):
    if pdf.endswith('.pdf') and datakeyword.findall(pdf.lower()):
        shutil.move('C:/Users/pablo/Downloads/PDF/' + pdf, 'C:/Users/pablo/Downloads/PDF/Data_Science')
    break
    
for pdf in os.listdir('C:/Users/pablo/Downloads/PDF'):
    if pdf.endswith('.pdf') and mushroomkeyword.findall(pdf.lower()):
        shutil.move('C:/Users/pablo/Downloads/PDF/' + pdf, 'C:/Users/pablo/Downloads/PDF/Mushrooms')
    break

for pdf in os.listdir('C:/Users/pablo/Downloads/PDF'):
    if pdf.endswith('.pdf') and inkscapekeyword.findall(pdf.lower()):
        shutil.move('C:/Users/pablo/Downloads/PDF/' + pdf, 'C:/Users/pablo/Downloads/PDF/Inkscape')



# In[ ]:





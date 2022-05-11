import os

def sorter (folder="C:/Users/Fabia/Pictures"): 
    
    #folder = 'C:/Users/Fabian/Desktop/Analysis/File_sorter/Example'

    for entry in os.scandir(folder):
        #dirname = os.path.join(folder, entry.name)
        #print (dirname)


        if not entry.name.startswith('.') and entry.is_file():
            if entry.name[0:3] =="IMG" or "VID": 
                year= entry.name[3:7] 
                month= entry.name[7:9] 
                if not os.path.exists(folder+'/'+year+'_'+month):
                    os.mkdir(folder+'/'+year+'_'+month)
                try:
                    os.rename(folder+"/"+entry.name, folder+"/"+year+'_'+month+"/"+entry.name)
                except FileExistsError :
                    pass
            else: 
                print("Nothing to sort here!")

import os, uuid
MainFolder = input("Path to the folder with the files (Example: C:/Users/GHOST/Desktop/MyFolder): ")
Counter = 0
for root, dirs, files in os.walk(MainFolder):
    for file in files:
        if (file[-4:].lower() == ".dat"):
            FilePath = os.path.join(root, file)
            CurrentFile = open(FilePath, "r")
            NewData = ""
            for Line in CurrentFile:
                if (Line[0:4].lower() == "guid"):
                    NewGUID = uuid.uuid4().hex
                    NewData = NewData + "GUID " + NewGUID
                    print("[Rewrited]", FilePath)
                    Counter+=1
                    if (Line[-1:] == "\n"):
                        NewData = NewData + "\n"
                else:
                    NewData = NewData + Line
            CurrentFile.close()
            CurrentFile = open(FilePath, "w")
            CurrentFile.write(NewData)
            CurrentFile.close()
print("Total GUIDs rewritten:", Counter)
input()

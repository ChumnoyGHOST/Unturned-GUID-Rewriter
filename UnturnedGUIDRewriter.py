import os, uuid
MainFolder = input("Path to the folder with the files (Example: C:/Users/GHOST/Desktop/MyFolder): ")
GUIDsRewritten = 0
Errors = 0
Warnings = 0
encodings = ["UTF-8", "Windows-1250", "Windows-1252"]
for root, dirs, files in os.walk(MainFolder):
    for file in files:
        if (file[-4:].lower() == ".dat"):
            FilePath = os.path.join(root, file)
            GoodEncoding = False
            for Encoding in encodings:
                try:
                    if Encoding != encodings[0]:
                        print("[Warning] It is recommended to set the encoding to UTF-8 instead of ", Encoding, ": ", FilePath, sep = '')
                        Warnings += 1
                    CurrentFile = open(FilePath, "r", encoding=Encoding)
                    GoodEncoding = True
                except UnicodeDecodeError:
                    continue
            if not(GoodEncoding):
                Errors += 1
                print("[Error] Unknown encoding:", FilePath)
                continue
            NewData = ""
            try:
                for Line in CurrentFile:
                    if (Line[0:4].lower() == "guid"):
                        NewGUID = uuid.uuid4().hex.upper()
                        NewData = NewData + "GUID " + NewGUID
                        print("[Success] Rewrited - ", NewGUID, ": ", FilePath, sep = '')
                        GUIDsRewritten += 1
                        if (Line[-1:] == "\n"):
                            NewData = NewData + "\n"
                    else:
                        NewData = NewData + Line
                CurrentFile.close()
                CurrentFile = open(FilePath, "w", encoding="UTF-8")
                CurrentFile.write(NewData)
            except:
                print("[Error] Failed to read", Encoding, "encoded file:", FilePath)
                Errors += 1
            CurrentFile.close()
print("Total GUIDs rewritten:", GUIDsRewritten)
if Warnings > 0:
    print("Warnings:", Warnings)
if Errors > 0:
    print("Errors:", Errors)
input()

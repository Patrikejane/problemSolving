def New_Folder(files):
    if len(files):
        return "New Folder"
    else:
        return '"'+'New Folder' +' (' + str(len(files))+ ')' + '"'


print(New_Folder([[]]))

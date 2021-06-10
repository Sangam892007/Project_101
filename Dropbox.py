from os import access, name
import dropbox

class uplaodDropBox(object):
    def __init__(self, accessToken):
        self.accesstoken = accessToken

    def uploadFiles(self, targetFile, sourceFile):
        connection = dropbox.Dropbox(self.accesstoken)
        with open(sourceFile, 'rb') as f:
            connection.files_upload(f.read(), targetFile)

def main():
    accesstoken = 'sl.AyYgJE7-a_Hv1U48V0ImprCp0jabH3lPLGfMVXys5sWectzFINith1o9fwCtmbDHn2gvyOVra_jfQM-kfb0QiBXFrVHw9wrZId-PWKsA6G0D8TB5kJal7zxbuQcpsslyRnbWI06sfS0'
    transfer = uplaodDropBox(accesstoken)
    sourcefile = "Sorter.py"
    targetfile = "/test/Sorter.py"

    transfer.uploadFiles(targetfile, sourcefile)

if __name__ == "__main__":
    main()
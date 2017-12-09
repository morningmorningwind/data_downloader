# encoding: utf-8
import requests, os, sys, zipfile, shutil

class DataDownloader:
    '''
    A simple data downloader written in python, very convenient for serving scientific data from url.
    It can also be used for other downloading tasks.
    For example (downloading datasets from "https://xxx.com" to a local directory "datasets"):
>>  DATA_FILES = [['https://xxx.com/1.dat', 'datasets/1.dat'], ['https://xxx.xxx/2.dat', 'datasets/2.dat']]
>>  d = DataDownloader(DATA_FILES) # initialize the downloader with DATA_FILES to be downloaded.
>>  d.download() # download all the files in the list.
>>  d.upzip() # unzip all files in the .zip files in to the same directory with the .zip file
>>  # (here do whatever you want with the downloaded datasets)
>>  d.cleanup() # delete all the files in the list after doing the tasks.
    '''
    def __init__(self, files, auto=False, disp=False):
        self.files = files
        # for a dropbox link, we should change it to the true url of the file:
        for i in range(len(files)):
            self.files[i][0] = self.files[i][0].replace('www.dropbox.com', 'dl.dropboxusercontent.com')
        if auto:
            print('Automatically downloading datasets...')
            self.download(disp=disp)
            self.unzip(disp=disp)
            self.cleanup(disp=disp)
            print('Datasets are downloaded.')
            
    def get_dir_name(self, fullpath):
        if os.name != 'nt':
            divider = '/'
        else:
            divider = '\\'

        s = fullpath.split(divider)
        directory = divider.join(s[:-1])
        name = s[-1]
        return directory, name
        
    def exists(self, fullpath):
        directory, name = self.get_dir_name(fullpath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if os.path.isfile(fullpath):
            return True
        else:
            return False
    
    def is_downloadable(self, url):
        h = requests.head(url, allow_redirects=True)
        header = h.headers
        content_type = header.get('content-type')
        if 'text' in content_type.lower():
            return False
        if 'html' in content_type.lower():
            return False
        return True

    def unzip(self, disp=True):
        for url, path in self.files:
            if self.exists(path):
                if path[-4:] == '.zip':
                    directory, name = self.get_dir_name(path)
                    zip_ref = zipfile.ZipFile(path, 'r')
                    zip_ref.extractall(directory)
                    zip_ref.close()
                    if disp:
                        print('%s is unzipped.' % path)

    def download(self, force=False, disp=True):
        for url, path in self.files:
            if not force:
                if self.exists(path):
                    if disp:
                        print(path + ' has already been downloaded. Skipped.')
                    continue
            if self.is_downloadable(url):
                with open(path, "wb") as f:
                    if disp:
                        print('Downloading %s from %s' % (path, url))                   
                    response = requests.get(url, allow_redirects=True, stream=True)
                    total_length = response.headers.get('content-length',None)
                    if total_length is None:
                        f.write(response.content)
                    else:
                        dl = 0
                        total_length = int(total_length)
                        for data in response.iter_content(chunk_size=4096):
                            dl += len(data)
                            f.write(data)
                            if disp:
                                done = int(50 * dl / total_length)
                                sys.stdout.write("\r[%s%s] %d/%d" % ('=' * done, ' ' * (50-done), dl, total_length) )    
                                sys.stdout.flush()
                        if disp:
                            sys.stdout.write("\n")
            else:
                print('Warning:' + url + ' is not downloadable. Skipped.')    
                
    def cleanup(self, disp=True):
        for url, path in self.files:
            if self.exists(path):
                os.remove(path)
                if disp:
                    print('%s is removed.' % path)
            else:
                if disp:
                    print("%s doesn't exist." % path)
            directory, name = self.get_dir_name(path)
            if os.name != 'nt':
                divider = '/'
            else:
                divider = '\\'
            mac = directory+divider+'__MACOSX'
            if os.path.exists(mac):
                shutil.rmtree(mac)

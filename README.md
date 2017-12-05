A simple data downloader written in python, very convenient for serving scientific data from url. The url can be a Dropbox sharing link or any other types of links linking to an online file. It can also be used for other downloading tasks.
<h2>Simple Usage</h2> 
<p>
    For example (downloading datasets from "https://xxx.com" to a local directory "datasets"):
  </p>
<p>>>  DATA_FILES = [['https://xxx.com/1.zip', 'datasets/1.zip'], ['https://xxx.xxx/2.zip', 'datasets/2.zip']]</p>
<p>>>  d = DataDownloader(DATA_FILES, auto=True, disp=True) # initialize the downloader with DATA_FILES to be downloaded.</p>
<p>It will automatically download the file, and zip it into the folder "datasets/", and then delete the .zip file</p>
<h2> Advanced Usage</h2>
<p>
    For example (downloading datasets from "https://xxx.com" to a local directory "datasets"):
  </p>
  
<p>>>  DATA_FILES = [['https://xxx.com/1.dat', 'datasets/1.dat'], ['https://xxx.xxx/2.dat', 'datasets/2.dat']]</p>
<p>>>  d = DataDownloader(DATA_FILES) # initialize the downloader with DATA_FILES to be downloaded.</p>
<p>>>  d.download() # download all the files in the list.</p>
<p>>>  d.upzip() # unzip all files in the .zip files in to the same directory with the .zip file</p>
<p>>>  \# (here do whatever you want with the downloaded datasets)</p>
<p>>>  d.cleanup() # delete all the files in the list after doing the tasks.</p>


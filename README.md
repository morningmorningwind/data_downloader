A simple data downloader written in python, very convenient for serving scientific data from urls. The urls can be a Dropbox sharing links or any other types of links linking to an online file. It can also be used for other downloading tasks.
## Simple Usage

For example (downloading datasets from "https://xxx.com" to a local directory "datasets"):
```python
>>  DATA_FILES = [['https://xxx.com/1.zip', 'datasets/1.zip'], ['https://xxx.xxx/2.zip', 'datasets/2.zip']]
>>  d = DataDownloader(DATA_FILES, auto=True, disp=True) # initialize the downloader with DATA_FILES to be downloaded.
```
It will automatically download the file, zip it into the folder "datasets/", and then delete the .zip file.

## Advanced Usage

For example (downloading datasets from "https://xxx.com" to a local directory "datasets"):
```python
>>  DATA_FILES = [['https://xxx.com/1.dat', 'datasets/1.dat'], ['https://xxx.xxx/2.dat', 'datasets/2.dat']]
>>  d = DataDownloader(DATA_FILES) # initialize the downloader with DATA_FILES to be downloaded.
>>  d.download() # download all the files in the list.
>>  d.upzip() # unzip all files in the .zip files in to the same directory with the .zip file
>>  # (here do whatever you want with the downloaded datasets)
>>  d.cleanup() # delete all the files in the list after doing the tasks.
```


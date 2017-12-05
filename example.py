# encoding: utf-8
from data_downloader import DataDownloader
DATASETS =[
    ['https://www.dropbox.com/s/oi12styucu69q8r/empirical.zip?dl=0', 'data/empirical.zip'],
    ]
d = DataDownloader(DATASETS, auto=True, disp=True)

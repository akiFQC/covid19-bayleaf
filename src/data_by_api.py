import requests
import json
import glob
import os 

class Collector:
    def __init__(self, usr, pw, dirpath):
        self.usr =usr
        self.pw = pw
        self.dirpath = dirpath
        os.makedirs(self.dirpath, exist_ok=True)

    def get(self) :
        pass

def main():
    co = Collector(usr="akiFQC", pw="anonymous",dirpath="../test//tes_tcollect")

if __name__ == "__main__":
    main()
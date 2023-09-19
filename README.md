# Real Estate Scraper



## Description
This project intent is to compile all houses for sale with a base price at the Australian State of Queensland, this spider will crawl over ads of each region following pagination links and gathering all house information of each ad for further analysis, excluding ads under offer or already sold. 

## Requirements

Python 3.10+


## Installation

To clone the repository, type the code below in a shell :

```bash
  git clone https://github.com/ObsidianShark/RealStateScraper-Scrapy.git
  cd realestate
```

To install dependencies, run the command bellow :

```bash
  pip install -r requirements.txt
```



## Usage

Spiders list:

* domain_SEQ - To crawl over South East Queensland
* domain_CQ - To crawl over Central Queensland
* domain_NQ - To crawl over North Queensland
* domain_FNQ - To crawl over Far North Queensland


To crawl a desired region pick a spider name and run the command bellow:

```bash
  scrapy crawl your_spider
```

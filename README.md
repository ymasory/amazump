# amazump #

Dump your amazon.com purchases into json/xml/csv!

## Install Scrapy ##

- Install Python.
You probably already have it installed.

- Install [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html).

```sh
$ sudo pip install Scrapy
```

## Scrape your Amazon account ##

Run the crawler, dumping your orders to a json file:

```sh
$ cd scrapy/crawl
$ scrapy crawl orders -o dump.json -t json
```

Xml and Csv formats are also supported by Scrapy:

```sh
$ scrapy crawl orders -o dump.xml -t xml
$ scrapy crawl orders -o dump.csv -t csv
```

## Analyze the dump file ##

We've written a few analyses you may wish to run on your dump file.
Only Json dumps are supported.

- Install GHC.

```sh
$ sudo apt-get install ghc6 # Debian-based Linux
$ brew install ghc          # Mac, via Homebrew
```

- Compile the analysis script.

```sh
$ cd scrapy/analyze
$ ghc -o anazump anazump.hs
```

- Run the analysis script.

```sh
$ ./anazump
```

## Develop ##
- The crawler is written in Python and uses the Scrapy framework.
- The analysis script is written in Haskell.
- Contributions welcome so long as they are your original work and licensed under this project's license.


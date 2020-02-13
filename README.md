# vstup.com parser
This is a parser for get information about all students in 2019 who aplied or submited documents in institutes in Ukraine.
## Used libraries
- Scrapy

## Instalation

```
pip install scrapy
```

## Test whether the program works

In directory ```.../vstup_parser``` in terminal write:
```
scrapy crawl spider 
```

After launch we get something like:
```terminal
...
http://vstup.info/2019/i2019i217.html
http://vstup.info/2019/i2019i3969.html
http://vstup.info/2019/i2019i193.html
http://vstup.info/2019/i2019i63.html
http://vstup.info/2019/i2019i83.html
http://vstup.info/2019/i2019i3846.html
2020-02-13 18:03:35 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://vstup.info/2019/i2019i295.html> (referer: http://vstup.info/2019/i2019o5.html)
2020-02-13 18:03:35 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://vstup.info/2019/i2019i3846.html> (referer: http://vstup.info/2019/i2019o14.html)
...
```

This means that everything works.

## Launching
In the example, we test for successful launch, but do not receive information.

But we can export information by scrapy tools.

### Main types
- JSON
- CSV
- XML
### Options for export in files

#### JSON
```
scrapy crawl spider -o example.json
```

#### CSV
```
scrapy crawl spider -o example.csv
```

#### XML
```
scrapy crawl spider -o example.xml
```

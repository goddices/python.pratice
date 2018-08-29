from scrapy import cmdline
name = 'btbtdy'
cmd = 'scrapy crawl {0}'.format(name) 
cmdline.execute(cmd.split())
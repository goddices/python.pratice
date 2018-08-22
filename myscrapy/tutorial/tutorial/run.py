from scrapy import cmdline
name = 'loldy'
cmd = 'scrapy crawl {0}'.format(name) 
cmdline.execute(cmd.split())
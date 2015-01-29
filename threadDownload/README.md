# threadDownload.py
Download resources corresponding to the urls with multi threads.

##Note:
1. Note the differences between Thread.start() and Thread.run().<br>

####output with Thread.start()
```bash
lxw threadDownload$ python threadDownload.py 
Thread 5 has finished downloading "http://www.cnblogs.com/lxw0109/p/start_run.html"!
Thread 2 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf"!
Thread 4 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"!
Thread 1 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040a.pdf"!
Thread 0 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040.pdf"!
Thread 3 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040es.pdf"!
Program is Over. Time cost: 1.90802598
```
####output with Thread.run()
```bash
lxw threadDownload$ python threadDownload.py 
Thread 0 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040.pdf"!
Thread 1 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040a.pdf"!
Thread 2 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf"!
Thread 3 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040es.pdf"!
Thread 4 has finished downloading "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"!
Thread 5 has finished downloading "http://www.cnblogs.com/lxw0109/p/start_run.html"!
Program is Over. Time cost: 8.25431513786
```
2. Cannot invoke join() seprately without invoking start() in advance, or we may get the following error info:<br>
**"RuntimeError: cannot join thread before it is started"**


# ab2cb: convert AdBlock Plus content filters to Safari Content Blockers

This is a work in progress! It is not perfect.

The `ab2cb` script reads filter lists as used by AdBlock Plus and produces a JSON Content Blocker file.

Documentation on Content Blockers is a bit sparse. The best source seems to be reading the Safari test source code.

## Usage

```shell
$ ab2cb -h
usage: ab2cb [options] File [File ...]

ab2cb: convert AdBlock content filters to Safari Content Blockers

positional arguments:
  File                  Files to extract from

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --debug               Turn on debug logging.
  --debug-log FILE      Save debug logging to FILE.
  -o FILE, --output FILE
                        Save converted text to FILE. If not given, output to
                        stdout.
```

##  Run Without Installing

1. Clone this repo
2. cd to the repo
3. Activate with the command: `source bin/activate.sh`
4. Run `ab2cb -h`

## References

Safari Extensibility: Content Blocking and Shared Links  
WWDC 2015 Video  
https://developer.apple.com/videos/wwdc/2015/?id=511

EasyList  
https://easylist.adblockplus.org/en/

Writing Adblock Plus filters  
https://adblockplus.org/en/filters

Introduction to WebKit Content Blockers
Surfin' Safari Blog   
https://www.webkit.org/blog/3476/content-blockers-first-look/

AdBlock Plus  
filterClasses.js  
https://github.com/adblockplus/adblockplus/blob/master/lib/filterClasses.js

WebKit Tests  
ContentExtensions.cpp  
http://trac.webkit.org/browser/trunk/Tools/TestWebKitAPI/Tests/WebCore/ContentExtensions.cpp


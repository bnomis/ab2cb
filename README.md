# ab2cb: convert AdBlock Plus content filters to Safari Content Blockers

This is a work in progress! It is not perfect.

The `ab2cb` script reads filter lists as used by AdBlock Plus and produces a JSON Content Blocker file.

Documentation on Content Blockers is a bit sparse. The best source seems to be reading the Safari test source code.


## Examples

### Convert  A File

```shell
$ ab2cb -o blockList.json easylist.txt
```

### Read From stdin and Write To stdout

```shell
$ curl -s https://easylist-downloads.adblockplus.org/easylist.txt | ab2cb > blockList.json
```

## Usage

```shell
$ ab2cb -h
usage: ab2cb [options] [File ...]

ab2cb: convert AdBlock content filters to Safari Content Blockers

positional arguments:
  File                  Files to extract from. If not given read from stdin.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --debug               Turn on debug logging.
  --debug-log FILE      Save debug logging to FILE.
  -o FILE, --output FILE
                        Save converted text to FILE. If not given, output to
                        stdout.
  --no-white            Do not produce white list rules.
```


##  To Run Without Installing

1. Clone this repo
2. cd to the repo
3. Activate with the command: `. bin/activate.sh`
4. Make the dev environment with the command: `make dev`
5. Run `ab2cb -h`


## Testing

Assuming you have `tox` and `pytest` installed, just type `tox` in this directory.


### Testing filters

Currently this is manual: you have to load the content blocker json into Safari, navigate to a test page and check the blocking using the web inspector. I'm working on automating this.

There is a small JavaScript file in the test directory called `check.js` that will load a json file and check the regex compiles.


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


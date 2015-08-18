#!/usr/bin/env python
from __future__ import print_function

import json
import pytest

import ab2cb.ab2cb

class ABCB(object):
    def __init__(self, ab=None, cb=None):
        self.ab = ab or ''
        self.cb = cb or {}
    
    def __eq__(self, other):
        return (self.ab == other.ab) and (self.cb == other.cb)

    def __ne__(self, other):
        return (self.ab != other.ab) or (self.cb != other.cb)

    def json(self, indent=4):
        return json.dumps(self.cb, indent=indent)


def abcb_from_text(text):
    cb = ab2cb.ab2cb.filter_from_text(text)
    return ABCB(ab=text, cb=cb)


ad_urls = [
    ABCB(ab='&ad_box_', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://.*&ad_box_"
        }
    }),
    ABCB(ab='&ad_channel=', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://.*&ad_channel="
        }
    }),
    ABCB(ab='+advertorial.', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://.*\\+advertorial\\."
        }
    }),
    ABCB(ab='&prvtof=*&poru=', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://.*&prvtof=.*&poru="
        }
    }),
    ABCB(ab='-ad-180x150px.', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://.*-ad-180x150px\\."
        }
    }),
    ABCB(ab='://findnsave.*.*/api/groupon.json?', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "://findnsave\\..*\\..*/api/groupon\\.json\\?"
        }
    }),
]


element_hiding = [
    ABCB(ab='###A9AdsMiddleBoxTop', cb={
        "action": {
            "type": "css-display-none",
            "selector": "#A9AdsMiddleBoxTop"
        },
        "trigger": {
            "url-filter": ".*"
        }
    }),
    ABCB(ab='thedailygreen.com#@##AD_banner', cb={
        "action": {
            "type": "css-display-none",
            "selector": "#AD_banner"
        },
        "trigger": {
            "url-filter": ".*",
            "unless-domain": [
                "thedailygreen.com"
            ]
        }
    }),
    ABCB(ab='sprouts.com,tbns.com.au#@##AdImage', cb={
        "action": {
            "type": "css-display-none",
            "selector": "#AdImage"
        },
        "trigger": {
            "url-filter": ".*",
            "unless-domain": [
                "sprouts.com",
                "tbns.com.au"
            ]
        }
    }),
    ABCB(ab='santander.co.uk#@#a[href^="http://ad-emea.doubleclick.net/"]', cb={
        "action": {
            "type": "css-display-none",
            "selector": "a[href^=\"http://ad-emea.doubleclick.net/\"]"
        },
        "trigger": {
            "url-filter": ".*",
            "unless-domain": [
                "santander.co.uk"
            ]
        }
    }),
    ABCB(ab='search.safefinder.com,search.snapdo.com###ABottomD', cb={
        "action": {
            "type": "css-display-none",
            "selector": "#ABottomD"
        },
        "trigger": {
            "url-filter": ".*",
            "if-domain": [
                "search.safefinder.com",
                "search.snapdo.com"
            ]
        }
    }),
    ABCB(ab='tweakguides.com###adbar > br + p[style="text-align: center"] + p[style="text-align: center"]', cb={
        "action": {
            "type": "css-display-none",
            "selector": "#adbar > br + p[style=\"text-align: center\"] + p[style=\"text-align: center\"]"
        },
        "trigger": {
            "url-filter": ".*",
            "if-domain": [
                "tweakguides.com"
            ]
        }
    }),
]




popups = [
    ABCB(ab='||admngronline.com^$popup,third-party', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://admngronline\\.com(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)",
            "load-type": [
                "third-party"
            ],
            "resource-type": [
                "popup"
            ]
        }
    }),
    ABCB(ab='||bet365.com^*affiliate=$popup', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://bet365\\.com(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$).*affiliate=",
            "resource-type": [
                "popup"
            ]
        }
    }),
    
]







third_party = [
    ABCB(ab='||007-gateway.com^$third-party', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://007-gateway\\.com(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)",
            "load-type": [
                "third-party"
            ]
        }
    }),
    ABCB(ab='||anet*.tradedoubler.com^$third-party', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://anet.*\\.tradedoubler\\.com(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)",
            "load-type": [
                "third-party"
            ]
        }
    }),
    ABCB(ab='||doubleclick.net^$third-party,domain=3news.co.nz|92q.com|abc-7.com|addictinggames.com|allbusiness.com|allthingsd.com|bizjournals.com|bloomberg.com|bnn.ca|boom92houston.com|boom945.com|boomphilly.com|break.com|cbc.ca|cbs19.tv|cbs3springfield.com|cbsatlanta.com|cbslocal.com|complex.com|dailymail.co.uk|darkhorizons.com|doubleviking.com|euronews.com|extratv.com|fandango.com|fox19.com|fox5vegas.com|gorillanation.com|hawaiinewsnow.com|hellobeautiful.com|hiphopnc.com|hot1041stl.com|hothiphopdetroit.com|hotspotatl.com|hulu.com|imdb.com|indiatimes.com|indyhiphop.com|ipowerrichmond.com|joblo.com|kcra.com|kctv5.com|ketv.com|koat.com|koco.com|kolotv.com|kpho.com|kptv.com|ksat.com|ksbw.com|ksfy.com|ksl.com|kypost.com|kysdc.com|live5news.com|livestation.com|livestream.com|metro.us|metronews.ca|miamiherald.com|my9nj.com|myboom1029.com|mycolumbusmagic.com|mycolumbuspower.com|myfoxdetroit.com|myfoxorlando.com|myfoxphilly.com|myfoxphoenix.com|myfoxtampabay.com|nbcrightnow.com|neatorama.com|necn.com|neopets.com|news.com.au|news4jax.com|newsone.com|nintendoeverything.com|oldschoolcincy.com|own3d.tv|pagesuite-professional.co.uk|pandora.com|player.theplatform.com|ps3news.com|radio.com|radionowindy.com|rottentomatoes.com|sbsun.com|shacknews.com|sk-gaming.com|ted.com|thebeatdfw.com|theboxhouston.com|theglobeandmail.com|timesnow.tv|tv2.no|twitch.tv|universalsports.com|ustream.tv|wapt.com|washingtonpost.com|wate.com|wbaltv.com|wcvb.com|wdrb.com|wdsu.com|wflx.com|wfmz.com|wfsb.com|wgal.com|whdh.com|wired.com|wisn.com|wiznation.com|wlky.com|wlns.com|wlwt.com|wmur.com|wnem.com|wowt.com|wral.com|wsj.com|wsmv.com|wsvn.com|wtae.com|wthr.com|wxii12.com|wyff4.com|yahoo.com|youtube.com|zhiphopcleveland.com', cb={
        "action": {
             "type": "block"
         },
         "trigger": {
             "url-filter": "^https?://doubleclick\\.net(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)",
             "load-type": [
                 "third-party"
             ],
             "if-domain": [
                 "3news.co.nz",
                 "92q.com",
                 "abc-7.com",
                 "addictinggames.com",
                 "allbusiness.com",
                 "allthingsd.com",
                 "bizjournals.com",
                 "bloomberg.com",
                 "bnn.ca",
                 "boom92houston.com",
                 "boom945.com",
                 "boomphilly.com",
                 "break.com",
                 "cbc.ca",
                 "cbs19.tv",
                 "cbs3springfield.com",
                 "cbsatlanta.com",
                 "cbslocal.com",
                 "complex.com",
                 "dailymail.co.uk",
                 "darkhorizons.com",
                 "doubleviking.com",
                 "euronews.com",
                 "extratv.com",
                 "fandango.com",
                 "fox19.com",
                 "fox5vegas.com",
                 "gorillanation.com",
                 "hawaiinewsnow.com",
                 "hellobeautiful.com",
                 "hiphopnc.com",
                 "hot1041stl.com",
                 "hothiphopdetroit.com",
                 "hotspotatl.com",
                 "hulu.com",
                 "imdb.com",
                 "indiatimes.com",
                 "indyhiphop.com",
                 "ipowerrichmond.com",
                 "joblo.com",
                 "kcra.com",
                 "kctv5.com",
                 "ketv.com",
                 "koat.com",
                 "koco.com",
                 "kolotv.com",
                 "kpho.com",
                 "kptv.com",
                 "ksat.com",
                 "ksbw.com",
                 "ksfy.com",
                 "ksl.com",
                 "kypost.com",
                 "kysdc.com",
                 "live5news.com",
                 "livestation.com",
                 "livestream.com",
                 "metro.us",
                 "metronews.ca",
                 "miamiherald.com",
                 "my9nj.com",
                 "myboom1029.com",
                 "mycolumbusmagic.com",
                 "mycolumbuspower.com",
                 "myfoxdetroit.com",
                 "myfoxorlando.com",
                 "myfoxphilly.com",
                 "myfoxphoenix.com",
                 "myfoxtampabay.com",
                 "nbcrightnow.com",
                 "neatorama.com",
                 "necn.com",
                 "neopets.com",
                 "news.com.au",
                 "news4jax.com",
                 "newsone.com",
                 "nintendoeverything.com",
                 "oldschoolcincy.com",
                 "own3d.tv",
                 "pagesuite-professional.co.uk",
                 "pandora.com",
                 "player.theplatform.com",
                 "ps3news.com",
                 "radio.com",
                 "radionowindy.com",
                 "rottentomatoes.com",
                 "sbsun.com",
                 "shacknews.com",
                 "sk-gaming.com",
                 "ted.com",
                 "thebeatdfw.com",
                 "theboxhouston.com",
                 "theglobeandmail.com",
                 "timesnow.tv",
                 "tv2.no",
                 "twitch.tv",
                 "universalsports.com",
                 "ustream.tv",
                 "wapt.com",
                 "washingtonpost.com",
                 "wate.com",
                 "wbaltv.com",
                 "wcvb.com",
                 "wdrb.com",
                 "wdsu.com",
                 "wflx.com",
                 "wfmz.com",
                 "wfsb.com",
                 "wgal.com",
                 "whdh.com",
                 "wired.com",
                 "wisn.com",
                 "wiznation.com",
                 "wlky.com",
                 "wlns.com",
                 "wlwt.com",
                 "wmur.com",
                 "wnem.com",
                 "wowt.com",
                 "wral.com",
                 "wsj.com",
                 "wsmv.com",
                 "wsvn.com",
                 "wtae.com",
                 "wthr.com",
                 "wxii12.com",
                 "wyff4.com",
                 "yahoo.com",
                 "youtube.com",
                 "zhiphopcleveland.com"
             ]
         }
    }),
    ABCB(ab='||dt00.net^$third-party,domain=~marketgid.com|~marketgid.ru|~marketgid.ua|~mgid.com|~thechive.com', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://dt00\\.net(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)",
            "load-type": [
                "third-party"
            ],
            "unless-domain": [
                "marketgid.com",
                "marketgid.ru",
                "marketgid.ua",
                "mgid.com",
                "thechive.com"
            ]
        }
    }),
    ABCB(ab='||amazonaws.com/newscloud-production/*/backgrounds/$domain=crescent-news.com|daily-jeff.com|recordpub.com|state-journal.com|the-daily-record.com|the-review.com|times-gazette.com', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://amazonaws\\.com/newscloud-production/.*/backgrounds/",
            "if-domain": [
                "crescent-news.com",
                "daily-jeff.com",
                "recordpub.com",
                "state-journal.com",
                "the-daily-record.com",
                "the-review.com",
                "times-gazette.com"
            ]
        }
    }),
    ABCB(ab='||d1noellhv8fksc.cloudfront.net^', cb={
        "action": {
            "type": "block"
        },
        "trigger": {
            "url-filter": "^https?://d1noellhv8fksc\\.cloudfront\\.net(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)"
        }
    }),
    
]






whitelist = [
    ABCB(ab='@@||google.com/recaptcha/$domain=mediafire.com', cb={
        "action": {
            "type": "ignore-previous-rules"
        },
        "trigger": {
            "url-filter": "^https?://google\\.com/recaptcha/",
            "if-domain": [
                "mediafire.com"
            ]
        }
    }),
    ABCB(ab='@@||ad4.liverail.com/?compressed|$domain=majorleaguegaming.com|pbs.org|wikihow.com', cb={
        "action": {
            "type": "ignore-previous-rules"
        },
        "trigger": {
            "url-filter": "^https?://ad4\\.liverail\\.com/\\?compressed$",
            "if-domain": [
                "majorleaguegaming.com",
                "pbs.org",
                "wikihow.com"
            ]
        }
    }),
    ABCB(ab='@@||advertising.autotrader.co.uk^$~third-party', cb={
        "action": {
            "type": "ignore-previous-rules"
        },
        "trigger": {
            "url-filter": "^https?://advertising\\.autotrader\\.co\\.uk(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)"
        }
    }),
    ABCB(ab='@@||advertising.racingpost.com^$image,script,stylesheet,~third-party,xmlhttprequest', cb={
        "action": {
            "type": "ignore-previous-rules"
        },
        "trigger": {
            "url-filter": "^https?://advertising\\.racingpost\\.com(?:[\\x00-\\x24\\x26-\\x2C\\x2F\\x3A-\\x40\\x5B-\\x5E\\x60\\x7B-\\x7F]|$)",
            "resource-type": [
                "image",
                "style-sheet",
                "script",
                "raw"
            ]
        }
    }),
]


# test the ABCB equality/notequal operators
class TestABCB(object):
    def test_eq(self):
        a = ABCB()
        b = ABCB()
        assert a == b
    
        ab = 'string'
        
        a = ABCB(ab=ab)
        b = ABCB(ab=ab)
        assert a == b
    
        cb = {
            "action": {
                "type": "block"
            },
            "trigger": {
                "url-filter": "://findnsave\\..*\\..*/api/groupon\\.json\\?"
            }
        }
    
        a = ABCB(cb=cb)
        b = ABCB(cb=cb)
        assert a == b
        
        a = ABCB(ab=ab, cb=cb)
        b = ABCB(ab=ab, cb=cb)
        assert a == b
    
    
    def test_neq(self):
        ab = 'string'
        cb = {
            "action": {
                "type": "block"
            },
            "trigger": {
                "url-filter": "://findnsave\\..*\\..*/api/groupon\\.json\\?"
            }
        }
        
        a = ABCB()
        b = ABCB(ab=ab)
        assert a != b
    
        a = ABCB()
        b = ABCB(cb=cb)
        assert a != b

        a = ABCB(ab=ab)
        b = ABCB(cb=cb)
        assert a != b


@pytest.mark.parametrize('abcb', ad_urls)
class TestAdURLs(object):
    def test_url(self, abcb):
        out = abcb_from_text(abcb.ab)
        assert out == abcb


@pytest.mark.parametrize('abcb', element_hiding)
class TestElementHiding(object):
    def test_element(self, abcb):
        out = abcb_from_text(abcb.ab)
        assert out == abcb


@pytest.mark.parametrize('abcb', popups)
class TestPopups(object):
    def test_popup(self, abcb):
        out = abcb_from_text(abcb.ab)
        assert out == abcb


@pytest.mark.parametrize('abcb', third_party)
class TestThirdParty(object):
    def test_third_party(self, abcb):
        out = abcb_from_text(abcb.ab)
        assert out == abcb


@pytest.mark.parametrize('abcb', whitelist)
class TestWhiteList(object):
    def test_whitelist(self, abcb):
        out = abcb_from_text(abcb.ab)
        assert out == abcb
        
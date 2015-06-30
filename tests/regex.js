#!/usr/bin/env node

// test regexs are valid in JavaScript

var fs = require('fs');

function test_regex(regex){
    try{
        reg = new RegExp(regex);
    }
    catch (e){
        console.log(e);
        return false;
    }
    return true;
}

//var regs = ['ab+x', '(?:regex'];


var fn = '/Users/simonb/src/ab2cb/tests/regex.txt';

fs.readFile(fn, function(err, data){
    if(err){
        console.log(err);
        throw err;
    }
    var regs = data.toString().split('\n');
    var len = regs.length;

    for (var i = 0; i < len; i++){
        var r = regs[i].trim();
        
        if(!r){
            continue;
        }
        
        if(test_regex(r)){
            console.log('good', r);
        }
        else{
            console.log('bad', r);
        }
    }
});
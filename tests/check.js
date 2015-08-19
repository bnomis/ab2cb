#!/usr/bin/env node
// simple check of a content block json file
// JSON parsing works
// RegEx compiles
// exits with code 0 on success
// exits with code 1 on error

var fs = require('fs');
var exit_value = 0;

process.argv.forEach(function(val, index, array) {
    if(index > 1){
        if(!process_file(val)){
            exit_value = 1;
        }
    }
});
process.exit(exit_value);


function process_file(fn){
    var good = true;
    var data = fs.readFileSync(fn);
    var rules = JSON.parse(data);
    var len = rules.length;

    for (var i = 0; i < len; i++){
        var r = rules[i];
    
        if(!r){
            continue;
        }
    
        if(!test_rule(r)){
            console.log('failed rule', r);
            good = false;
        }
    }
    return good;
}


function test_rule(rule){
    var state = true;
    
    if(rule["trigger"]["url-filter"]){
        if(!test_regex(rule["trigger"]["url-filter"])){
            state = false;
        }
    }
    return state;
}


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






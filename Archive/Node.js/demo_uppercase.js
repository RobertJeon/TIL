// import uc from 'upper-case';
// const http = require('http');

// http.createServer(function (req, res) {
//     res.writeHead(200, {'Content-Type': 'text/html'});
//     res.write(uc.upperCase("Hello World!"));
//     res.end();
// }).listen(8080);


// var uc = require('upper-case');
// Error [ERR_REQUIRE_ESM]
// import { upperCase } from "upper-case";
// var http = require('http');
// var uc = require('upper-case');

// http.createServer(function (req, res) {
//     res.writeHead(200, {'Content-Type': 'text/html'});
//     res.write(uc.upperCase("Hello World!"));
//     res.end();
// }).listen(8080);

var http = require('http');
var uc = require('uppercase');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(uc("Hello World!"));
    res.end();
}).listen(8080);

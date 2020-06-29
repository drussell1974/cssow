'use strict';
var express = require('express');
var markdown = require('./renderGithubMarkdown'); // loads ./routes/index.js
var http = require('http');
var path = require('path');

var port = process.env.MARKSERVICE_DOWN_MIDDLEWARE__PORT_INT || 3031

// Middleware:
var web = express();
web.set('views', path.join(__dirname, 'views'));
web.use(require('stylus').middleware(path.join(__dirname, 'public')));
web.use(express.static(path.join(__dirname, 'public')));

web.get('/:filename', markdown.render);

process.on('SIGTERM', shutDown); // Doesn't work in win32 os.
process.on('SIGINT', shutDown);

http.createServer(web).listen(port, function(){
  console.log('Express server listening on port ' + port);
  console.log('options=', markdown.options);
});

function shutDown() {
  console.log('Shutting server down. No longer listening on port ' + port + '.');
  process.exit();
}
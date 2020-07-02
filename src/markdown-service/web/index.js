'use strict';

var express = require('express');
var http = require('http');
var path = require('path');

var port = process.env.MARKDOWN_SERVICE__PORT_INT || 3003

// Markdown

var path = require('path');
var GithubMarkdown = require('./lib/markdown.js');

var mdOpts = {
  flavor: 'markdown',
};

function RenderMarkdown() {
  this.options = {};

  this.render = function(req, res) {
    var md = new GithubMarkdown();
    md.on("pipe", function(src) {
        console.log(src);
    });
    var debug = req.param('debug', false);
    md.debug = debug;
    md.bufmax = 2048;
    md.returnType = req.param('format', 'html');

    var fileName = path.join(__dirname, 'views', req.params.course_name, req.params.lesson_name, req.params.activity_name, req.params.file_name);
    md.render(fileName, mdOpts, function(err) {
      if (err) { res.write('>>>' + err); res.end(); return; }
      else md.pipe(res);
    });
  };
}

var markd = new RenderMarkdown();
markd.render = markd.render.bind(markd);

// Middleware:
var app = express();

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  next();
});

app.get('/:course_name/:lesson_name/:activity_name/:file_name', markd.render);

process.on('SIGTERM', shutDown); // Doesn't work in win32 os.
process.on('SIGINT', shutDown);

http.createServer(app).listen(port, function(){
  console.log('Markdown Document Service: listening on port ' + port);
  console.log('options=', markd.options);
});

function shutDown() {
  console.log('Shutting server down. No longer listening on port ' + port + '.');
  process.exit();
}
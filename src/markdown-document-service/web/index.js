'use strict';

var express = require('express');
var http = require('http');
var path = require('path');

var port = process.env.MARKDOWN_SERVICE_MIDDLEWARE__PORT_INT || 8082

// Markdown

var path = require('path');
var GithubMarkdown = require('./scripts/github-markdown.js');

var mdOpts = {
  flavor: 'markdown',
};

function RenderMarkdown() {
  this.options = {};

  this.render = function(req, res) {
    var md = new GithubMarkdown();
    var debug = req.param('debug', false);
    md.debug = debug;
    md.bufmax = 2048;
    var fileName = path.join(__dirname, 'views', req.params.filename);
    md.render(fileName, mdOpts, function(err) {
      if (err) { res.write('>>>' + err); res.end(); return; }
      else md.pipe(res);
    });
  };
}

var markd = new RenderMarkdown();
markd.render = markd.render.bind(markd);

// Middleware:
var web = express();
web.get('/:filename', markd.render);

process.on('SIGTERM', shutDown); // Doesn't work in win32 os.
process.on('SIGINT', shutDown);

http.createServer(web).listen(port, function(){
  console.log('Express server listening on port ' + port);
  console.log('options=', markd.options);
});

function shutDown() {
  console.log('Shutting server down. No longer listening on port ' + port + '.');
  process.exit();
}
'use strict';
/*
 * GET /markdown:filename.
 */
var path = require('path');
var GithubMarkdown = require('./scripts/github-markdown.js');

var mdOpts = {
  flavor: 'markdown',
};

function RenderGithubMarkdown() {
  this.options = {};

  this.render = function(req, res) {
    var md = new GithubMarkdown();
    var debug = req.param('debug', false);
    md.debug = debug;
    md.bufmax = 2048;
    var fileName = path.join('views', req.params.filename);
    md.render(fileName, mdOpts, function(err) {
      if (err) { res.write('>>>' + err); res.end(); return; }
      else md.pipe(res);
    });
  };
}

var singleton = new RenderGithubMarkdown();
singleton.render = singleton.render.bind(singleton);
module.exports = singleton;

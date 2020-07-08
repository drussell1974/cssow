const express = require('express');
const path = require('path');
const app = express();
require('dotenv').config()

/* Get Environment Variables from dotenv config (required above)*/

const {
    STUDENT_WEB__WEB_SERVER_PORT_INT, /* replace port in devserver */
    STUDENT_WEB__CSSOW_API_URI, /* uri for accessing cssow json api*/
    STUDENT_WEB__DEFAULT_SCHEMEOFWORK, /* default scheme of work */
    STUDENT_WEB__MARKDOWN_SERVICE_URI, /* uri for markdown documents */
 } = process.env

app.use(express.static(path.join(__dirname, 'build')));
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

app.listen(STUDENT_WEB__WEB_SERVER_PORT_INT, function() {
    console.log(`index.js: listening on port ${STUDENT_WEB__WEB_SERVER_PORT_INT}...`)
});

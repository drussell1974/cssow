const express = require('express');
const path = require('path');
const app = express();
const cors = require('cors');
require('dotenv').config()

/* Get Environment Variables from dotenv config (required above)*/
const {
    STUDENT_WEB__WEB_SERVER_PORT_INT = process.env.STUDENT_WEB__WEB_SERVER_PORT_INT,
    STUDENT_WEB__CSSOW_API_URI = process.env.STUDENT_WEB__CSSOW_API_URI,
} = process.env

app.use(cors());
app.use(express.static(path.join(__dirname, 'build')));
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

app.listen(STUDENT_WEB__WEB_SERVER_PORT_INT, function() {
    console.log(`index.js: STUDENT_WEB__CSSOW_API_URI=${STUDENT_WEB__CSSOW_API_URI}`);
    console.log(`index.js: listening on port ${STUDENT_WEB__WEB_SERVER_PORT_INT}...`);
});

# Prerequisites

Use 'yarn install' from package.json to install the prerequisites, or run directly from the command line...

# packages

Use 'yarn test' from package.json to run 'jest', or run directly from the command line...

Use 'yarn build' from package.json to create production deployment and tar file 'webpack --mode production && tar -czf ../../build/teacher_react_apps/teacher-react-apps.build.tar.gz build' ...

Use 'yarn build' from package.json to create development deployment and copy to teacher_web website 'webpack --mode development && cp -R build ../../src/teacher_web/web/static/default/js/teacher_react_apps' ...

## full calendar support

https://fullcalendar.io/docs/react

yarn add @fullcalendar/react @fullcalendar/daygrid @fullcalendar/interaction

# Run the api service and website

1. Switch to the virtual environment

> cd src/teacher_web

> source [path to .venv] .venv/flask/bin/activate

2. 127.0.0.1:3002

# Create an alert

3. Do something to create an alert

4. Verify web service is returning a started message
    - Check the sow_alerts table for a record
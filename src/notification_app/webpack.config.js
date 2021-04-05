const webpack = require('webpack');
const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
require('dotenv').config()

/* Get Environment Variables from dotenv config (required above)*/

const {
   STUDENT_WEB__WEB_SERVER_PORT_INT: port_int, /* replace port in devserver */
   STUDENT_WEB__CSSOW_API_URI: api_uri, /* uri for accessing cssow json api*/
   STUDENT_WEB__DEFAULT_INSTITUTE: default_institute, /* default institute */
   STUDENT_WEB__DEFAULT_DEPARTMENT: default_department, /* default department */
   STUDENT_WEB__DEFAULT_SCHEMEOFWORK: default_schemeofwork, /* default scheme of work */
} = process.env

module.exports = {
   mode: "development",
   entry: './app/App.js',
   output: {
      path: path.join(__dirname, '/build/'),
      publicPath: '/',
      filename: 'notification-app/bundle.js'
   },
   node: {
      fs: 'empty'
   },
   devServer: {
      inline: true,
      port: port_int,
      contentBase:path.join(__dirname,'./build'),
      historyApiFallback: true,
   },
   module: {
      rules: [
         {
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
               presets: ["@babel/preset-env", "@babel/react"]
            }
         },
         {
            test:/\.css$/,
            use:[
               'style-loader',
               'css-loader',
               ],
         },
         {
            test:/\.eot$/,
            loader:'file-loader',
            options:{
               outputPath:'assets',
            }
         },
         {
            test:/\.jpg(2*)$/,
            loader:'file-loader',
            options:{
               outputPath:'assets',
            }
         },
         {
            test:/\.svg$/,
            loader:'file-loader',
            options:{
               outputPath:'assets',
            }
         },
         {
            test:/\.ttf$/,
            loader:'file-loader',
            options:{
               outputPath:'assets',
            }
         },
         {
            test:/\.woff(2*)$/,
            loader:'file-loader',
            options:{
               outputPath:'assets',
            }
         }
      ]
   },
   plugins:[
      /* Create custom variables accessible throughout solution */
       new webpack.DefinePlugin({
          "REACT_APP_STUDENT_WEB__CSSOW_API_URI": JSON.stringify(api_uri),
       })
   ]
}
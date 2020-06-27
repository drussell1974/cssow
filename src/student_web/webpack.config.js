const webpack = require('webpack');
const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
require('dotenv').config()

/* Get Environment Variables from dotenv config (required above)*/

const {
   STUDENT_WEB__WEB_SERVER_PORT_INT: port_int, /* replace port in devserver */
   STUDENT_WEB__CSSOW_API_URI: api_uri, /* uri for accessing cssow json api*/
   STUDENT_WEB__DEFAULT_SCHEMEOFWORK: default_schemeofwork, /* default scheme of work */
} = process.env

module.exports = {
   mode: "development",
   entry: './app/App.js',
   output: {
      path: path.join(__dirname, '/build/'),
      filename: 'bundle.js'
   },
   devServer: {
      inline: true,
      port: port_int,
      contentBase:path.join(__dirname,'./build'),
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
            use:'file-loader',
         },
         {
            test:/\.jpg(2*)$/,
            use:'file-loader',
         },
         {
            test:/\.svg$/,
            use:'file-loader',
         },
         {
            test:/\.ttf$/,
            use:'file-loader',
         },
         {
            test:/\.woff(2*)$/,
            use:'file-loader',
         }
      ]
   },
   plugins:[
      new HtmlWebpackPlugin({
         template: './app/index.html'
      }),
      new CopyPlugin([
         { from: 'assets', to: 'assets' },
         { from: 'node_modules/github-markdown-css/github-markdown.css', to: 'assets/css' },
       ]),
       /* Create custom variables accessible throughout solution */
       new webpack.DefinePlugin({
          "STUDENT_WEB__CSSOW_API_URI":JSON.stringify(api_uri),
          "STUDENT_WEB__DEFAULT_SCHEMEOFWORK": JSON.stringify(default_schemeofwork), 
       })
   ]
}
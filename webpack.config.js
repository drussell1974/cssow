const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
   mode: "development",
   entry: './reactapp/App.js',
   output: {
      path: path.join(__dirname, '/build/'),
      filename: 'bundle.js'
   },
   devServer: {
      inline: true,
      port: 8001,
      contentBase:'./build',
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
         }
      ]
   },
   plugins:[
      new HtmlWebpackPlugin({
         template: './reactapp/index.html'
      })
   ]
}
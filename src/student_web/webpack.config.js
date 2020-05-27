const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
   mode: "development",
   entry: './app/App.js',
   output: {
      path: path.join(__dirname, '/build/'),
      filename: 'bundle.js'
   },
   devServer: {
      inline: true,
      port: 8001,
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
       ]),
   ]
}
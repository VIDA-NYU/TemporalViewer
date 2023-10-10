const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    
    mode: 'development',

    entry: {
        egocloud: path.resolve(__dirname, '../../playground/index.ts')
    },

    module: {
        rules: [
          {
            test: /\.(js|ts)x?$/,
            exclude:  /node_modules/,
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env', '@babel/react', '@babel/typescript']
            }
          },
          {
            test: /\.css$/,
            use: [
                'style-loader',
                'css-loader'
                ]
        },
        {
            test: /\.(png|svg|jpg|gif)$/,
            use: [
                'file-loader'
                ]
        }
        ]
      },
    
    plugins: [ new HtmlWebpackPlugin(
        {
            title: 'TemporalViewer',
            filename: 'index.html',
            template: path.resolve(__dirname, '../../playground/index.html')
        }
    )],
    
    resolve: {
        extensions: ['.ts', '.js']
    },
    
    // output: {
    //     path: path.resolve(__dirname, '../playground/dist'),
    //     filename: '[name].js' 
    // },
    
    devServer: {

        static: {
            directory: path.resolve(__dirname, '../../playground')
        },

        port: 3000,
        open: true,
        hot: true,
        compress: true,
        historyApiFallback: true
    }
}
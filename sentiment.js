var Sentiment = require('sentiment')

var sentiment = new Sentiment();
var docx = sentiment.analyze("i love beautiful apples");

console.log(docx)
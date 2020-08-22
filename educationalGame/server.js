var connect = require('connect');
var serveStatic = require('serve-static');

connect()
    .use(serveStatic(__dirname))
    .listen(5050, () => console.log('Server running on 5050...'));

//The adress is: http://localhost:5050/
var http = require('http');
var dt = require('./myfirstmodule');
// 모듈을 찾는 데 을 사용한다는 점에 유의하세요 ./. 즉, 모듈이 Node.js 파일과 동일한 폴더에 있음을 의미합니다.

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write("The date and time are currently: " + dt.myDateTime());
    res.end();
}).listen(8080);
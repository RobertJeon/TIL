var http = require('http');
// 모율을 포함하려면 require() 모듈 이름과 함께 함수를 사용

// http 모듈에 액세스 할 수 있으며 서버를 생성할 수 있습니다.
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('Hello World!!!!!');
}).listen(8080);
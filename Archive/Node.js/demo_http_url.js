var http = require('http');
http.createServer(function (req, res) {
    // 메소드의 첫 번째 인수 res.writeHead()는 상태 코드이고, 200은 모두 정상임을 의미하며, 두 번째 인수는 응답 헤더를 포함하는 객체입니다.
    res.writeHead(200, {'Content-Type': 'text/html'});
    // 전달된 함수에는 클라이언트의 요청을 개체(http.IncomingMessage 개체)로 나타내는 인수가 http.createServer() 
    res.write(req.url);
    res.end();
}).listen(8080);
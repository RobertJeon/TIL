// "Formidable"이라는 파일 업로드 작업을 위한 매우 좋은 모듈이 있습니다.

var formidable = require('formidable');

// 1단계: 업로드 양식 만들기
var http = require('http');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
}).listen(8080);

// 2단계: 업로드된 파일 구문 분석
// 업로드된 파일이 서버에 도달하면 구문 분석할 수 있도록 Formidable 모듈을 포함합니다.
// 파일이 업로드되고 구문 분석되면 컴퓨터의 임시 폴더에 저장됩니다.

var http = require('http');
var formidable = require('formidable');

http.createServer(function (req, res) {
    if (req.url == '/fileupload') {
        var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            res.write('File uploaded');
            res.end();
        });
    } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
        res.write('<input type="file" name="filetoupload"><br>');
        res.write('<input type="submit">');
        res.write('</form>');
        return res.end();
    }
}).listen(8080);

// 3단계: 파일 저장
// 파일이 서버에 성공적으로 업로드되면 임시 폴더에 저장됩니다.
// 이 디렉터리의 경로는 parse()메서드의 콜백 함수에서 세 번째 인수로 전달된 "files" 개체에서 찾을 수 있습니다.
// 선택한 폴더로 파일을 이동하려면 파일 시스템 모듈을 사용하고 파일 이름을 바꿉니다.

var http = require('http');
var formidable = require('formidable');
var fs = require('fs');

http.createServer(function (req, res) {
    if (req.url == '/fileupload') {
        var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            var oldpath = files.filetoupload.filepath;
            var newpath = 'C:/Users/Your Name/' + files.filetoupload.originalFilename;
        fs.rename(oldpath, newpath, function (err) {
            if (err) throw err;
            res.write('File uploaded and moved!');
            res.end();
        });
    });
    } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
        res.write('<input type="file" name="filetoupload"><br>');
        res.write('<input type="submit">');
        res.write('</form>');
        return res.end();
    }
}).listen(8080);
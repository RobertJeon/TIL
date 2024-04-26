// fs.appendFile()
// AppendFile() 메서드를 사용하여 새 파일을 만듭니다.

var fs = require('fs');

fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
    if (err) throw err;
    console.log('Saved!');
});

// fs.open()
// open() 메서드를 사용하여 비어 있는 새 파일을 만듭니다.

var fs = require('fs');

fs.open('mynewfile2.txt', 'w', function (err, file) {
    if (err) throw err;
    console.log('Saved!');
});

// fs.writeFile()
// writeFile() 메서드를 사용하여 새 파일을 만듭니다.

var fs = require('fs');

fs.writeFile('mynewfile3.txt', 'Hello content!', function (err) {
    if (err) throw err;
    console.log('Saved!');
});

// fs.appendFile()
// fs.appendFile()메서드는 지정된 파일의 끝에 지정된 내용을 추가합니다.
var fs = require('fs');

fs.appendFile('mynewfile1.txt', ' This is my text.', function (err) {
    if (err) throw err;
    console.log('Updated!');
});

// fs.writeFile()
// fs.writeFile()메서드는 지정된 파일과 콘텐츠를 대체합니다.
var fs = require('fs');

fs.writeFile('mynewfile3.txt', 'This is my text', function (err) {
    if (err) throw err;
    console.log('Replaced!');
});

// fs.unlink()
// fs.unlink()메소드는 지정된 파일을 삭제합니다.
var fs = require('fs');

fs.unlink('mynewfile2.txt', function (err) {
    if (err) throw err;
    console.log('File deleted!');
});

// fs.rename()
// fs.rename()메서드는 지정된 파일의 이름을 바꿉니다.
var fs = require('fs');

fs.rename('mynewfile1.txt', 'myrenamedfile.txt', function (err) {
    if (err) throw err;
    console.log('File Renamed!');
});
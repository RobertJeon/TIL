// 컴퓨터의 모든 작업은 이벤트입니다. 연결이 이루어지거나 파일이 열릴 때와 같습니다.

var fs = require('fs');
var rs = fs.createReadStream('./demofile.txt');
rs.on('open', function () {
    console.log('The file is open');
});

// Node.js에는 "이벤트"라는 내장 모듈이 있는데, 여기서 자신만의 이벤트를 생성하고, 실행하고, 수신할 수 있습니다.
// 내장 이벤트 모듈을 포함하려면 require() 메소드를 사용하십시오. 
// 또한 모든 이벤트 속성과 메서드는 EventEmitter 객체의 인스턴스입니다. 
// 이러한 속성과 메서드에 액세스하려면 EventEmitter 객체를 생성하세요.

var events = require('events');
var eventEmitter = new events.EventEmitter();

// EventEmitter 객체를 사용하여 자신의 이벤트에 이벤트 핸들러를 할당할 수 있습니다.
var events = require('events');
var eventEmitter = new events.EventEmitter();

//Create an event handler:
var myEventHandler = function () {
  console.log('I hear a scream!');
}

//Assign the event handler to an event:
eventEmitter.on('scream', myEventHandler);

//Fire the 'scream' event:
eventEmitter.emit('scream');
// Boolean

let isDone: boolean = false;

// Number

let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;

// String

let color: string = "blue";
color = 'red';

let fullName: string = `Bob Bobbington`;
let age: number = 37;
let sentence: string = `Hello, my name is ${ fullName }.
I'll be ${ age + 1 } years old next month.`;

let sentence_2: string = "Hello, my name is " + fullName + ".\n\n" +
    "I'll be " + (age + 1) + " years old next month.";

// Array

let list: number[] = [1, 2, 3];
let list2: Array<number> = [1, 2, 3];

// Tuple

// 튜플 타입으로 선언
let x: [string, number];
// 초기화
x = ["hello", 10]; // 성공
// 잘못된 초기화
// x = [10, "hello"]; // 오류

console.log(x[0].substring(1)); // 성공
// console.log(x[1].substring(1)); // 오류, 'number'에는 'substring' 이 없습니다.

// x[3] = "world"; // 오류, '[string, number]' 타입에는 프로퍼티 '3'이 없습니다.

// console.log(x[5].toString()); // '[string, number]' 타입에는 프로퍼티 '5'가 없습니다.


// Enum

// enum Color {Red, Green, Blue}
// let c: Color = Color.Green;

// enum Color {Red = 1, Green, Blue}
// let c: Color = Color.Green;

// enum Color {Red = 1, Green = 2, Blue = 4}
// let c: Color = Color.Green;

enum Color {Red = 1, Green, Blue}
let colorName: string = Color[2];

console.log(colorName); // 값이 2인 'Green'이 출력됩니다.


import {A, hello} from "./Parent.js";

hello();

var a = new A();
var b = new A();
console.log(A.name);
console.log(A.name);
var h = new hello();
h.prototype = {"word" : "world"}
Object.assign(hello, {"a": "Changed"})
// a.prototype.name = "Changed"
console.log(a.name);
console.log(b.name);
a.desc = "Desc: A"
b.desc = "Desc: B"
console.log(a.desc)
console.log(b.desc)
console.log(h.word)

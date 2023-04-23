class A {
    constructor() {
        console.log("A: hello")
    }

    hello() {
        console.log('AHELLO: hello')
    }

    static name = "AClass";
    static world() {
        console.log('AWorld')
    }

    desc = "Init Desc";
}

export {A};
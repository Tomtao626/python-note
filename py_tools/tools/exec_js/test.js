const fetch = require('node-fetch');

function getM() {
    fetch('https://match.yuanrenxue.com/static/match/match15/main.wasm').then(response =>
        response.arrayBuffer()
    ).then(bytes => WebAssembly.instantiate(bytes)).then(results => {
        let instance = results.instance;
        let q = instance.exports.encode;
        let m = function () {
            let t1 = parseInt(Date.parse(new Date()) / 1000 / 2);
            let t2 = parseInt(Date.parse(new Date()) / 1000 / 2 - Math.floor(Math.random() * (50) + 1));
            return q(t1, t2).toString() + '|' + t1 + '|' + t2;
        }();
        console.log(m)
    })
}

getM()

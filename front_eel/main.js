async function example(type) {
    await eel.example()(callBack)
    let example = await eel.example()()
    console.log('example meow' + example)
}

function callBack(meow) {
    console.log('сallBack meow ' + meow)
}
console.log('HELLO THERE');

const btn = document.querySelector('#showuser');
const div = document.querySelector('#userdata');
const avpic = document.querySelector('#avatar');
const divandfol = document.querySelector('#userandfollow');


function btnPressed() {

    fetch("https://newsapi.org/v2/everything?q=music&from=2022-11-14&sortBy=popularity&apiKey=fc3250f8a4ef484d978a4f6362a209ac")
        .then(response => response.json())
        .then(data => {
            console.log(data)})
        .catch(err => console.log(err))


}


btn.addEventListener('click', btnPressed)



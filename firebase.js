// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js";
import { getDatabase, set, get, update, remove, ref, child } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
import { config } from './config.js';

// Initialize Firebase
const app = initializeApp(config);
const db = getDatabase();
var score = 0;

var metaract = document.querySelector("#metaract");
var interval = document.querySelector("#interval");

var scoreBtn = document.querySelector("#scoreButton");
scoreBtn.addEventListener('click', increaseScore);
var scoreClr = document.querySelector("#scoreClear");
scoreClr.addEventListener('click', clearScore);
var submitBtn = document.querySelector("#submit");
submitBtn.addEventListener('click', sendData);

var test = document.querySelector('#find');
test.addEventListener('click', testing);

function testing(){
    get(child(ref(db), "Test"))
    .then((tree)=>{
        console.log(tree.val());//for example: .Metaract
    });
}

function increaseScore(){
    score++;
    document.querySelector('#score').innerHTML = `score: ${score}`;
}

function clearScore(){
    score = 0;
    document.querySelector('#score').innerHTML = `score: ${score}`;
}

function sendData(){
    set(ref(db, "Test"), {
        Score: score,
        Metaract: metaract.value,
        Interval: interval.value
    })
    .then(()=>{alert("success!");})
    .catch((error)=>{alert(error);})
}
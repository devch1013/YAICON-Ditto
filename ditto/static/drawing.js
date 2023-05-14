const canvas = document.getElementById("jsCanvas");
const ctx = canvas.getContext("2d");
const colors = document.getElementsByClassName("jsColor");
const range = document.getElementById("jsRange");
const mode = document.getElementById("jsMode");
const eraser = document.getElementById("jsEraser");
const saveBtn = document.getElementById("jsSave");
const clear = document.getElementById("jsClear");

const INITIAL_COLOR = "#000000";
const CANVAS_WIDTH = 1042;
const CANVAS_HEIGHT = 677;


ctx.strokeStyle = "#2c2c2c";

canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;

ctx.strokeStyle = INITIAL_COLOR;
ctx.fillStyle = "#ffffff";
ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
ctx.lineWidth = 2.5;

let painting = false;
let filling = false;
let erasing = false;

function stopPainting(){
    painting = false;
}

function startPainting(){
    painting = true;
}

function onMouseMove(event) {
    const x = event.offsetX;
    const y = event.offsetY;
    if (!painting) {
        ctx.beginPath();
        ctx.moveTo(x, y);
    } else{
        ctx.lineTo(x, y);
        ctx.stroke();
    }
}

function handleColorClick(event) {
    const color = event.target.style.backgroundColor;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
}

function handleEraserClick(event) {
    if (erasing == true) {
        erasing = false;
        const color = "#ffffff";
        ctx.strokeStyle = color;
        ctx.fillStyle = color;
    } else {
        erasing = true;
        const color = "#000000";
        ctx.strokeStyle = color;
        ctx.fillStyle = color;
    }
    
}

function handleRangeChange(event) {
    const size = event.target.value;
    ctx.lineWidth = size;
}

function handleModeClick() {
    if (filling == true) {
        filling = false;
        icon = document.getElementById("change-icon");
        icon.classList.replace('fa-paint-roller', 'fa-pencil');
    } else {
        filling = true;
        icon = document.getElementById("change-icon");
        icon.classList.replace('fa-pencil', 'fa-paint-roller');
    }
}

function handleCanvasClick() {
    if (filling) {
        ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    }
}

function handleSaveClick() {
    canvas_url = canvas.toDataURL('image/png');
    document.getElementById('canvas_data').value = canvas_url;
}

function handleClearClick() {
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    ctx.fillStyle = ctx.strokeStyle;
}

if (canvas) {
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", startPainting);
    canvas.addEventListener("mouseup", stopPainting);
    canvas.addEventListener("mouseleave", stopPainting);
    canvas.addEventListener("click", handleCanvasClick);
}

Array.from(colors).forEach(color =>
    color.addEventListener("click", handleColorClick));

if (eraser) {
    eraser.addEventListener("click", handleEraserClick);
}

if (range) {
    range.addEventListener("input", handleRangeChange);
}

if (mode) {
    mode.addEventListener("click", handleModeClick);
}

if (saveBtn) {
    saveBtn.addEventListener("click", handleSaveClick);
}

if (clear) {
    clear.addEventListener("click", handleClearClick);
}
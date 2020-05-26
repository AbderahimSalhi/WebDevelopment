// Select color input
let color = document.getElementById('colorPicker');
// Select size input
let grid = document.getElementById('pixelCanvas');
let sizePicker = document.getElementById('sizePicker');
const height = document.getElementById('inputHeight').value;
const width = document.getElementById('inputWidth').value;

//call the grid table function
makeGrid(height, width);

//add an event listner to retrieve the size of the table
sizePicker.addEventListener('click', function (event) {

    event.preventDefault(); // prevent the refreshement of the page until the submit button is clicked

    grid.firstElementChild.remove();
    let height = document.getElementById('inputHeight').value;
    let width = document.getElementById('inputWidth').value;

    makeGrid(height, width);

});

//declare a grid table function
function makeGrid(height, width) {

    for (i = 0; i < height; i++) {
        let row = grid.insertRow(i);
        for (j = 0; j < width; j++) {
            let column = row.insertCell(j);
            column.addEventListener('click', function (event) {
                console.log(event);
                column.style.backgroundColor = color.value;

            });
        }
    }


};
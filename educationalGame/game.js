maxSize = [1200,800]

function setup() {
  createCanvas(maxSize[0], maxSize[1]);
}
j = 0
function draw() {
    background(155, 245, 250);
    rect(0, maxSize[1]-100, 529, 55, 20);
    rect(600, maxSize[1]-300, 529, 55, 20);
    
    
    for (let i = 1; i<100; i++){
        rect( i++, j*10, 10, 10, 10);
    }
    j++;
    if (j>500){
        j = -1;
    }
    
}

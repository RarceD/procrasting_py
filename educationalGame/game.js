maxSize = [1200, 800];

function setup() {
  createCanvas(maxSize[0], maxSize[1]);
}
let pos = 10;
let i = 1;
function draw() {
  background(155, 245, 250);
  rect(0, maxSize[1] - 100, 529, 55, 20);
  rect(600, maxSize[1] - 300, 529, 55, 20);

  rect(pos + i, 100, 10, 100, 100);
  pos += i * 6;
  if (pos > 1200 || pos < 0) i = -i;
}
